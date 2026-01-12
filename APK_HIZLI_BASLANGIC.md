# APK Oluşturma - Hızlı Başlangıç

## Windows'ta APK Oluşturma

### 1. WSL2 Kurulumu (İlk Kez)

PowerShell'i **Yönetici olarak** açın:

```powershell
wsl --install
```

Bilgisayarı yeniden başlatın.

### 2. Ubuntu Terminalinde Komutlar

Ubuntu terminalini açın ve şu komutları çalıştırın:

```bash
# Sistem güncellemesi
sudo apt update && sudo apt upgrade -y

# Gerekli paketler
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# Buildozer kurulumu
pip3 install --user --upgrade buildozer Cython

# PATH'e ekle
echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
```

### 3. Projeye Git

```bash
cd /mnt/d/python310/Projeler/Stok\ Takip
```

### 4. APK Oluştur

```bash
buildozer android debug
```

**İlk çalıştırma 30-60 dakika sürebilir!** Buildozer tüm Android araçlarını indirecek.

### 5. APK'yı Bul

APK dosyası şu konumda olacak:
```
bin/stoktakip-0.1-arm64-v8a-debug.apk
```

Bu dosyayı tablete kopyalayıp yükleyin.

---

## Sorun Giderme

**Buildozer bulunamadı hatası:**
```bash
export PATH=$PATH:~/.local/bin
buildozer --version
```

**Temiz başlangıç:**
```bash
buildozer android clean
buildozer android debug
```

**Disk alanı:**
En az 10 GB boş alan gerekli.

---

## Alternatif: Hazır Script

```bash
chmod +x apk_olustur.sh
./apk_olustur.sh
```

---

Detaylı bilgi için `APK_OLUSTURMA.md` dosyasına bakın.
