#!/usr/bin/env python3

import os
import sys
import time

# Import fungsi dari file requirement.py dan ubuntu_reset.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Coba import fungsi dari requirement.py
try:
    from requirement import install_chrome, install_curl, install_windsurf, install_all
    requirement_available = True
except ImportError:
    requirement_available = False

# Coba import fungsi dari ubuntu_reset.py
try:
    from ubuntu_reset import reset_machine_id
    reset_available = True
except ImportError:
    reset_available = False

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_banner():
    clear_screen()
    print("\n" + "-" * 60)
    print("\t\tUBUNTU SUBSIDI TOOLS")
    print("-" * 60)
    print("\nMenu Utama:\n")
    
    if requirement_available:
        print("1. Install Requirement:")
        print("   - Google Chrome")
        print("   - curl")
        print("   - Windsurf IDE")
    else:
        print("1. Install Requirement (Modul tidak tersedia)")
    
    if reset_available:
        print("2. Reset Device ID Ubuntu")
    else:
        print("2. Reset Device ID Ubuntu (Modul tidak tersedia)")
    
    print("3. Keluar\n")

def show_requirement_menu():
    if not requirement_available:
        print("\nModul requirement.py tidak tersedia. Silakan pastikan file ada di direktori yang sama.")
        input("\nTekan Enter untuk kembali ke menu utama...")
        return
    
    clear_screen()
    print("\n" + "-" * 60)
    print("\t\tMENU REQUIREMENT INSTALLER")
    print("-" * 60)
    print("\nPilih Instalasi:\n")
    print("1. Install Google Chrome")
    print("2. Install curl")
    print("3. Install Windsurf IDE")
    print("4. Install Semua (Chrome + curl + Windsurf)")
    print("5. Kembali ke Menu Utama\n")
    
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
        return
    else:
        print("\nPilihan tidak valid. Silakan pilih 1-5.")
        time.sleep(1.5)

def run_reset():
    if not reset_available:
        print("\nModul ubuntu_reset.py tidak tersedia. Silakan pastikan file ada di direktori yang sama.")
        input("\nTekan Enter untuk kembali ke menu utama...")
        return
    
    confirm = input("\nApakah kamu yakin ingin mereset Device ID Ubuntu? (y/n): ")
    if confirm.lower() == 'y':
        reset_machine_id()
    else:
        print("\nReset dibatalkan.")
        input("\nTekan Enter untuk kembali ke menu utama...")

def main():
    while True:
        show_banner()
        choice = input("Pilih menu [1-3]: ")
        
        if choice == '1':
            show_requirement_menu()
        elif choice == '2':
            run_reset()
        elif choice == '3':
            print("\nKeluar dari program. Sampai jumpa kembali!\n")
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih 1-3.")
            time.sleep(1.5)

if __name__ == "__main__":
    # Cek apakah script dijalankan di Ubuntu/Linux
    if os.path.exists("/etc/os-release") or os.name == 'nt':  # Izinkan juga dijalankan di Windows untuk testing
        main()
    else:
        print("\nScript ini sebaiknya dijalankan di Ubuntu atau sistem Linux lainnya.")
        print("Beberapa fitur mungkin tidak berfungsi di sistem operasi lain.\n")
