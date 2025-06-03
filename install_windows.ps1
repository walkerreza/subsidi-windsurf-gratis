# Windows Installer untuk Subsidi Windsurf
# Dibuat oleh Reza Walker

# Banner
Write-Host "`n" -NoNewLine
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "    SUBSIDI WINDSURF INSTALLER (WINDOWS)    " -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "`n"

# Buat direktori penyimpanan
$subsidiDir = "$env:USERPROFILE\Documents\subsidi-windsurf"
Write-Host "[+] Membuat direktori: $subsidiDir" -ForegroundColor Yellow

try {
    if (-not (Test-Path -Path $subsidiDir)) {
        New-Item -Path $subsidiDir -ItemType Directory -ErrorAction Stop | Out-Null
        Write-Host "    Direktori berhasil dibuat!" -ForegroundColor Green
    } else {
        Write-Host "    Direktori sudah ada!" -ForegroundColor Green
    }
    Set-Location -Path $subsidiDir -ErrorAction Stop
}
catch {
    Write-Host "`n[!] Gagal membuat direktori $subsidiDir. Mencoba direktori Downloads..." -ForegroundColor Red
    $subsidiDir = "$env:USERPROFILE\Downloads\subsidi-windsurf"
    
    try {
        if (-not (Test-Path -Path $subsidiDir)) {
            New-Item -Path $subsidiDir -ItemType Directory -ErrorAction Stop | Out-Null
        }
        Set-Location -Path $subsidiDir -ErrorAction Stop
        Write-Host "    Menggunakan direktori alternatif: $subsidiDir" -ForegroundColor Yellow
    }
    catch {
        Write-Host "`n[!] ERROR: Tidak bisa membuat direktori. Menggunakan direktori saat ini." -ForegroundColor Red
        $subsidiDir = (Get-Location).Path
    }
}

# Download semua file
Write-Host "`n[+] Menyimpan file ke direktori: $subsidiDir" -ForegroundColor Yellow
Write-Host "`n"

$files = @{
    "ubuntu_reset.py" = "https://raw.githubusercontent.com/walkerreza/subsidi-windsurf-gratis/main/ubuntu_reset.py"
    "requirement.py" = "https://raw.githubusercontent.com/walkerreza/subsidi-windsurf-gratis/main/requirement.py"
    "menu.py" = "https://raw.githubusercontent.com/walkerreza/subsidi-windsurf-gratis/main/menu.py"
    "setup.py" = "https://raw.githubusercontent.com/walkerreza/subsidi-windsurf-gratis/main/setup.py"
    "installer.sh" = "https://raw.githubusercontent.com/walkerreza/subsidi-windsurf-gratis/main/installer.sh"
}

$missingFiles = @()

foreach ($file in $files.Keys) {
    Write-Host "[+] Downloading $file..." -ForegroundColor Yellow
    try {
        Invoke-WebRequest -Uri $files[$file] -OutFile "$subsidiDir\$file" -ErrorAction Stop
    }
    catch {
        Write-Host "    Gagal download $file : $($_.Exception.Message)" -ForegroundColor Red
        $missingFiles += $file
    }
}

# Verifikasi file yang didownload
Write-Host "`n[+] Memverifikasi file yang didownload..." -ForegroundColor Yellow

if ($missingFiles.Count -eq 0) {
    Write-Host "`n✅ Download berhasil! Semua file telah tersimpan di: ${subsidiDir}" -ForegroundColor Green
    Get-ChildItem -Path $subsidiDir
}
else {
    Write-Host "`n⚠️ Beberapa file tidak berhasil didownload:" -ForegroundColor Red
    foreach ($file in $missingFiles) {
        Write-Host "    - $file" -ForegroundColor Red
    }
    Write-Host "`nFile yang ada di direktori ${subsidiDir}:" -ForegroundColor Yellow
    Get-ChildItem -Path $subsidiDir
}

# Cek instalasi Python
Write-Host "`n[+] Memeriksa instalasi Python di Windows..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version
    Write-Host "    $pythonVersion terdeteksi!" -ForegroundColor Green
    $pythonInstalled = $true
}
catch {
    Write-Host "    Python tidak terinstall di Windows." -ForegroundColor Red
    $pythonInstalled = $false
}

# Informasi tambahan
Write-Host "`n============================================" -ForegroundColor Cyan
Write-Host "         INSTRUKSI PENGGUNAAN              " -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "`nScript ini hanya untuk download file. Untuk menggunakan tools:" -ForegroundColor White

if ($pythonInstalled) {
    Write-Host "`n1. File sudah siap digunakan di Windows dengan Python"
    Write-Host "   Namun beberapa fitur khusus Ubuntu tidak akan berfungsi di Windows."
    Write-Host "`n2. Untuk menjalankan menu utama di Windows, ketik:"
    Write-Host "   python menu.py" -ForegroundColor Green
    Write-Host "`n3. Untuk hasil terbaik, pindahkan file-file ini ke Ubuntu"
}
else {
    Write-Host "`n1. Python tidak terdeteksi di Windows kamu."
    Write-Host "   Download Python dari: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "`n2. Setelah install Python, kamu bisa jalankan menu dengan:"
    Write-Host "   python menu.py" -ForegroundColor Yellow
    Write-Host "`n3. Untuk hasil terbaik, pindahkan file-file ini ke Ubuntu"
}

Write-Host "`n============================================" -ForegroundColor Cyan
Write-Host "       HATI-HATI! PENGINGAT PENTING        " -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "`nBeberapa script ini dirancang untuk Ubuntu/Linux dan TIDAK AKAN BERFUNGSI"
Write-Host "dengan sempurna di Windows. Script reset device ID khususnya hanya bisa"
Write-Host "dijalankan di Ubuntu."
Write-Host "`n"

# Tanya pengguna mau buka folder atau tidak
$openFolder = Read-Host "Buka folder tempat file disimpan? (y/n)"
if ($openFolder -eq "y" -or $openFolder -eq "Y") {
    Start-Process "explorer.exe" -ArgumentList $subsidiDir
}

Write-Host "`n🎉 Instalasi selesai!" -ForegroundColor Magenta
Write-Host "© 2025 Reza Walker`n" -ForegroundColor White
