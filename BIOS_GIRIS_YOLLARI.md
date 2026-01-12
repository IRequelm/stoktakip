# BIOS/UEFI'ye Giriş Yolları

## Yöntem 1: Windows Ayarlarından (En Kolay)

1. **Windows tuşu + I** ile Ayarlar'ı açın
2. **Güncelleme ve Güvenlik** (Windows 10) veya **Sistem** → **Kurtarma** (Windows 11)
3. **Gelişmiş başlangıç** bölümünde **Şimdi yeniden başlat**'a tıklayın
4. Bilgisayar yeniden başladığında:
   - **Sorun Gider** seçin
   - **Gelişmiş seçenekler**
   - **UEFI Üretici Yazılımı Ayarları**
   - **Yeniden başlat**

Bu sizi direkt BIOS/UEFI'ye götürür!

## Yöntem 2: Shift + Yeniden Başlat

1. **Başlat menüsüne** tıklayın
2. **Güç** butonuna tıklayın
3. **Shift tuşuna basılı tutarak** **Yeniden başlat**'a tıklayın
4. Aynı menü açılacak (Yöntem 1'deki adımları takip edin)

## Yöntem 3: Komut Satırından

PowerShell'i **Yönetici olarak** açın:

```powershell
shutdown /r /o /f /t 00
```

Bu komut bilgisayarı Advanced Startup Options ile yeniden başlatır.

## Yöntem 4: Farklı Tuş Kombinasyonları

Bilgisayar açılırken şu tuşları deneyin:

- **F2** (en yaygın)
- **F10**
- **Del** (Delete)
- **F12**
- **Esc**
- **F1**
- **F8**

**Önemli:** Bilgisayar açılırken sürekli basılı tutun, bir kez değil!

## Yöntem 5: Markaya Özel Tuşlar

- **Dell:** F2 veya F12
- **HP:** F10 veya Esc
- **Lenovo:** F1 veya F2
- **ASUS:** F2 veya Del
- **Acer:** F2 veya Del
- **MSI:** Del
- **Samsung:** F2

## BIOS'ta Virtualization Bulma

BIOS'a girdikten sonra:

1. **Advanced** veya **System Configuration** menüsüne gidin
2. Şunlardan birini arayın:
   - **Virtualization Technology (VT-x)**
   - **Intel Virtualization Technology**
   - **AMD-V**
   - **SVM Mode**
   - **Virtualization**

3. **Enabled** yapın
4. **F10** ile kaydedin ve çıkın

## Önemli Notlar

- Bazı bilgisayarlarda hızlı başlatma açıksa tuşlara basma süresi çok kısa olabilir
- Windows'tan giriş (Yöntem 1) en garantili yoldur
- BIOS'a girmek için bilgisayarın tamamen kapatılıp açılması gerekebilir
