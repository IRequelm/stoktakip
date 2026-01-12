@echo off
echo ==========================================
echo Hizli Baslatmayi Kapatma
echo ==========================================
echo.
echo Bu script Hizli Baslatmayi kapatacak.
echo Boylece BIOS'a girmek daha kolay olacak.
echo.
echo Devam etmek icin Enter'a basin...
pause

powercfg /hibernate off

echo.
echo Hizli baslatma kapatildi!
echo.
echo Simdi bilgisayari TAMAMEN KAPATIN
echo (Uyku modu degil, tamamen kapat)
echo.
echo Sonra acarken F2 tusuna surekli basin.
echo.
pause
