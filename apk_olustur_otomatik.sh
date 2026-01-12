#!/bin/bash
# Otomatik APK Oluşturma Scripti

set -e  # Hata durumunda dur

echo "=========================================="
echo "Stok Takip APK Oluşturma Başlatılıyor..."
echo "=========================================="
echo ""

# Proje dizinine git
PROJECT_DIR="/mnt/d/python310/Projeler/Stok Takip"
cd "$PROJECT_DIR" || {
    echo "HATA: Proje dizinine geçilemedi: $PROJECT_DIR"
    exit 1
}

echo "✓ Proje dizini: $(pwd)"
echo ""

# Sistem güncellemesi
echo "Sistem güncelleniyor..."
sudo apt update -qq
echo "✓ Sistem güncellendi"
echo ""

# Gerekli paketleri kur
echo "Gerekli paketler kontrol ediliyor..."
REQUIRED_PACKAGES="git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev"

MISSING_PACKAGES=""
for package in $REQUIRED_PACKAGES; do
    if ! dpkg -l | grep -q "^ii  $package "; then
        MISSING_PACKAGES="$MISSING_PACKAGES $package"
    fi
done

if [ -n "$MISSING_PACKAGES" ]; then
    echo "Eksik paketler kuruluyor: $MISSING_PACKAGES"
    sudo apt install -y $MISSING_PACKAGES
    echo "✓ Paketler kuruldu"
else
    echo "✓ Tüm paketler zaten kurulu"
fi
echo ""

# Buildozer kontrolü ve kurulumu
if ! command -v buildozer &> /dev/null; then
    echo "Buildozer kuruluyor..."
    pip3 install --user --upgrade buildozer Cython
    export PATH=$PATH:~/.local/bin
    echo "✓ Buildozer kuruldu"
else
    echo "✓ Buildozer zaten kurulu: $(buildozer --version)"
fi
echo ""

# Buildozer PATH kontrolü
if ! command -v buildozer &> /dev/null; then
    export PATH=$PATH:~/.local/bin
    if ! command -v buildozer &> /dev/null; then
        echo "HATA: Buildozer bulunamadı!"
        exit 1
    fi
fi

echo "=========================================="
echo "APK oluşturuluyor..."
echo "Bu işlem 30-60 dakika sürebilir!"
echo "Lütfen bekleyin..."
echo "=========================================="
echo ""

# APK oluştur
buildozer android debug

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✓ APK başarıyla oluşturuldu!"
    echo "=========================================="
    echo ""
    echo "APK dosyası:"
    ls -lh bin/*.apk 2>/dev/null || echo "bin/ klasöründe APK dosyası bulunamadı"
    echo ""
    echo "Tablete yüklemek için bu dosyayı kopyalayın."
else
    echo ""
    echo "=========================================="
    echo "✗ Hata oluştu!"
    echo "=========================================="
    echo "Hata mesajlarını kontrol edin."
    exit 1
fi
