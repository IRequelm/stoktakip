# BIOS'a Giriş - Kablosuz Klavye Sorunu

## Çözüm 1: USB Kablolu Klavye Kullan (En Kolay)

1. Bir USB kablolu klavye bulun (geçici olarak)
2. USB kablolu klavyeyi takın
3. Bilgisayarı yeniden başlatın
4. Açılışta F2'ye basın (USB klavye çalışacak)

## Çözüm 2: Windows'tan BIOS'a Giriş (Alternatif)

Bazı bilgisayarlarda Windows'tan direkt BIOS'a girebilirsiniz:

### PowerShell ile (Yönetici):

```powershell
# UEFI firmware ayarlarına git
shutdown /r /fw /t 0
```

Bu komut bilgisayarı UEFI/BIOS ayarlarına götürür (eğer UEFI destekliyorsa).

## Çözüm 3: Alternatif - WSL2 Olmadan APK Oluşturma

BIOS'a giremiyorsanız, alternatif yöntemler:

### Seçenek A: Online Build Servisi
- GitHub Actions
- GitLab CI/CD
- Cloud build servisleri

### Seçenek B: Linux Sanal Makine (VirtualBox)
- VirtualBox kurun
- Linux ISO indirin
- Sanal makinede APK oluşturun
- BIOS'a girmeye gerek yok

### Seçenek C: Başka Bir Bilgisayar
- Linux veya Mac bilgisayarda APK oluşturun
- Dosyaları paylaşın

### Seçenek D: Pydroid 3 (Hızlı Test)
- APK değil ama uygulamayı çalıştırabilirsiniz
- Tablete Pydroid 3 kurun
- Python dosyalarını çalıştırın

## Çözüm 4: BIOS Ayarlarını Değiştirme (Eğer Erişim Varsa)

Eğer bir şekilde BIOS'a girebilirseniz:
- **USB Legacy Support** veya **USB Keyboard Support**'u **Enabled** yapın
- Böylece kablosuz klavye de çalışabilir
