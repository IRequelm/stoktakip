#!/bin/bash
# APK Oluşturma Scripti
# Bu scripti Linux/WSL2 ortamında çalıştırın

echo "=========================================="
echo "Stok Takip APK Oluşturma Başlatılıyor..."
echo "=========================================="

# Buildozer'ın kurulu olup olmadığını kontrol et
if ! command -v buildozer &> /dev/null
then
    echo "Buildozer bulunamadı. Kurulum yapılıyor..."
    pip3 install --user --upgrade buildozer
    pip3 install --user --upgrade Cython
    export PATH=$PATH:~/.local/bin
fi

# Temizleme (opsiyonel - ilk çalıştırmada gerekli değil)
# buildozer android clean

echo "APK oluşturuluyor... Bu işlem 30-60 dakika sürebilir."
echo "Lütfen bekleyin..."

# APK oluştur
buildozer android debug

if [ $? -eq 0 ]; then
    echo "=========================================="
    echo "✓ APK başarıyla oluşturuldu!"
    echo "=========================================="
    echo "APK dosyası: bin/stoktakip-*.apk"
    echo "Tablete yüklemek için bu dosyayı kopyalayın."
else
    echo "=========================================="
    echo "✗ Hata oluştu!"
    echo "=========================================="
    echo "Hata mesajlarını kontrol edin."
fi
