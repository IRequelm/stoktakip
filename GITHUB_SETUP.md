# GitHub'a Yükleme ve APK Oluşturma

## Adımlar

1. **GitHub'da yeni repository oluşturun:**
   - GitHub.com'a gidin
   - "New repository" tıklayın
   - Repository adı: `stok-takip` (veya istediğiniz isim)
   - Public veya Private seçin
   - "Create repository" tıklayın

2. **Projeyi GitHub'a yükleyin:**

```bash
# Git yapılandırması (ilk kez)
git config --global user.name "Adınız"
git config --global user.email "email@example.com"

# Dosyaları ekle
git add .

# Commit yap
git commit -m "İlk commit - Stok Takip uygulaması"

# GitHub repository URL'inizi ekleyin (örnek)
git remote add origin https://github.com/KULLANICI_ADI/stok-takip.git

# Push yap
git branch -M main
git push -u origin main
```

3. **GitHub Actions'ı tetikleyin:**
   - GitHub repository sayfanıza gidin
   - "Actions" sekmesine tıklayın
   - "Build Android APK" workflow'unu seçin
   - "Run workflow" butonuna tıklayın
   - Workflow çalışmaya başlayacak (30-60 dakika sürebilir)

4. **APK'yı indirin:**
   - Workflow tamamlandığında "apk" artifact'ını indirin
   - APK dosyasını tablete yükleyin

## Otomatik Build

Her push'ta otomatik olarak APK oluşturulur. Manuel olarak da "Actions" sekmesinden tetikleyebilirsiniz.
