@echo off
echo ==========================================
echo Hyper-V Servisleri Kontrolu
echo ==========================================
echo.

echo vmcompute servisi:
sc query vmcompute
echo.
echo vmms servisi:
sc query vmms
echo.

echo ==========================================
echo Eger servisler durdurulmussa:
echo.
echo PowerShell'i Yonetici olarak acin:
echo.
echo net start vmcompute
echo net start vmms
echo.
echo VEYA:
echo.
echo sc config vmcompute start= auto
echo sc config vmms start= auto
echo net start vmcompute
echo net start vmms
echo ==========================================
pause
