@echo off
echo ==========================================
echo BIOS/UEFI'ye Girmek Icin
echo ==========================================
echo.
echo Bu script bilgisayari Advanced Startup Options
echo ile yeniden baslatacak.
echo.
echo BIOS'a girmek icin:
echo 1. Sorun Gider
echo 2. Gelişmiş seçenekler
echo 3. UEFI Üretici Yazılımı Ayarları
echo 4. Yeniden başlat
echo.
echo Devam etmek icin Enter'a basin...
pause

shutdown /r /o /f /t 00
