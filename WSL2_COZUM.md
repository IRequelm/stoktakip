# WSL2 Sorun Çözümü

## Hata: HCS_E_HYPERV_NOT_INSTALLED

Bu hata Hyper-V servislerinin çalışmadığını gösterir.

## Çözüm 1: Hyper-V Servislerini Etkinleştir

PowerShell'i **Yönetici olarak** açın ve şu komutları çalıştırın:

```powershell
# Hyper-V'yi etkinleştir
bcdedit /set hypervisorlaunchtype auto

# Bilgisayarı yeniden başlatın
shutdown /r /t 0
```

## Çözüm 2: BIOS'ta Virtualization Kontrolü

1. Bilgisayarı yeniden başlatın
2. BIOS'a girin (F2, F10, Del)
3. **Virtualization Technology (VT-x)** veya **AMD-V** özelliğini bulun
4. **Enabled** yapın
5. Kaydedin ve çıkın

## Çözüm 3: Windows Özelliklerinden Hyper-V

1. Windows tuşu + R
2. `optionalfeatures` yazın
3. **Hyper-V** işaretleyin (varsa)
4. Yeniden başlatın

## Çözüm 4: Alternatif - WSL1 Kullan

Eğer WSL2 çalışmıyorsa, geçici olarak WSL1 kullanabilirsiniz:

```powershell
wsl --set-default-version 1
wsl --install -d Ubuntu
```

Ancak WSL1'de Buildozer çalışmayabilir, bu yüzden WSL2'yi çalıştırmak daha iyi.

## Kontrol

Yeniden başlattıktan sonra:

```powershell
wsl --status
```

"Varsayılan Sürüm: 2" görünmeli.
