# APK Oluşturma Rehberi

Stok Takip uygulamanızı Android APK'ya dönüştürmek için adım adım talimatlar:

## Gereksinimler

**Windows için:**
- WSL2 (Windows Subsystem for Linux) kurulu olmalı
- En az 10 GB boş disk alanı
- İyi internet bağlantısı (ilk kurulumda çok veri indirir)

**Linux/Mac için:**
- Doğrudan kullanılabilir

## Adım 1: WSL2 Kurulumu (Windows için)

PowerShell'i **Yönetici olarak** açın ve şu komutu çalıştırın:

```powershell
wsl --install
```

Bilgisayarı yeniden başlatın. WSL2 kurulumu tamamlandıktan sonra Ubuntu terminali açılacak.

## Adım 2: Buildozer Kurulumu

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

# PATH'e ekleme
echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc

# Buildozer'ın çalıştığını kontrol et
buildozer --version
```

## Adım 3: Proje Dosyalarını WSL'ye Kopyalama

Windows dosyalarına WSL'den erişim:

```bash
# Windows D: sürücüsüne erişim
cd /mnt/d/python310/Projeler/Stok\ Takip

# Veya projeyi WSL home dizinine kopyalayın
cp -r /mnt/d/python310/Projeler/Stok\ Takip ~/stok-takip
cd ~/stok-takip
```

## Adım 4: APK Oluşturma

```bash
# İlk kez çalıştırma (30-60 dakika sürebilir)
# Buildozer tüm Android SDK, NDK ve araçları indirecek
buildozer android debug

# Başarılı olursa APK dosyası şu konumda olacak:
# bin/stoktakip-0.1-arm64-v8a-debug.apk
# veya
# bin/stoktakip-0.1-armeabi-v7a-debug.apk
```

## Adım 5: APK'yı Tablete Yükleme

1. **APK dosyasını tablete aktarın:**
   - USB ile kopyalayın
   - Email ile gönderin
   - Cloud storage (Google Drive, Dropbox) kullanın
   - WiFi üzerinden paylaşın

2. **Tablette bilinmeyen kaynaklardan yükleme iznini açın:**
   - Ayarlar > Güvenlik > Bilinmeyen kaynaklardan uygulama yükleme
   - Veya Ayarlar > Uygulamalar > Özel erişim > Bilinmeyen uygulamaları yükle

3. **APK dosyasına tıklayın ve yükleyin**

## Sorun Giderme

### Buildozer hataları:
```bash
# Temizle ve tekrar dene
buildozer android clean
buildozer android debug
```

### Disk alanı yetersiz:
```bash
# Buildozer cache'i temizle
rm -rf ~/.buildozer
```

### İnternet bağlantısı sorunları:
- İlk kurulumda çok veri indirir (2-3 GB)
- Sabırlı olun, tekrar deneyin

### APK çok büyük:
`buildozer.spec` dosyasında sadece bir mimari kullanın:
```
android.archs = arm64-v8a
```

## Release APK (Dağıtım için)

Dağıtım için release APK oluşturmak:

```bash
buildozer android release
```

Bu komut bir keystore dosyası isteyecek. İlk kez için:

```bash
keytool -genkey -v -keystore stoktakip.keystore -alias stoktakip -keyalg RSA -keysize 2048 -validity 10000
```

## Hızlı Test (Alternatif)

Eğer Buildozer kurulumu çok uzun sürüyorsa, önce Pydroid 3 ile test edebilirsiniz (ANDROID_KURULUM.md dosyasına bakın).

---

**Not:** İlk APK oluşturma işlemi 30-60 dakika sürebilir çünkü tüm Android geliştirme araçlarını indirir. Sonraki çalıştırmalarda çok daha hızlı olacaktır.
