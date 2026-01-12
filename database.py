import sqlite3
from datetime import datetime
from typing import List, Dict, Optional

class Database:
    def __init__(self, db_name='stok_takip.db'):
        self.db_name = db_name
        self.init_database()
    
    def get_connection(self):
        """Veritabanı bağlantısı oluştur"""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_database(self):
        """Veritabanı tablolarını oluştur"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS urunler (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                urun_adi TEXT NOT NULL,
                urun_no TEXT NOT NULL UNIQUE,
                urun_cinsi TEXT NOT NULL CHECK(urun_cinsi IN ('Bağlantı Elemanı', 'Mekanik', 'Elektronik')),
                birim TEXT NOT NULL CHECK(birim IN ('Adet', 'kg', 'Metre')),
                raf_no TEXT,
                dolap_no TEXT,
                aciklama TEXT,
                ekleme_tarihi TEXT NOT NULL,
                UNIQUE(urun_no, raf_no, dolap_no)
            )
        ''')
        
        # Mevcut tabloda yeni sütunlar yoksa ekle (migration)
        try:
            cursor.execute('ALTER TABLE urunler ADD COLUMN urun_cinsi TEXT')
            cursor.execute('ALTER TABLE urunler ADD COLUMN birim TEXT')
            # Varsayılan değerleri güncelle
            cursor.execute('UPDATE urunler SET urun_cinsi = "Mekanik" WHERE urun_cinsi IS NULL')
            cursor.execute('UPDATE urunler SET birim = "Adet" WHERE birim IS NULL')
        except sqlite3.OperationalError:
            pass
        
        # Eski konum_tipi ve konum_no sütunlarını raf_no ve dolap_no'ya dönüştür
        try:
            # Önce yeni sütunları ekle
            cursor.execute('ALTER TABLE urunler ADD COLUMN raf_no TEXT')
            cursor.execute('ALTER TABLE urunler ADD COLUMN dolap_no TEXT')
            
            # Eski verileri yeni sütunlara taşı
            cursor.execute('''
                UPDATE urunler 
                SET raf_no = CASE WHEN konum_tipi = 'Raf' THEN konum_no ELSE NULL END,
                    dolap_no = CASE WHEN konum_tipi = 'Dolap' THEN konum_no ELSE NULL END
                WHERE raf_no IS NULL AND dolap_no IS NULL
            ''')
        except sqlite3.OperationalError:
            # Sütunlar zaten varsa veya tablo yoksa hata verme
            pass
        
        conn.commit()
        conn.close()
    
    def urun_ekle(self, urun_adi: str, urun_no: str, urun_cinsi: str, birim: str, raf_no: str = "", dolap_no: str = "", aciklama: str = "") -> bool:
        """Yeni ürün ekle"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            # En az bir konum numarası olmalı
            if not raf_no and not dolap_no:
                return False
            
            cursor.execute('''
                INSERT INTO urunler (urun_adi, urun_no, urun_cinsi, birim, raf_no, dolap_no, aciklama, ekleme_tarihi)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (urun_adi, urun_no, urun_cinsi, birim, raf_no or None, dolap_no or None, aciklama, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def urun_ara(self, arama_metni: str) -> List[Dict]:
        """Ürün adına göre arama yap"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM urunler 
            WHERE urun_adi LIKE ? OR urun_no LIKE ?
            ORDER BY urun_adi, raf_no, dolap_no
        ''', (f'%{arama_metni}%', f'%{arama_metni}%'))
        
        sonuclar = []
        for row in cursor.fetchall():
            # Eski format desteği (konum_tipi, konum_no)
            konum_tipi = None
            konum_no = None
            if 'raf_no' in row.keys() and row['raf_no']:
                konum_tipi = 'Raf'
                konum_no = row['raf_no']
            elif 'dolap_no' in row.keys() and row['dolap_no']:
                konum_tipi = 'Dolap'
                konum_no = row['dolap_no']
            elif 'konum_tipi' in row.keys():
                konum_tipi = row['konum_tipi']
                konum_no = row.get('konum_no', '')
            
            sonuclar.append({
                'id': row['id'],
                'urun_adi': row['urun_adi'],
                'urun_no': row['urun_no'],
                'urun_cinsi': row.get('urun_cinsi', 'Mekanik'),
                'birim': row.get('birim', 'Adet'),
                'raf_no': row.get('raf_no', ''),
                'dolap_no': row.get('dolap_no', ''),
                'konum_tipi': konum_tipi,
                'konum_no': konum_no,
                'aciklama': row['aciklama'],
                'ekleme_tarihi': row['ekleme_tarihi']
            })
        
        conn.close()
        return sonuclar
    
    def tum_urunler(self) -> List[Dict]:
        """Tüm ürünleri getir"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM urunler 
            ORDER BY urun_adi, raf_no, dolap_no
        ''')
        
        sonuclar = []
        for row in cursor.fetchall():
            # Eski format desteği (konum_tipi, konum_no)
            konum_tipi = None
            konum_no = None
            if 'raf_no' in row.keys() and row['raf_no']:
                konum_tipi = 'Raf'
                konum_no = row['raf_no']
            elif 'dolap_no' in row.keys() and row['dolap_no']:
                konum_tipi = 'Dolap'
                konum_no = row['dolap_no']
            elif 'konum_tipi' in row.keys():
                konum_tipi = row['konum_tipi']
                konum_no = row.get('konum_no', '')
            
            sonuclar.append({
                'id': row['id'],
                'urun_adi': row['urun_adi'],
                'urun_no': row['urun_no'],
                'urun_cinsi': row.get('urun_cinsi', 'Mekanik'),
                'birim': row.get('birim', 'Adet'),
                'raf_no': row.get('raf_no', ''),
                'dolap_no': row.get('dolap_no', ''),
                'konum_tipi': konum_tipi,
                'konum_no': konum_no,
                'aciklama': row['aciklama'],
                'ekleme_tarihi': row['ekleme_tarihi']
            })
        
        conn.close()
        return sonuclar
    
    def urun_sil(self, urun_id: int) -> bool:
        """Ürün sil"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('DELETE FROM urunler WHERE id = ?', (urun_id,))
            
            conn.commit()
            conn.close()
            return True
        except:
            return False
    
    def urun_guncelle(self, urun_id: int, urun_adi: str, urun_no: str, urun_cinsi: str, birim: str, raf_no: str = "", dolap_no: str = "", aciklama: str = "") -> bool:
        """Ürün bilgilerini güncelle"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            # En az bir konum numarası olmalı
            if not raf_no and not dolap_no:
                return False
            
            cursor.execute('''
                UPDATE urunler 
                SET urun_adi = ?, urun_no = ?, urun_cinsi = ?, birim = ?, raf_no = ?, dolap_no = ?, aciklama = ?
                WHERE id = ?
            ''', (urun_adi, urun_no, urun_cinsi, birim, raf_no or None, dolap_no or None, aciklama, urun_id))
            
            conn.commit()
            conn.close()
            return True
        except:
            return False
