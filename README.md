# Ubuntu Subsidi Tools 🚀

Kumpulan tools praktis untuk membantu kamu dalam menyiapkan Ubuntu dengan cepat dan mudah! 💻

## 🌟 Fitur

Repo ini berisi beberapa tools keren yang bisa kamu gunakan di Ubuntu:

- **Reset Device ID Ubuntu** - Reset machine-id dengan mudah
- **Instalasi Google Chrome** - Install browser Chrome dengan satu klik
- **Instalasi curl** - Setup curl dengan cepat
- **Instalasi Windsurf IDE** - Dapatkan editor code favorit dengan mudah

## 📋 Daftar File

- `menu.py` - Menu utama yang menghubungkan semua tools
- `ubuntu_reset.py` - Script untuk reset device ID Ubuntu
- `requirement.py` - Script untuk instalasi Chrome, curl, dan Windsurf IDE
- `setup.py` - Installer otomatis (recommended)
- `installer.sh` - Installer alternatif berbasis bash

## 🚀 Cara Penggunaan

### Metode Paling Mudah (Recommended)

1. Clone repository ini ke Ubuntu kamu
   ```bash
   git clone https://github.com/username/subsidi.git
   cd subsidi
   ```

2. Jalankan setup.py untuk instalasi otomatis
   ```bash
   python3 setup.py
   ```

3. Ikuti petunjuk di layar untuk menyelesaikan setup

4. Setelah setup selesai, kamu bisa menjalankan tools dengan perintah
   ```bash
   subsidi
   ```

### Metode Manual

1. Clone repository
   ```bash
   git clone https://github.com/username/subsidi.git
   cd subsidi
   ```

2. Berikan permission executable ke file-file Python
   ```bash
   chmod +x menu.py requirement.py ubuntu_reset.py
   ```

3. Jalankan menu utama
   ```bash
   ./menu.py
   ```

## 📝 Catatan Penting

- Tools ini dirancang untuk Ubuntu dan distro Linux berbasis Debian
- Beberapa fitur memerlukan akses sudo
- Reset device ID akan mereboot sistem

## 🛠️ Requirements

- Python 3.6 atau lebih baru
- Akses internet untuk instalasi paket
- Akses sudo (untuk beberapa fitur)

## 📜 License

MIT

---

Dibuat dengan ❤️ untuk membuat hidup lebih mudah dengan Ubuntu!
