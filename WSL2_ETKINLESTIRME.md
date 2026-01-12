# WSL2 Etkinleştirme Adımları

## Hata: Virtual Machine Platform gerekli

WSL2'yi kullanmak için Windows özelliklerini etkinleştirmeniz gerekiyor.

## Yöntem 1: PowerShell ile (Önerilen)

1. **PowerShell'i Yönetici olarak açın:**
   - Windows tuşuna basın
   - "PowerShell" yazın
   - Sağ tıklayın → "Yönetici olarak çalıştır"

2. **Şu komutları sırayla çalıştırın:**

```powershell
# WSL özelliğini etkinleştir
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# Virtual Machine Platform'u etkinleştir
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Bilgisayarı yeniden başlatın
shutdown /r /t 0
```

## Yöntem 2: Windows Özellikleri ile

1. **Windows Özelliklerini açın:**
   - Windows tuşu + R
   - `optionalfeatures` yazın ve Enter'a basın

2. **Şu özellikleri işaretleyin:**
   - ☑ Windows Subsystem for Linux
   - ☑ Virtual Machine Platform

3. **Tamam'a tıklayın ve bilgisayarı yeniden başlatın**

## Yöntem 3: BIOS'ta Virtualization

Eğer hala çalışmazsa, BIOS'ta Virtualization (VT-x/AMD-V) etkin olmalı:

1. Bilgisayarı yeniden başlatın
2. BIOS'a girin (genellikle F2, F10, Del tuşu)
3. Virtualization veya VT-x/AMD-V özelliğini bulun
4. **Enabled** yapın
5. Kaydedin ve çıkın

## Yeniden Başlattıktan Sonra

1. Ubuntu terminalini tekrar açın
2. Kurulum devam edecek
3. Kullanıcı adı ve şifre oluşturun
4. APK oluşturma işlemine geçin

---

**Not:** Yeniden başlatma zorunludur!
