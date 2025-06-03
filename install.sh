#!/bin/bash

# Installer script untuk Ubuntu Subsidi Tools
# Dibuat oleh Reza Walker

echo "🦅 PEMERINTAH KABUPATEN BLITAR 🇮🇩"
echo "SISTEM INFORMASI SUBSIDI TEPAT GUNA"
echo "🔴⚪ BERSATU KITA TEGUH, BERCERAI KITA RUNTUH ⚪🔴"
echo ""
echo "[+] Memulai download tools..."

# Buat direktori subsidi jika belum ada
mkdir -p ~/subsidi
cd ~/subsidi

# Download semua file yang dibutuhkan dari GitHub
echo "[+] Downloading ubuntu_reset.py..."
curl -s -O https://raw.githubusercontent.com/username/subsidi/main/ubuntu_reset.py

echo "[+] Downloading requirement.py..."
curl -s -O https://raw.githubusercontent.com/username/subsidi/main/requirement.py

echo "[+] Downloading menu.py..."
curl -s -O https://raw.githubusercontent.com/username/subsidi/main/menu.py

echo "[+] Downloading setup.py..."
curl -s -O https://raw.githubusercontent.com/username/subsidi/main/setup.py

echo "[+] Downloading installer.sh..."
curl -s -O https://raw.githubusercontent.com/username/subsidi/main/installer.sh

# Berikan permission executable
echo "[+] Memberikan permission executable..."
chmod +x *.py installer.sh

echo ""
echo "✅ Download selesai! Semua file telah tersimpan di ~/subsidi"

# Tanya user apakah ingin menjalankan setup
echo ""
echo "Apakah kamu ingin menjalankan setup sekarang?"
read -p "Jalankan setup? (y/n): " choice

if [[ $choice == "y" || $choice == "Y" ]]; then
    echo "[+] Menjalankan setup.py..."
    python3 setup.py
else
    echo "[+] Kamu bisa menjalankan setup nanti dengan perintah:"
    echo "    cd ~/subsidi && python3 setup.py"
fi

echo ""
echo "🇮🇩 Terima kasih telah menggunakan tools ini! 🇮🇩"
echo "Hak Cipta © 2025 Reza Walker"
