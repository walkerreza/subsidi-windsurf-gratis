#!/usr/bin/env python3

import os
import subprocess
import time

def clear_screen():
    os.system('clear')

def run_command(command):
    print(f"\n[Eksekusi] {command}")
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n[Error] Command gagal dijalankan: {e}")
        return False

def show_banner():
    clear_screen()
    print("\n" + "-" * 60)
    print("\t\tUBUNTU REQUIREMENT INSTALLER")
    print("-" * 60)
    print("\nMenu Instalasi:\n")
    print("1. Install Google Chrome")
    print("2. Install curl")
    print("3. Install Windsurf IDE")
    print("4. Install Semua (Chrome + curl + Windsurf)")
    print("5. Keluar\n")

def install_chrome():
    print("\n[+] Memulai instalasi Google Chrome...")
    
    # Tambahkan repository key Google Chrome
    print("[+] Menambahkan Google Chrome repository key...")
    run_command("wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -")
    
    # Tambahkan Google Chrome repository
    print("[+] Menambahkan Google Chrome repository...")
    run_command("sudo sh -c 'echo \"deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main\" > /etc/apt/sources.list.d/google-chrome.list'")
    
    # Update package list
    print("[+] Mengupdate package list...")
    run_command("sudo apt update")
    
    # Install Google Chrome
    print("[+] Menginstall Google Chrome...")
    success = run_command("sudo apt install -y google-chrome-stable")
    
    if success:
        print("\n✓ Google Chrome berhasil diinstall!")
        print("  Kamu bisa menjalankannya dengan perintah: google-chrome-stable")
    else:
        print("\n✗ Instalasi Google Chrome gagal. Silakan coba lagi nanti.")
    
    input("\nTekan Enter untuk kembali ke menu...")

def install_curl():
    print("\n[+] Memulai instalasi curl...")
    
    # Update package list
    print("[+] Mengupdate package list...")
    run_command("sudo apt update")
    
    # Install curl
    print("[+] Menginstall curl...")
    success = run_command("sudo apt install -y curl")
    
    if success:
        print("\n✓ curl berhasil diinstall!")
        print("  Versi curl yang terinstall:")
        run_command("curl --version | head -n 1")
    else:
        print("\n✗ Instalasi curl gagal. Silakan coba lagi nanti.")
    
    input("\nTekan Enter untuk kembali ke menu...")

def install_windsurf():
    print("\n[+] Memulai instalasi Windsurf IDE...")
    
    # Install dependencies
    print("[+] Menginstall dependencies...")
    run_command("sudo apt update && sudo apt install -y apt-transport-https gnupg ca-certificates software-properties-common wget")
    
    # Download dan tambahkan Windsurf repository key
    print("[+] Menambahkan Windsurf repository key...")
    run_command("wget -qO- https://apt.windsurf.com/keys/public | sudo tee /etc/apt/trusted.gpg.d/windsurf.asc")
    
    # Tambahkan Windsurf repository
    print("[+] Menambahkan Windsurf repository...")
    run_command("echo \"deb [signed-by=/etc/apt/trusted.gpg.d/windsurf.asc] https://apt.windsurf.com/ stable main\" | sudo tee /etc/apt/sources.list.d/windsurf.list")
    
    # Update package list
    print("[+] Mengupdate package list...")
    run_command("sudo apt update")
    
    # Install Windsurf IDE
    print("[+] Menginstall Windsurf IDE...")
    success = run_command("sudo apt install -y windsurf")
    
    if success:
        print("\n✓ Windsurf IDE berhasil diinstall!")
        print("  Kamu bisa menjalankannya dengan perintah: windsurf")
    else:
        print("\n✗ Instalasi Windsurf IDE gagal.")
        print("  Jika instalasi gagal, kamu juga bisa mengunjungi website resmi Windsurf untuk download langsung:")
        print("  https://windsurf.com/editor/download-linux")
    
    input("\nTekan Enter untuk kembali ke menu...")

def install_all():
    print("\n[+] Memulai instalasi semua requirement (Chrome, curl, Windsurf)...")
    time.sleep(1)
    
    print("\n[+] Langkah 1/3: Instalasi Google Chrome")
    install_chrome()
    
    print("\n[+] Langkah 2/3: Instalasi curl")
    install_curl()
    
    print("\n[+] Langkah 3/3: Instalasi Windsurf IDE")
    install_windsurf()
    
    print("\n✓ Semua requirement berhasil diinstall!")
    input("\nTekan Enter untuk kembali ke menu...")

def main():
    while True:
        show_banner()
        choice = input("Pilih menu [1-5]: ")
        
        if choice == '1':
            install_chrome()
        elif choice == '2':
            install_curl()
        elif choice == '3':
            install_windsurf()
        elif choice == '4':
            install_all()
        elif choice == '5':
            print("\nKeluar dari program. Sampai jumpa kembali!\n")
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih 1-5.")
            time.sleep(1.5)

if __name__ == "__main__":
    # Cek apakah script dijalankan di Ubuntu/Linux
    if os.path.exists("/etc/os-release"):
        main()
    else:
        print("\nScript ini hanya dapat dijalankan di Ubuntu atau sistem Linux lainnya.")
        print("Silakan jalankan di Ubuntu untuk melanjutkan.\n")