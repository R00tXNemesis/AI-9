# AI-9
How Far AI Change The World - Web Security Scanner 2.0


## 🔍 Web Security Scanner ##

Web Security Scanner adalah alat berbasis Python untuk menganalisis keamanan situs web. Dengan fitur deteksi kelemahan, alat ini memberikan laporan tentang keamanan situs beserta skor persentase berdasarkan kelemahan yang ditemukan.

🎯 Fitur Utama

✅ Verifikasi Admin – Hanya dapat dijalankan dengan kode admin (admin123).
✅ Analisis HTTPS – Memeriksa apakah situs menggunakan protokol aman.
✅ Pemeriksaan Header Keamanan – Mendeteksi header penting yang hilang.
✅ Deteksi Formulir Tidak Aman – Menemukan formulir dengan metode pengiriman data tidak terenkripsi.
✅ Skor Keamanan – Memberikan nilai keamanan berbasis persentase.
✅ Tampilan Profesional – Menggunakan warna dan ikon untuk laporan yang jelas.

⚡ Cara Instalasi

Pastikan Python sudah terinstal di perangkat Anda, lalu jalankan:

pip install requests beautifulsoup4

🚀 Cara Menggunakan

1. Jalankan skrip di terminal atau Termux:

python security_scanner.py


2. Masukkan kode admin (default: admin123).


3. Masukkan URL situs web yang ingin diperiksa.


4. Hasil analisis keamanan akan ditampilkan, termasuk kelemahan dan skor keamanan.



📌 Contoh Output

Masukkan kode admin: ******
Masukkan URL situs Anda: http://example.com

🔍  Hasil Analisis Keamanan :

⚠️  Situs tidak menggunakan HTTPS.
⚠️  Header keamanan yang hilang: Content-Security-Policy, X-Frame-Options
🛡️  Skor Keamanan: 70%
