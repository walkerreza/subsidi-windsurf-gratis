#!/usr/bin/env python3

import os
import subprocess
import sys

# Pesan selamat datang
print("\n" + "-" * 60)
print("\t\tINSTALLER UBUNTU SUBSIDI TOOLS")
print("-" * 60)
print("\nHai! Setup otomatis dimulai...\n")

# Berikan executable permission ke semua file Python
files_to_chmod = ['menu.py', 'requirement.py', 'ubuntu_reset.py', 'installer.sh']

for file in files_to_chmod:
    if os.path.exists(file):
        print(f"[+] Memberikan permission executable ke {file}")
        os.chmod(file, 0o755)  # Equivalent to chmod +x
    else:
        print(f"[!] File {file} tidak ditemukan, dilewati")

# Buat script launcher (opsional)
print("\n[+] Membuat script launcher 'subsidi'")

# Path ke direktori saat ini
current_dir = os.path.dirname(os.path.abspath(__file__))

# Buat launcher script
launcher_content = f"#!/bin/bash\ncd {current_dir} && ./menu.py\n"

with open("subsidi", "w") as f:
    f.write(launcher_content)

# Berikan permission executable ke launcher
os.chmod("subsidi", 0o755)

# Tanya pengguna apakah ingin memindahkan launcher ke /usr/local/bin
print("\nApakah kamu ingin menambahkan command 'subsidi' ke sistem?")
print("Ini akan memungkinkan kamu menjalankan tools dengan mengetik 'subsidi' di terminal mana saja.")

choice = input("Install command 'subsidi'? (y/n): ")

if choice.lower() == 'y':
    try:
        # Pindahkan ke /usr/local/bin (perlu sudo)
        print("\n[+] Memindahkan launcher ke /usr/local/bin (perlu password sudo)")
        subprocess.run(["sudo", "mv", "subsidi", "/usr/local/bin/"], check=True)
        print("\n✓ Instalasi selesai! Kamu sekarang bisa menjalankan tools dengan mengetik 'subsidi' di terminal mana saja.")
    except subprocess.CalledProcessError:
        print("\n✗ Gagal memindahkan file. Pastikan kamu memiliki akses sudo.")
        print("  Kamu masih bisa menjalankan program dengan './menu.py' dari direktori ini.")
else:
    print("\nOke, kamu bisa menjalankan program dengan './menu.py' dari direktori ini.")

# Tanya apakah ingin langsung menjalankan program
print("\nApakah kamu ingin menjalankan program sekarang?")
choice = input("Jalankan program? (y/n): ")

if choice.lower() == 'y':
    print("\n[+] Menjalankan program...\n")
    # Jalankan menu.py
    os.execv(sys.executable, [sys.executable, 'menu.py'])
else:
    print("\nOke, kamu bisa menjalankan program nanti dengan ./menu.py")
    if choice.lower() == 'y' and os.path.exists("/usr/local/bin/subsidi"):
        print("atau dengan mengetik 'subsidi' di terminal mana saja.")

print("\nTerima kasih! Selamat mencoba!\n")
