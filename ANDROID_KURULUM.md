# Android Tablete Yükleme Rehberi

Stok Takip uygulamanızı Android tablete yüklemek için iki yöntem var:

## Yöntem 1: Buildozer ile APK Oluşturma (Önerilen - Profesyonel)

Bu yöntem ile tam bir Android APK dosyası oluşturursunuz ve tablete yükleyebilirsiniz.

### Gereksinimler

**Windows için:**
- WSL2 (Windows Subsystem for Linux) kurulu olmalı
- Veya Linux sanal makine (VirtualBox/VMware)

**Linux/Mac için:**
- Doğrudan kullanılabilir

### Adım Adım Kurulum

#### 1. Linux Ortamı Hazırlama (Windows için WSL2)

Windows kullanıyorsanız:
```powershell
# PowerShell'de (Yönetici olarak):
wsl --install
# Bilgisayarı yeniden başlatın
```

#### 2. Buildozer ve Gerekli Araçları Kurma

Linux terminalinde (WSL2 veya Linux):
```bash
# Sistem güncellemesi
sudo apt update
sudo apt upgrade -y

# Gerekli paketler
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# Buildozer kurulumu
pip3 install --user --upgrade buildozer
pip3 install --user --upgrade Cython

# PATH'e ekleme (her terminal açılışında)
echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
```

#### 3. Proje Klasörüne Gitme

```bash
cd "/mnt/d/python310/Projeler/Stok Takip"
# veya projenizin bulunduğu klasöre gidin
```

#### 4. APK Oluşturma

```bash
# İlk kez çalıştırma (uzun sürebilir, ~30-60 dakika)
buildozer android debug

# Sonraki çalıştırmalarda daha hızlı olacak
```

APK dosyası `bin/` klasöründe oluşturulacak: `bin/stoktakip-0.1-arm64-v8a-debug.apk`

#### 5. Tablete Yükleme

1. APK dosyasını tablete aktarın (USB, email, cloud storage vb.)
2. Tablette "Bilinmeyen kaynaklardan uygulama yükleme" iznini açın:
   - Ayarlar > Güvenlik > Bilinmeyen kaynaklar
3. APK dosyasına tıklayıp yükleyin

---

## Yöntem 2: Pydroid 3 ile Çalıştırma (Kolay - Hızlı Test)

Bu yöntem daha kolay ama daha az profesyonel. Uygulama bir Python runtime içinde çalışır.

### Adımlar

1. **Pydroid 3'ü tablete yükleyin:**
   - Google Play Store'dan "Pydroid 3" uygulamasını indirin ve kurun

2. **Gerekli paketleri yükleyin:**
   - Pydroid 3'ü açın
   - Menüden "Pip" sekmesine gidin
   - "kivy" yazıp yükleyin

3. **Proje dosyalarını tablete aktarın:**
   - `main.py` ve `database.py` dosyalarını tablete kopyalayın
   - USB, email veya cloud storage kullanabilirsiniz

4. **Uygulamayı çalıştırın:**
   - Pydroid 3'te `main.py` dosyasını açın
   - "Run" butonuna basın

### Dezavantajlar
- Pydroid 3 uygulaması açık kalmalı
- Bağımsız bir APK değil
- Daha yavaş çalışabilir

---

## Yöntem 3: Python-for-Android (Gelişmiş)

Daha fazla kontrol istiyorsanız python-for-android kullanabilirsiniz, ancak bu daha karmaşıktır.

---

## Sorun Giderme

### Buildozer hataları:
- `buildozer android clean` komutu ile temizleyip tekrar deneyin
- İnternet bağlantınızın iyi olduğundan emin olun (ilk kurulumda çok veri indirir)

### APK çok büyük:
- `buildozer.spec` dosyasında gereksiz paketleri kaldırın
- `android.archs = arm64-v8a` yaparak sadece 64-bit destekleyin

### Tablette açılmıyor:
- Android sürümünüz 5.0 (API 21) veya üzeri olmalı
- `buildozer.spec` dosyasında `p4a.minimum_sdk_version = 21` kontrol edin

---

## Öneri

**İlk test için:** Pydroid 3 yöntemini kullanın (hızlı)
**Kalıcı kullanım için:** Buildozer ile APK oluşturun (profesyonel)
