import requests
from bs4 import BeautifulSoup
import sys

# Warna ANSI untuk tampilan terminal
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Verifikasi admin sebelum program berjalan
admin_code = input("Masukkan kode admin: ")
if admin_code != "admin123":
    print(f"{RED}Akses ditolak! Kode salah.{RESET}")
    sys.exit()

def check_security(url):
    print(f"\n{CYAN}Memeriksa keamanan situs: {url}{RESET}")
    print("=" * 50)

    weaknesses = []
    score = 100  # Skor awal 100% (tidak ada kelemahan)

    # Cek apakah menggunakan HTTPS
    if not url.startswith("https"):
        weaknesses.append("⚠️  Situs tidak menggunakan HTTPS.")
        score -= 20

    # Ambil halaman utama
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"{RED}❌ Error: Tidak dapat mengakses situs. {e}{RESET}")
        return

    # Cek header keamanan
    security_headers = [
        "Content-Security-Policy", "X-Frame-Options",
        "X-XSS-Protection", "Strict-Transport-Security",
        "X-Content-Type-Options", "Referrer-Policy"
    ]
    
    missing_headers = [h for h in security_headers if h not in response.headers]
    if missing_headers:
        weaknesses.append(f"⚠️  Header keamanan yang hilang: {', '.join(missing_headers)}")
        score -= len(missing_headers) * 5

    # Cek formulir tidak aman
    soup = BeautifulSoup(response.text, "html.parser")
    forms = soup.find_all("form")
    for form in forms:
        if form.get("action") and "https" not in form.get("action"):
            weaknesses.append(f"⚠️  Formulir tidak aman ditemukan: {form.get('action')}")
            score -= 10

    # Tampilkan hasil analisis
    print("\n🔍  Hasil Analisis Keamanan")
    print("=" * 50)
    if weaknesses:
        for weak in weaknesses:
            print(f"{YELLOW}{weak}{RESET}")
    else:
        print(f"{GREEN}✅ Tidak ditemukan kelemahan keamanan besar.{RESET}")
    
    print(f"\n🛡️  Skor Keamanan: {CYAN}{max(score, 0)}%{RESET}")
    print("=" * 50)

# Contoh pemakaian
url = input("\nMasukkan URL situs Anda: ")
check_security(url)