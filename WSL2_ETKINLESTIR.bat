@echo off
echo ==========================================
echo WSL2 Etkinlestirme
echo ==========================================
echo.
echo Bu script YONETICI IZINLERI gerektirir!
echo.
echo PowerShell'i Yonetici olarak acip su komutlari calistirin:
echo.
echo dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
echo dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
echo shutdown /r /t 0
echo.
echo VEYA Windows Ozellikleri'nden manuel olarak:
echo - Windows tusu + R
echo - optionalfeatures yazin
echo - Windows Subsystem for Linux isaretleyin
echo - Virtual Machine Platform isaretleyin
echo - Tamam ve yeniden baslat
echo.
pause
