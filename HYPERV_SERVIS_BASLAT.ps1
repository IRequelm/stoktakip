# Hyper-V Servislerini Başlatma Scripti
# PowerShell'i Yönetici olarak çalıştırın

Write-Host "=========================================="
Write-Host "Hyper-V Servislerini Etkinleştirme"
Write-Host "=========================================="
Write-Host ""

# Servisleri otomatik başlatma için ayarla
Write-Host "Servisler otomatik başlatma için ayarlanıyor..."
& sc.exe config vmcompute start= auto
& sc.exe config vmms start= auto
Write-Host ""

# Servisleri başlat
Write-Host "Servisler başlatılıyor..."
try {
    Start-Service vmcompute -ErrorAction Stop
    Write-Host "✓ vmcompute servisi başlatıldı"
} catch {
    Write-Host "✗ vmcompute servisi başlatılamadı: $_"
}

try {
    Start-Service vmms -ErrorAction Stop
    Write-Host "✓ vmms servisi başlatıldı"
} catch {
    Write-Host "✗ vmms servisi başlatılamadı: $_"
}
Write-Host ""

# Servis durumlarını kontrol et
Write-Host "Servis durumları:"
Write-Host ""
Get-Service vmcompute, vmms | Format-Table -AutoSize
Write-Host ""

Write-Host "=========================================="
Write-Host "Tamamlandı!"
Write-Host "Şimdi Ubuntu'yu kurmayı deneyin:"
Write-Host "wsl --install -d Ubuntu"
Write-Host "=========================================="
