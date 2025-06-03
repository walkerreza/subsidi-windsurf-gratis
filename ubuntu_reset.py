#!/usr/bin/env python3

import os
import subprocess
import time

def run_command(command, need_output=False):
    print(f"\n[Eksekusi] {command}")
    
    try:
        if need_output:
            result = subprocess.check_output(command, shell=True, text=True)
            return result.strip()
        else:
            subprocess.run(command, shell=True, check=True)
            return None
    except subprocess.CalledProcessError as e:
        print(f"\n[Error] Command gagal dijalankan: {e}")
        return None

def reset_machine_id():
    print("\n Reset device ID dimulai...\n")
    print("🔄 Proses reset device ID dimulai...\n")
    
    # Step 1: Hapus file machine-id
    run_command("sudo rm -f /etc/machine-id")
    print("✅ File machine-id berhasil dihapus!")
    
    # Step 2: Generate machine-id baru
    run_command("sudo systemd-machine-id-setup")
    print("✅ Machine ID baru berhasil dibuat!")
    
    # Step 3: Cek machine-id baru
    new_id = run_command("cat /etc/machine-id", need_output=True)
    if new_id:
        print(f"\n✨ Machine ID baru kamu adalah: {new_id}")
    
    # Step 4: Konfirmasi reboot
    print("\n⚠️ Sistem akan direboot dalam 10 detik... ⚠️")
    print("Kita akan segera kembali setelah reboot, tunggu sebentar~")
    
    # Countdown sebelum reboot
    for i in range(10, 0, -1):
        print(f"Reboot dalam {i} detik...", end="\r")
        time.sleep(1)
    
    # Reboot sistem
    run_command("sudo reboot")

if __name__ == "__main__":
    # Cek apakah berjalan di Ubuntu
    if os.path.exists("/etc/machine-id"):
        reset_machine_id()
    else:
        print("\n Script ini hanya dapat dijalankan di Ubuntu atau sistem Linux yang memiliki /etc/machine-id!")
        print("Maaf, sepertinya Anda tidak menjalankan ini di Ubuntu. Silakan jalankan di Ubuntu untuk melanjutkan.\n")
