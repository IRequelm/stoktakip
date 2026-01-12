@echo off
echo ==========================================
echo Hyper-V Servisleri Kontrolu
echo ==========================================
echo.

echo Hyper-V servislerini kontrol ediliyor...
sc query vmcompute
echo.
sc query vmms
echo.

echo ==========================================
echo Eger servisler durdurulmussa:
echo.
echo PowerShell'i Yonetici olarak acin ve:
echo bcdedit /set hypervisorlaunchtype auto
echo.
echo Sonra bilgisayari yeniden baslatin
echo ==========================================
pause
