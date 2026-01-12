from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from database import Database
import os

# Tablet için ekran boyutunu ayarla
try:
    Window.size = (1024, 768)
except:
    pass

# Arka plan rengini profesyonel gri yap
Window.clearcolor = (0.92, 0.92, 0.93, 1)  # Biraz daha koyu gri

class AnaEkran(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=0, spacing=0)
        
        # Header - ERP benzeri koyu mavi/gri
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(70), padding=dp(15))
        header_rect = None
        with header.canvas.before:
            Color(0.15, 0.25, 0.35, 1)  # Daha koyu mavi-gri
            header_rect = Rectangle(pos=header.pos, size=header.size)
        
        def update_header_rect(instance, value):
            header_rect.pos = instance.pos
            header_rect.size = instance.size
        
        header.bind(pos=update_header_rect, size=update_header_rect)
        
        # Logo (sol üst köşe)
        logo_path = 'logos/Logo1.png'
        if os.path.exists(logo_path):
            logo = Image(
                source=logo_path,
                size_hint_x=None,
                width=dp(60),
                allow_stretch=True,
                keep_ratio=True
            )
            header.add_widget(logo)
        
        # Başlık
        baslik = Label(
            text='STOK TAKİP SİSTEMİ',
            size_hint_x=1,
            font_size='24sp',
            halign='left',
            valign='middle',
            color=(1, 1, 1, 1),
            bold=True
        )
        baslik.bind(texture_size=baslik.setter('size'))
        header.add_widget(baslik)
        
        layout.add_widget(header)
        
        # Toolbar - Butonlar
        toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(50), padding=dp(10), spacing=dp(10))
        toolbar_rect = None
        with toolbar.canvas.before:
            Color(0.9, 0.9, 0.9, 1)  # Açık gri
            toolbar_rect = Rectangle(pos=toolbar.pos, size=toolbar.size)
        
        def update_toolbar_rect(instance, value):
            toolbar_rect.pos = instance.pos
            toolbar_rect.size = instance.size
        
        toolbar.bind(pos=update_toolbar_rect, size=update_toolbar_rect)
        
        urun_ekle_btn = Button(
            text='+ Yeni Ürün',
            font_size='16sp',
            size_hint_x=None,
            width=dp(150),
            background_color=(0.3, 0.5, 0.7, 1),
            color=(1, 1, 1, 1)
        )
        urun_ekle_btn.bind(on_press=self.urun_ekle_ekranina_git)
        
        urun_ara_btn = Button(
            text='🔍 Ara',
            font_size='16sp',
            size_hint_x=None,
            width=dp(120),
            background_color=(0.5, 0.5, 0.5, 1),
            color=(1, 1, 1, 1)
        )
        urun_ara_btn.bind(on_press=self.urun_ara_ekranina_git)
        
        toolbar.add_widget(urun_ekle_btn)
        toolbar.add_widget(urun_ara_btn)
        toolbar.add_widget(Widget())  # Spacer
        
        layout.add_widget(toolbar)
        
        # Tablo başlığı
        tablo_header = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(45), padding=dp(10))
        tablo_header_rect = None
        with tablo_header.canvas.before:
            Color(0.25, 0.35, 0.45, 1)  # Daha koyu mavi-gri
            tablo_header_rect = Rectangle(pos=tablo_header.pos, size=tablo_header.size)
        
        def update_tablo_header_rect(instance, value):
            tablo_header_rect.pos = instance.pos
            tablo_header_rect.size = instance.size
        
        tablo_header.bind(pos=update_tablo_header_rect, size=update_tablo_header_rect)
        
        headers = ['Ürün Adı', 'Ürün No', 'Cins', 'Birim', 'Raf', 'Dolap', 'İşlemler']
        header_widths = [0.25, 0.15, 0.12, 0.08, 0.08, 0.08, 0.24]
        
        for header_text, width in zip(headers, header_widths):
            header_label = Label(
                text=header_text,
                size_hint_x=width,
                font_size='15sp',
                color=(1, 1, 1, 1),
                bold=True,
                halign='left',
                valign='middle'
            )
            header_label.bind(texture_size=header_label.setter('size'))
            tablo_header.add_widget(header_label)
        
        layout.add_widget(tablo_header)
        
        # ScrollView ile liste - Tablo görünümü
        scroll = ScrollView()
        self.urun_listesi = BoxLayout(orientation='vertical', spacing=dp(2), size_hint_y=None, padding=0)
        self.urun_listesi.bind(minimum_height=self.urun_listesi.setter('height'))
        scroll.add_widget(self.urun_listesi)
        layout.add_widget(scroll)
        
        self.add_widget(layout)
        self.db = Database()
        self.urunleri_yukle()
    
    def urun_ekle_ekranina_git(self, instance):
        self.manager.current = 'urun_ekle'
    
    def urun_ara_ekranina_git(self, instance):
        self.manager.current = 'urun_ara'
    
    def urunleri_yukle(self):
        self.urun_listesi.clear_widgets()
        urunler = self.db.tum_urunler()
        
        if not urunler:
            label = Label(
                text='Henüz ürün eklenmemiş',
                size_hint_y=None,
                height=dp(50),
                font_size='16sp',
                color=(0.4, 0.4, 0.4, 1)
            )
            self.urun_listesi.add_widget(label)
        else:
            for urun in urunler:
                urun_kart = self.urun_karti_olustur(urun)
                self.urun_listesi.add_widget(urun_kart)
    
    def urun_karti_olustur(self, urun):
        # Tablo satırı görünümü
        satir_no = len(self.urun_listesi.children) if hasattr(self.urun_listesi, 'children') else 0
        kart = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(45),
            padding=dp(8)
        )
        
        # Zebra striping - alternatif satırlar
        with kart.canvas.before:
            if satir_no % 2 == 0:
                Color(1, 1, 1, 1)  # Beyaz
            else:
                Color(0.97, 0.97, 0.98, 1)  # Açık gri
            Rectangle(pos=kart.pos, size=kart.size)
            # Alt çizgi
            Color(0.85, 0.85, 0.85, 1)
            Rectangle(pos=(kart.x, kart.y), size=(kart.width, 1))
        
        # Ürün Adı
        urun_adi_label = Label(
            text=urun.get('urun_adi', '')[:30] + ('...' if len(urun.get('urun_adi', '')) > 30 else ''),
            size_hint_x=0.25,
            font_size='14sp',
            halign='left',
            text_size=(None, None),
            color=(0.1, 0.1, 0.1, 1)
        )
        urun_adi_label.bind(texture_size=urun_adi_label.setter('size'))
        
        # Ürün No
        urun_no_label = Label(
            text=urun.get('urun_no', ''),
            size_hint_x=0.15,
            font_size='14sp',
            halign='left',
            text_size=(None, None),
            color=(0.1, 0.1, 0.1, 1)
        )
        
        # Cins
        cins_label = Label(
            text=urun.get('urun_cinsi', 'Mekanik')[:15],
            size_hint_x=0.12,
            font_size='14sp',
            halign='left',
            text_size=(None, None),
            color=(0.2, 0.2, 0.2, 1)
        )
        
        # Birim
        birim_label = Label(
            text=urun.get('birim', 'Adet'),
            size_hint_x=0.08,
            font_size='14sp',
            halign='left',
            text_size=(None, None),
            color=(0.2, 0.2, 0.2, 1)
        )
        
        # Raf
        raf_label = Label(
            text=urun.get('raf_no', '-') or '-',
            size_hint_x=0.08,
            font_size='14sp',
            halign='left',
            text_size=(None, None),
            color=(0.2, 0.2, 0.2, 1)
        )
        
        # Dolap
        dolap_label = Label(
            text=urun.get('dolap_no', '-') or '-',
            size_hint_x=0.08,
            font_size='14sp',
            halign='left',
            text_size=(None, None),
            color=(0.2, 0.2, 0.2, 1)
        )
        
        # İşlemler butonları
        islem_layout = BoxLayout(orientation='horizontal', size_hint_x=0.24, spacing=dp(5))
        
        duzenle_btn = Button(
            text='Düzenle',
            size_hint_x=0.5,
            font_size='12sp',
            background_color=(0.3, 0.5, 0.7, 1),
            color=(1, 1, 1, 1)
        )
        duzenle_btn.bind(on_press=lambda x, u=urun: self.urun_duzenle(u))
        
        sil_btn = Button(
            text='Sil',
            size_hint_x=0.5,
            font_size='12sp',
            background_color=(0.6, 0.2, 0.2, 1),
            color=(1, 1, 1, 1)
        )
        sil_btn.bind(on_press=lambda x, u_id=urun['id']: self.urun_sil(u_id))
        
        islem_layout.add_widget(duzenle_btn)
        islem_layout.add_widget(sil_btn)
        
        kart.add_widget(urun_adi_label)
        kart.add_widget(urun_no_label)
        kart.add_widget(cins_label)
        kart.add_widget(birim_label)
        kart.add_widget(raf_label)
        kart.add_widget(dolap_label)
        kart.add_widget(islem_layout)
        
        return kart
    
    def urun_duzenle(self, urun):
        """Ürün düzenleme ekranına git"""
        self.manager.get_screen('urun_duzenle').urun_yukle(urun)
        self.manager.current = 'urun_duzenle'
    
    def urun_sil(self, urun_id):
        popup = Popup(
            title='Onay',
            content=Label(text='Bu ürünü silmek istediğinize emin misiniz?'),
            size_hint=(0.6, 0.3)
        )
        
        def onayla(instance):
            self.db.urun_sil(urun_id)
            self.urunleri_yukle()
            popup.dismiss()
        
        popup.content = BoxLayout(orientation='vertical', padding=dp(20))
        popup.content.add_widget(Label(text='Bu ürünü silmek istediğinize emin misiniz?'))
        
        buton_layout = BoxLayout(orientation='horizontal', spacing=dp(10), size_hint_y=None, height=dp(50))
        evet_btn = Button(text='Evet', size_hint_x=0.5)
        evet_btn.bind(on_press=onayla)
        hayir_btn = Button(text='Hayır', size_hint_x=0.5)
        hayir_btn.bind(on_press=popup.dismiss)
        
        buton_layout.add_widget(evet_btn)
        buton_layout.add_widget(hayir_btn)
        popup.content.add_widget(buton_layout)
        
        popup.open()
    
    def on_enter(self):
        self.urunleri_yukle()


class UrunEkleEkran(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=0, spacing=0)
        
        # Header
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60), padding=dp(15))
        with header.canvas.before:
            Color(0.2, 0.3, 0.4, 1)
            Rectangle(pos=header.pos, size=header.size)
        
        # Logo
        logo_path = 'logos/Logo1.png'
        if os.path.exists(logo_path):
            logo = Image(
                source=logo_path,
                size_hint_x=None,
                width=dp(50),
                allow_stretch=True,
                keep_ratio=True
            )
            header.add_widget(logo)
        
        # Başlık
        baslik = Label(
            text='YENİ ÜRÜN EKLE',
            size_hint_x=1,
            font_size='20sp',
            halign='left',
            valign='middle',
            color=(1, 1, 1, 1),
            bold=True
        )
        header.add_widget(baslik)
        
        layout.add_widget(header)
        
        # İçerik alanı
        icerik = BoxLayout(orientation='vertical', padding=dp(25), spacing=dp(15))
        
        # Form alanları - Grid layout (2 sütun)
        form_layout = GridLayout(cols=2, spacing=dp(15), size_hint_y=None)
        form_layout.bind(minimum_height=form_layout.setter('height'))
        
        # Ürün Adı
        form_layout.add_widget(Label(text='Ürün Adı *', size_hint_y=None, height=dp(35), font_size='14sp', color=(0.2, 0.2, 0.2, 1)))
        self.urun_adi_input = TextInput(
            multiline=False,
            size_hint_y=None,
            height=dp(35),
            font_size='14sp',
            hint_text='Ürün adını giriniz',
            background_color=(1, 1, 1, 1)
        )
        form_layout.add_widget(self.urun_adi_input)
        
        # Ürün No
        form_layout.add_widget(Label(text='Ürün Numarası *', size_hint_y=None, height=dp(35), font_size='14sp', color=(0.2, 0.2, 0.2, 1)))
        self.urun_no_input = TextInput(
            multiline=False,
            size_hint_y=None,
            height=dp(35),
            font_size='14sp',
            hint_text='Ürün numarasını giriniz',
            background_color=(1, 1, 1, 1)
        )
        form_layout.add_widget(self.urun_no_input)
        
        # Ürün Cinsi
        form_layout.add_widget(Label(text='Ürün Cinsi *', size_hint_y=None, height=dp(35), font_size='14sp', color=(0.2, 0.2, 0.2, 1)))
        self.urun_cinsi_spinner = Spinner(
            text='Mekanik',
            values=('Bağlantı Elemanı', 'Mekanik', 'Elektronik'),
            size_hint_y=None,
            height=dp(35),
            font_size='14sp',
            background_color=(1, 1, 1, 1)
        )
        form_layout.add_widget(self.urun_cinsi_spinner)
        
        # Birim
        form_layout.add_widget(Label(text='Birim *', size_hint_y=None, height=dp(35), font_size='14sp', color=(0.2, 0.2, 0.2, 1)))
        self.birim_spinner = Spinner(
            text='Adet',
            values=('Adet', 'kg', 'Metre'),
            size_hint_y=None,
            height=dp(35),
            font_size='14sp',
            background_color=(1, 1, 1, 1)
        )
        form_layout.add_widget(self.birim_spinner)
        
        # Raf Numarası
        form_layout.add_widget(Label(text='Raf Numarası', size_hint_y=None, height=dp(35), font_size='14sp', color=(0.4, 0.4, 0.4, 1)))
        self.raf_no_input = TextInput(
            multiline=False,
            size_hint_y=None,
            height=dp(35),
            font_size='14sp',
            hint_text='Raf numarasını giriniz',
            background_color=(1, 1, 1, 1)
        )
        form_layout.add_widget(self.raf_no_input)
        
        # Dolap Numarası
        form_layout.add_widget(Label(text='Dolap Numarası', size_hint_y=None, height=dp(35), font_size='14sp', color=(0.4, 0.4, 0.4, 1)))
        self.dolap_no_input = TextInput(
            multiline=False,
            size_hint_y=None,
            height=dp(35),
            font_size='14sp',
            hint_text='Dolap numarasını giriniz',
            background_color=(1, 1, 1, 1)
        )
        form_layout.add_widget(self.dolap_no_input)
        
        # Açıklama
        form_layout.add_widget(Label(text='Açıklama', size_hint_y=None, height=dp(35), font_size='14sp', color=(0.4, 0.4, 0.4, 1)))
        self.aciklama_input = TextInput(
            multiline=True,
            size_hint_y=None,
            height=dp(80),
            font_size='14sp',
            hint_text='Ek açıklama giriniz',
            background_color=(1, 1, 1, 1)
        )
        form_layout.add_widget(self.aciklama_input)
        
        icerik.add_widget(form_layout)
        
        # Butonlar - Toolbar
        toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(50), spacing=dp(10), padding=dp(10))
        with toolbar.canvas.before:
            Color(0.95, 0.95, 0.96, 1)
            Rectangle(pos=toolbar.pos, size=toolbar.size)
        
        kaydet_btn = Button(
            text='Kaydet',
            font_size='16sp',
            size_hint_x=None,
            width=dp(120),
            background_color=(0.2, 0.5, 0.7, 1),
            color=(1, 1, 1, 1)
        )
        kaydet_btn.bind(on_press=self.urun_kaydet)
        
        iptal_btn = Button(
            text='İptal',
            font_size='16sp',
            size_hint_x=None,
            width=dp(120),
            background_color=(0.6, 0.6, 0.6, 1),
            color=(1, 1, 1, 1)
        )
        iptal_btn.bind(on_press=self.ana_sayfaya_don)
        
        toolbar.add_widget(Widget())  # Spacer
        toolbar.add_widget(kaydet_btn)
        toolbar.add_widget(iptal_btn)
        
        icerik.add_widget(toolbar)
        layout.add_widget(icerik)
        
        self.add_widget(layout)
        self.db = Database()
    
    def urun_kaydet(self, instance):
        urun_adi = self.urun_adi_input.text.strip()
        urun_no = self.urun_no_input.text.strip()
        urun_cinsi = self.urun_cinsi_spinner.text
        birim = self.birim_spinner.text
        raf_no = self.raf_no_input.text.strip()
        dolap_no = self.dolap_no_input.text.strip()
        aciklama = self.aciklama_input.text.strip()
        
        # Zorunlu alanlar kontrolü
        if not urun_adi:
            self.hata_goster('Lütfen ürün adını giriniz!')
            return
        
        if not urun_no:
            self.hata_goster('Lütfen ürün numarasını giriniz!')
            return
        
        if not raf_no and not dolap_no:
            self.hata_goster('Lütfen en az bir konum numarası (Raf veya Dolap) giriniz!')
            return
        
        if self.db.urun_ekle(urun_adi, urun_no, urun_cinsi, birim, raf_no, dolap_no, aciklama):
            self.basari_goster('Ürün başarıyla eklendi!')
            # Formu temizle
            self.urun_adi_input.text = ''
            self.urun_no_input.text = ''
            self.urun_cinsi_spinner.text = 'Mekanik'
            self.birim_spinner.text = 'Adet'
            self.raf_no_input.text = ''
            self.dolap_no_input.text = ''
            self.aciklama_input.text = ''
        else:
            self.hata_goster('Bu ürün numarası ve konum kombinasyonu zaten mevcut!')
    
    def hata_goster(self, mesaj):
        popup = Popup(
            title='Hata',
            content=Label(text=mesaj, text_size=(dp(400), None)),
            size_hint=(0.6, 0.3)
        )
        popup.open()
    
    def basari_goster(self, mesaj):
        popup = Popup(
            title='Başarılı',
            content=Label(text=mesaj, text_size=(dp(400), None)),
            size_hint=(0.6, 0.3)
        )
        popup.open()
    
    def ana_sayfaya_don(self, instance):
        self.manager.current = 'ana_ekran'


class UrunDuzenleEkran(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=dp(30), spacing=dp(20))
        
        # Logo ve başlık için üst kısım
        ust_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(80), spacing=dp(20))
        
        # Logo (sol üst köşe)
        logo_path = 'logos/Logo1.png'
        if os.path.exists(logo_path):
            logo = Image(
                source=logo_path,
                size_hint_x=None,
                width=dp(80),
                allow_stretch=True,
                keep_ratio=True
            )
            ust_layout.add_widget(logo)
        
        # Başlık
        baslik = Label(
            text='[b]Ürün Düzenle[/b]',
            size_hint_x=1,
            font_size='28sp',
            markup=True,
            halign='center',
            valign='middle'
        )
        baslik.bind(texture_size=baslik.setter('size'))
        baslik.text_size = (None, None)
        ust_layout.add_widget(baslik)
        
        layout.add_widget(ust_layout)
        
        # Form alanları
        form_layout = BoxLayout(orientation='vertical', spacing=dp(15))
        
        # Ürün Adı
        form_layout.add_widget(Label(text='Ürün Adı:', size_hint_y=None, height=dp(40), font_size='20sp'))
        self.urun_adi_input = TextInput(
            multiline=False,
            size_hint_y=None,
            height=dp(60),
            font_size='20sp',
            hint_text='Ürün adını giriniz'
        )
        form_layout.add_widget(self.urun_adi_input)
        
        # Ürün No
        form_layout.add_widget(Label(text='Ürün Numarası:', size_hint_y=None, height=dp(40), font_size='20sp'))
        self.urun_no_input = TextInput(
            multiline=False,
            size_hint_y=None,
            height=dp(60),
            font_size='20sp',
            hint_text='Ürün numarasını giriniz'
        )
        form_layout.add_widget(self.urun_no_input)
        
        # Ürün Cinsi
        form_layout.add_widget(Label(text='Ürün Cinsi:', size_hint_y=None, height=dp(40), font_size='20sp'))
        self.urun_cinsi_spinner = Spinner(
            text='Mekanik',
            values=('Bağlantı Elemanı', 'Mekanik', 'Elektronik'),
            size_hint_y=None,
            height=dp(60),
            font_size='20sp'
        )
        form_layout.add_widget(self.urun_cinsi_spinner)
        
        # Birim
        form_layout.add_widget(Label(text='Birim:', size_hint_y=None, height=dp(40), font_size='20sp'))
        self.birim_spinner = Spinner(
            text='Adet',
            values=('Adet', 'kg', 'Metre'),
            size_hint_y=None,
            height=dp(60),
            font_size='20sp'
        )
        form_layout.add_widget(self.birim_spinner)
        
        # Raf Numarası
        form_layout.add_widget(Label(text='Raf Numarası (Opsiyonel):', size_hint_y=None, height=dp(40), font_size='20sp'))
        self.raf_no_input = TextInput(
            multiline=False,
            size_hint_y=None,
            height=dp(60),
            font_size='20sp',
            hint_text='Raf numarasını giriniz'
        )
        form_layout.add_widget(self.raf_no_input)
        
        # Dolap Numarası
        form_layout.add_widget(Label(text='Dolap Numarası (Opsiyonel):', size_hint_y=None, height=dp(40), font_size='20sp'))
        self.dolap_no_input = TextInput(
            multiline=False,
            size_hint_y=None,
            height=dp(60),
            font_size='20sp',
            hint_text='Dolap numarasını giriniz'
        )
        form_layout.add_widget(self.dolap_no_input)
        
        # Açıklama
        form_layout.add_widget(Label(text='Açıklama (Opsiyonel):', size_hint_y=None, height=dp(40), font_size='20sp'))
        self.aciklama_input = TextInput(
            multiline=True,
            size_hint_y=None,
            height=dp(120),
            font_size='18sp',
            hint_text='Ek açıklama giriniz'
        )
        form_layout.add_widget(self.aciklama_input)
        
        layout.add_widget(form_layout)
        
        # Butonlar
        buton_layout = BoxLayout(orientation='horizontal', spacing=dp(20), size_hint_y=None, height=dp(80))
        
        guncelle_btn = Button(
            text='Güncelle',
            font_size='24sp',
            size_hint_x=0.5,
            background_color=(0.2, 0.7, 0.2, 1)
        )
        guncelle_btn.bind(on_press=self.urun_guncelle)
        
        iptal_btn = Button(
            text='İptal',
            font_size='24sp',
            size_hint_x=0.5
        )
        iptal_btn.bind(on_press=self.ana_sayfaya_don)
        
        buton_layout.add_widget(guncelle_btn)
        buton_layout.add_widget(iptal_btn)
        
        layout.add_widget(buton_layout)
        
        self.add_widget(layout)
        self.db = Database()
        self.urun_id = None
    
    def urun_yukle(self, urun):
        """Mevcut ürün bilgilerini forma yükle"""
        self.urun_id = urun['id']
        self.urun_adi_input.text = urun.get('urun_adi', '')
        self.urun_no_input.text = urun.get('urun_no', '')
        self.urun_cinsi_spinner.text = urun.get('urun_cinsi', 'Mekanik')
        self.birim_spinner.text = urun.get('birim', 'Adet')
        self.raf_no_input.text = urun.get('raf_no', '')
        self.dolap_no_input.text = urun.get('dolap_no', '')
        self.aciklama_input.text = urun.get('aciklama', '')
    
    def urun_guncelle(self, instance):
        urun_adi = self.urun_adi_input.text.strip()
        urun_no = self.urun_no_input.text.strip()
        urun_cinsi = self.urun_cinsi_spinner.text
        birim = self.birim_spinner.text
        raf_no = self.raf_no_input.text.strip()
        dolap_no = self.dolap_no_input.text.strip()
        aciklama = self.aciklama_input.text.strip()
        
        # Zorunlu alanlar kontrolü
        if not urun_adi:
            self.hata_goster('Lütfen ürün adını giriniz!')
            return
        
        if not urun_no:
            self.hata_goster('Lütfen ürün numarasını giriniz!')
            return
        
        if not raf_no and not dolap_no:
            self.hata_goster('Lütfen en az bir konum numarası (Raf veya Dolap) giriniz!')
            return
        
        if self.db.urun_guncelle(self.urun_id, urun_adi, urun_no, urun_cinsi, birim, raf_no, dolap_no, aciklama):
            self.basari_goster('Ürün başarıyla güncellendi!')
            self.ana_sayfaya_don(None)
        else:
            self.hata_goster('Güncelleme başarısız! Lütfen bilgileri kontrol ediniz.')
    
    def hata_goster(self, mesaj):
        popup = Popup(
            title='Hata',
            content=Label(text=mesaj, text_size=(dp(400), None)),
            size_hint=(0.6, 0.3)
        )
        popup.open()
    
    def basari_goster(self, mesaj):
        popup = Popup(
            title='Başarılı',
            content=Label(text=mesaj, text_size=(dp(400), None)),
            size_hint=(0.6, 0.3)
        )
        popup.open()
    
    def ana_sayfaya_don(self, instance):
        # Ana ekranı yenile
        ana_ekran = self.manager.get_screen('ana_ekran')
        ana_ekran.urunleri_yukle()
        self.manager.current = 'ana_ekran'


class UrunAraEkran(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=dp(30), spacing=dp(20))
        
        # Logo ve başlık için üst kısım
        ust_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(80), spacing=dp(20))
        
        # Logo (sol üst köşe)
        logo_path = 'logos/Logo1.png'
        if os.path.exists(logo_path):
            logo = Image(
                source=logo_path,
                size_hint_x=None,
                width=dp(80),
                allow_stretch=True,
                keep_ratio=True
            )
            ust_layout.add_widget(logo)
        
        # Başlık
        baslik = Label(
            text='[b]Ürün Ara[/b]',
            size_hint_x=1,
            font_size='28sp',
            markup=True,
            halign='left',
            valign='middle'
        )
        baslik.bind(texture_size=baslik.setter('size'))
        ust_layout.add_widget(baslik)
        
        layout.add_widget(ust_layout)
        
        # Arama kutusu
        arama_layout = BoxLayout(orientation='horizontal', spacing=dp(15), size_hint_y=None, height=dp(70))
        
        self.arama_input = TextInput(
            multiline=False,
            size_hint_x=0.8,
            size_hint_y=None,
            height=dp(70),
            font_size='22sp',
            hint_text='Ürün adı veya numarası ile arayın...'
        )
        self.arama_input.bind(text=self.arama_yap)
        
        temizle_btn = Button(
            text='Temizle',
            size_hint_x=0.2,
            size_hint_y=None,
            height=dp(70),
            font_size='20sp'
        )
        temizle_btn.bind(on_press=self.arama_temizle)
        
        arama_layout.add_widget(self.arama_input)
        arama_layout.add_widget(temizle_btn)
        
        layout.add_widget(arama_layout)
        
        # Sonuçlar başlığı
        self.sonuc_baslik = Label(
            text='[b]Arama sonuçları burada görünecek[/b]',
            size_hint_y=None,
            height=dp(50),
            font_size='18sp',
            markup=True
        )
        layout.add_widget(self.sonuc_baslik)
        
        # Sonuçlar listesi
        scroll = ScrollView()
        self.sonuc_listesi = BoxLayout(orientation='vertical', spacing=dp(15), size_hint_y=None)
        self.sonuc_listesi.bind(minimum_height=self.sonuc_listesi.setter('height'))
        scroll.add_widget(self.sonuc_listesi)
        layout.add_widget(scroll)
        
        # Ana sayfa butonu
        ana_sayfa_btn = Button(
            text='Ana Sayfa',
            size_hint_y=None,
            height=dp(70),
            font_size='22sp'
        )
        ana_sayfa_btn.bind(on_press=self.ana_sayfaya_don)
        
        layout.add_widget(ana_sayfa_btn)
        
        self.add_widget(layout)
        self.db = Database()
    
    def arama_yap(self, instance, text):
        if not text.strip():
            self.sonuc_listesi.clear_widgets()
            self.sonuc_baslik.text = 'Arama sonuçları burada görünecek'
            return
        
        sonuclar = self.db.urun_ara(text.strip())
        self.sonuclari_goster(sonuclar)
    
    def sonuclari_goster(self, sonuclar):
        self.sonuc_listesi.clear_widgets()
        
        if not sonuclar:
            self.sonuc_baslik.text = 'Sonuç bulunamadı'
            label = Label(
                text='Aradığınız kriterlere uygun ürün bulunamadı.',
                size_hint_y=None,
                height=dp(60),
                font_size='18sp'
            )
            self.sonuc_listesi.add_widget(label)
        else:
            self.sonuc_baslik.text = f'{len(sonuclar)} sonuç bulundu'
            
            for urun in sonuclar:
                urun_kart = self.urun_karti_olustur(urun)
                self.sonuc_listesi.add_widget(urun_kart)
    
    def urun_karti_olustur(self, urun):
        kart = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=dp(180),
            padding=dp(15),
            spacing=dp(10)
        )
        kart.canvas.before.clear()
        from kivy.graphics import Color, RoundedRectangle
        with kart.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            RoundedRectangle(pos=kart.pos, size=kart.size, radius=[10])
        
        # Ürün adı ve numarası
        urun_bilgi = Label(
            text=f"[b]{urun['urun_adi']}[/b] - No: {urun['urun_no']}",
            size_hint_y=None,
            height=dp(35),
            font_size='22sp',
            halign='left',
            markup=True,
            text_size=(None, None)
        )
        urun_bilgi.bind(texture_size=urun_bilgi.setter('size'))
        
        # Ürün cinsi ve birim
        cins_birim_bilgi = Label(
            text=f"[b]Cins:[/b] {urun.get('urun_cinsi', 'Mekanik')} | [b]Birim:[/b] {urun.get('birim', 'Adet')}",
            size_hint_y=None,
            height=dp(30),
            font_size='18sp',
            halign='left',
            markup=True,
            text_size=(None, None)
        )
        cins_birim_bilgi.bind(texture_size=cins_birim_bilgi.setter('size'))
        
        # Konum bilgisini oluştur
        konum_metni = ""
        if urun.get('raf_no'):
            konum_metni = f"Raf: {urun['raf_no']}"
        if urun.get('dolap_no'):
            if konum_metni:
                konum_metni += f" | Dolap: {urun['dolap_no']}"
            else:
                konum_metni = f"Dolap: {urun['dolap_no']}"
        # Eski format desteği
        if not konum_metni and urun.get('konum_tipi') and urun.get('konum_no'):
            konum_metni = f"{urun['konum_tipi']}: {urun['konum_no']}"
        
        konum_bilgi = Label(
            text=f"[b]Konum:[/b] {konum_metni}" if konum_metni else "[b]Konum:[/b] Belirtilmemiş",
            size_hint_y=None,
            height=dp(40),
            font_size='24sp',
            halign='left',
            markup=True,
            color=(0, 0.6, 0, 1),
            text_size=(None, None)
        )
        konum_bilgi.bind(texture_size=konum_bilgi.setter('size'))
        
        # Açıklama (varsa)
        if urun.get('aciklama'):
            aciklama_label = Label(
                text=f"Açıklama: {urun['aciklama']}",
                size_hint_y=None,
                height=dp(30),
                font_size='16sp',
                halign='left',
                text_size=(None, None)
            )
            aciklama_label.bind(texture_size=aciklama_label.setter('size'))
            kart.add_widget(aciklama_label)
        
        kart.add_widget(urun_bilgi)
        kart.add_widget(cins_birim_bilgi)
        kart.add_widget(konum_bilgi)
        
        # Butonlar
        buton_layout = BoxLayout(orientation='horizontal', spacing=dp(10), size_hint_y=None, height=dp(50))
        
        # Düzenle butonu
        duzenle_btn = Button(
            text='Düzenle',
            size_hint_x=0.5,
            font_size='18sp',
            background_color=(0.2, 0.6, 0.8, 1)
        )
        duzenle_btn.bind(on_press=lambda x, u=urun: self.urun_duzenle(u))
        
        # Sil butonu
        sil_btn = Button(
            text='Sil',
            size_hint_x=0.5,
            font_size='18sp',
            background_color=(0.8, 0.2, 0.2, 1)
        )
        sil_btn.bind(on_press=lambda x, u_id=urun['id']: self.urun_sil(u_id))
        
        buton_layout.add_widget(duzenle_btn)
        buton_layout.add_widget(sil_btn)
        kart.add_widget(buton_layout)
        
        return kart
    
    def urun_duzenle(self, urun):
        """Ürün düzenleme ekranına git"""
        self.manager.get_screen('urun_duzenle').urun_yukle(urun)
        self.manager.current = 'urun_duzenle'
    
    def urun_sil(self, urun_id):
        """Ürün sil"""
        popup = Popup(
            title='Onay',
            content=Label(text='Bu ürünü silmek istediğinize emin misiniz?'),
            size_hint=(0.6, 0.3)
        )
        
        def onayla(instance):
            db = Database()
            db.urun_sil(urun_id)
            self.sonuclari_goster(self.db.urun_ara(self.arama_input.text.strip()))
            popup.dismiss()
        
        popup.content = BoxLayout(orientation='vertical', padding=dp(20))
        popup.content.add_widget(Label(text='Bu ürünü silmek istediğinize emin misiniz?'))
        
        buton_layout = BoxLayout(orientation='horizontal', spacing=dp(10), size_hint_y=None, height=dp(50))
        evet_btn = Button(text='Evet', size_hint_x=0.5)
        evet_btn.bind(on_press=onayla)
        hayir_btn = Button(text='Hayır', size_hint_x=0.5)
        hayir_btn.bind(on_press=popup.dismiss)
        
        buton_layout.add_widget(evet_btn)
        buton_layout.add_widget(hayir_btn)
        popup.content.add_widget(buton_layout)
        
        popup.open()
    
    def arama_temizle(self, instance):
        self.arama_input.text = ''
        self.sonuc_listesi.clear_widgets()
        self.sonuc_baslik.text = 'Arama sonuçları burada görünecek'
    
    def ana_sayfaya_don(self, instance):
        self.manager.current = 'ana_ekran'


class StokTakipApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(AnaEkran(name='ana_ekran'))
        sm.add_widget(UrunEkleEkran(name='urun_ekle'))
        sm.add_widget(UrunDuzenleEkran(name='urun_duzenle'))
        sm.add_widget(UrunAraEkran(name='urun_ara'))
        return sm


if __name__ == '__main__':
    try:
        app = StokTakipApp()
        app.run()
    except Exception as e:
        import traceback
        print(f"Hata oluştu: {e}")
        traceback.print_exc()
        input("Devam etmek için Enter'a basın...")
