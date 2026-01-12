# BIOS Virtualization Etkinleştirme

WSL2 çalışması için BIOS'ta Virtualization özelliğinin açık olması gerekiyor.

## Adımlar

1. **Bilgisayarı yeniden başlatın**

2. **BIOS'a girin:**
   - Bilgisayar açılırken şu tuşlardan birine basın:
     - **F2** (en yaygın)
     - **F10**
     - **Del**
     - **F12**
     - **Esc**
   - Markaya göre değişir (Dell, HP, Lenovo, vs.)

3. **Virtualization özelliğini bulun:**
   - **Advanced** veya **System Configuration** menüsüne gidin
   - Şu isimlerden birini arayın:
     - **Virtualization Technology (VT-x)**
     - **AMD-V**
     - **Intel Virtualization Technology**
     - **SVM Mode** (AMD için)
     - **Virtualization**

4. **Etkinleştirin:**
   - **Enabled** yapın
   - **Disabled** ise **Enabled**'a değiştirin

5. **Kaydedin ve çıkın:**
   - **F10** (Save & Exit)
   - Veya **Save Changes and Exit**

6. **Bilgisayar normal şekilde açılacak**

## Alternatif: Windows Özelliklerinden Kontrol

Eğer BIOS'a giremiyorsanız, önce Windows Özelliklerinden kontrol edin:

1. Windows tuşu + R
2. `optionalfeatures` yazın
3. **Virtual Machine Platform** işaretli mi kontrol edin
4. İşaretli değilse işaretleyin ve yeniden başlatın

## Kontrol

BIOS'ta değişiklik yaptıktan sonra:

```powershell
wsl --status
```

"Varsayılan Sürüm: 2" yazıyorsa hazırsınız.
