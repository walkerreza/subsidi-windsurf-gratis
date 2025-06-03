#!/bin/bash

# Installer script untuk Ubuntu Subsidi Tools
# Dibuat oleh Reza Walker

echo "🦅 PEMERINTAH KABUPATEN BLITAR 🇮🇩"
echo "SISTEM INFORMASI SUBSIDI TEPAT GUNA"
echo "🔴⚪ BERSATU KITA TEGUH, BERCERAI KITA RUNTUH ⚪🔴"
echo ""
echo "[+] Memulai download tools..."

# Buat direktori subsidi-windsurf jika belum ada
SUBSIDI_DIR="$HOME/subsidi-windsurf"
echo "[+] Membuat direktori: $SUBSIDI_DIR"
mkdir -p "$SUBSIDI_DIR"
cd "$SUBSIDI_DIR" || { echo "[!] Gagal masuk ke direktori $SUBSIDI_DIR. Mencoba direktori Downloads..."; SUBSIDI_DIR="$HOME/Downloads/subsidi-windsurf"; mkdir -p "$SUBSIDI_DIR"; cd "$SUBSIDI_DIR" || { echo "[!] ERROR: Tidak bisa membuat direktori. Menggunakan direktori saat ini."; SUBSIDI_DIR="$(pwd)"; }; }

# Download semua file yang dibutuhkan dari GitHub
echo ""  # Baris kosong
echo "[+] Menyimpan file ke direktori: $SUBSIDI_DIR"
echo ""  # Baris kosong
echo "[+] Downloading ubuntu_reset.py..."
curl -s -O https://raw.githubusercontent.com/walkerreza/subsidi-windsurf-gratis/main/ubuntu_reset.py

echo "[+] Downloading requirement.py..."
curl -s -O https://raw.githubusercontent.com/walkerreza/subsidi-windsurf-gratis/main/requirement.py

echo "[+] Downloading menu.py..."
curl -s -O https://raw.githubusercontent.com/walkerreza/subsidi-windsurf-gratis/main/menu.py

echo "[+] Downloading setup.py..."
curl -s -O https://raw.githubusercontent.com/walkerreza/subsidi-windsurf-gratis/main/setup.py

echo "[+] Downloading installer.sh..."
curl -s -O https://raw.githubusercontent.com/walkerreza/subsidi-windsurf-gratis/main/installer.sh

# Berikan permission executable
echo "[+] Memberikan permission executable..."
chmod +x *.py installer.sh

echo ""
# Cek apakah file berhasil didownload
echo ""  # Baris kosong
echo "[+] Memverifikasi file yang didownload..."
MISSING_FILES=""
for file in ubuntu_reset.py requirement.py menu.py setup.py installer.sh; do
    if [ ! -f "$file" ]; then
        MISSING_FILES="$MISSING_FILES $file"
    fi
done

if [ -z "$MISSING_FILES" ]; then
    echo "\n✅ Download berhasil! Semua file telah tersimpan di: $SUBSIDI_DIR"
    ls -la
else
    echo "\n⚠️ Beberapa file tidak berhasil didownload:$MISSING_FILES"
    echo "\nFile yang ada di direktori $SUBSIDI_DIR:"
    ls -la
fi

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
