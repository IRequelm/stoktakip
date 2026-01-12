@echo off
echo ==========================================
echo Hyper-V Servislerini Etkinlestirme
echo ==========================================
echo.
echo Bu script YONETICI IZINLERI gerektirir!
echo.
echo PowerShell'i Yonetici olarak acip su komutlari calistirin:
echo.
echo # Servisleri otomatik baslatma icin ayarla
echo sc config vmcompute start= auto
echo sc config vmms start= auto
echo.
echo # Servisleri baslat
echo net start vmcompute
echo net start vmms
echo.
echo # Kontrol et
echo sc query vmcompute
echo sc query vmms
echo.
echo Sonra Ubuntu'yu tekrar kurmayi deneyin:
echo wsl --install -d Ubuntu
echo.
pause
