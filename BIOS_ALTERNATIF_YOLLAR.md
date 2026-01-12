# BIOS'a Giriş - Alternatif Yöntemler

## Yöntem 1: Bilgisayarı Tamamen Kapat

1. **Bilgisayarı tamamen kapatın** (Uyku modu değil, tamamen kapatın)
2. **Açma butonuna basın**
3. **Hemen ardından sürekli F2 tuşuna basın** (veya F10, Del, F12)
4. BIOS ekranı açılana kadar basılı tutun

## Yöntem 2: Hızlı Başlatmayı Kapat

Hızlı başlatma açıksa tuşlara basma süresi çok kısa olur:

1. **Denetim Masası** → **Güç Seçenekleri**
2. **Güç düğmesinin yaptığı işi seçin**
3. **Şu anda kullanılmayan ayarları değiştir**
4. **Hızlı başlatmayı aç (önerilen)** seçeneğini **KAPATIN**
5. **Değişiklikleri kaydet**
6. Bilgisayarı yeniden başlatın ve F2'ye basın

## Yöntem 3: Sistem Bilgisi ile Marka Öğrenme

Hangi marka bilgisayar kullanıyorsunuz?

PowerShell'de şunu çalıştırın:
```powershell
Get-ComputerInfo | Select-Object CsManufacturer, CsModel
```

Markaya göre tuş:
- **Dell:** F2 (açılışta sürekli bas)
- **HP:** F10 veya Esc
- **Lenovo:** F1 veya F2
- **ASUS:** F2 veya Del
- **Acer:** F2 veya Del

## Yöntem 4: Windows Recovery Environment (WinRE)

1. **Windows tuşu + X**
2. **Ayarlar**
3. **Güncelleme ve Güvenlik** → **Kurtarma**
4. **Gelişmiş başlangıç** → **Şimdi yeniden başlat**
5. **Sorun Gider** → **Gelişmiş seçenekler**
6. **Komut İstemi**'ni seçin
7. Şu komutu yazın:
   ```
   bcdedit /set {default} bootmenupolicy legacy
   ```
8. Bilgisayarı yeniden başlatın
9. Artık F8 ile Advanced Boot Options açılabilir

## Yöntem 5: Grub Bootloader (Eğer Linux kuruluysa)

Eğer daha önce Linux kurduysanız, Grub menüsünden BIOS'a girebilirsiniz.

## Yöntem 6: Bilgisayar Markasına Özel

Bazı markaların özel yöntemleri var:

**HP:**
- Bilgisayar açılırken **Esc** tuşuna basın
- **F10** (BIOS Setup) seçeneğini seçin

**Dell:**
- Açılışta **F12** (Boot Menu)
- Veya **F2** (BIOS Setup)

**Lenovo:**
- Açılışta **F1** veya **F2**
- Veya **Novo** butonu (yan tarafta küçük buton)

## Önemli İpucu

Eğer hiçbiri işe yaramazsa:
- Bilgisayarı **tamamen kapatın**
- **Güç kablosunu çıkarın** (dizüstüyse bataryayı çıkarın)
- **30 saniye bekleyin**
- **Tekrar takın ve açın**
- **Açılır açılmaz sürekli F2'ye basın**
