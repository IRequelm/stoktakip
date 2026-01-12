#!/bin/bash
# APK Oluşturma Hazırlık Scripti

echo "=========================================="
echo "Stok Takip APK Hazırlık Kontrolü"
echo "=========================================="

# Proje dizinine git
cd /mnt/d/python310/Projeler/Stok\ Takip || exit 1

echo "✓ Proje dizinine geçildi"

# Gerekli paketleri kontrol et ve kur
echo "Gerekli paketler kontrol ediliyor..."

# Sistem güncellemesi
sudo apt update -qq

# Gerekli paketler
REQUIRED_PACKAGES="git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev"

for package in $REQUIRED_PACKAGES; do
    if ! dpkg -l | grep -q "^ii  $package "; then
        echo "Kuruluyor: $package"
        sudo apt install -y $package > /dev/null 2>&1
    else
        echo "✓ $package zaten kurulu"
    fi
done

# Buildozer kontrolü
if ! command -v buildozer &> /dev/null; then
    echo "Buildozer kuruluyor..."
    pip3 install --user --upgrade buildozer Cython > /dev/null 2>&1
    export PATH=$PATH:~/.local/bin
    echo "✓ Buildozer kuruldu"
else
    echo "✓ Buildozer zaten kurulu"
fi

# Buildozer versiyonunu göster
buildozer --version

echo "=========================================="
echo "Hazırlık tamamlandı!"
echo "APK oluşturmak için: buildozer android debug"
echo "=========================================="
