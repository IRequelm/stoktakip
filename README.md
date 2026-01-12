# Stok Takip Mobil Uygulaması

Tablet için tasarlanmış stok takip sistemi. Ürünleri raf ve dolap numaralarına göre takip eder.

## Özellikler

- ✅ Ürün ekleme (ürün adı, numarası, konum tipi ve numarası)
- ✅ Ürün arama (ürün adı veya numarasına göre)
- ✅ Konum bilgisi görüntüleme (hangi rafta veya dolapta)
- ✅ Ürün listesi görüntüleme
- ✅ Ürün silme
- ✅ SQLite veritabanı ile kalıcı veri saklama

## Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

2. Uygulamayı çalıştırın:
```bash
python main.py
```

## Kullanım

### Ürün Ekleme
1. Ana ekrandan "Ürün Ekle" butonuna tıklayın
2. Ürün bilgilerini girin:
   - Ürün Adı
   - Ürün Numarası
   - Konum Tipi (Raf veya Dolap)
   - Konum Numarası
   - Açıklama (opsiyonel)
3. "Kaydet" butonuna tıklayın

### Ürün Arama
1. Ana ekrandan "Ürün Ara" butonuna tıklayın
2. Arama kutusuna ürün adı veya numarasını yazın
3. Sonuçlar otomatik olarak görünecektir
4. Her sonuçta ürünün hangi rafta veya dolapta olduğu gösterilir

### Ürün Silme
- Ana ekrandaki ürün listesinde, silmek istediğiniz ürünün yanındaki "Sil" butonuna tıklayın

## Veritabanı

Uygulama SQLite veritabanı kullanır. Veritabanı dosyası (`stok_takip.db`) uygulama ile aynı klasörde otomatik olarak oluşturulur.

## Ekran Boyutu

Uygulama tablet için optimize edilmiştir (1024x768). Farklı ekran boyutları için `main.py` dosyasındaki `Window.size` değerini değiştirebilirsiniz.
