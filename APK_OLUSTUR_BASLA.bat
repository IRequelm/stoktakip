@echo off
echo ==========================================
echo Stok Takip APK Olusturma Baslatiliyor...
echo ==========================================
echo.
echo Ubuntu kurulumu tamamlandiysa devam edin.
echo.
pause

wsl bash -c "cd /mnt/d/python310/Projeler/Stok\ Takip && bash apk_hazirlik.sh"

echo.
echo ==========================================
echo Hazirlik tamamlandi!
echo APK olusturmak icin devam edin...
echo ==========================================
pause

wsl bash -c "cd /mnt/d/python310/Projeler/Stok\ Takip && buildozer android debug"

echo.
echo ==========================================
echo APK olusturma tamamlandi!
echo APK dosyasi: bin/stoktakip-*.apk
echo ==========================================
pause
