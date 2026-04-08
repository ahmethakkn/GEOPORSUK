#!/usr/bin/env python3
"""
GIS Explorer — Yerel Geliştirme Sunucusu
=========================================
Kullanım:
    python server.py

Ardından tarayıcıda açın:
    http://localhost:8000

Durdurmak için: Ctrl+C
"""

import http.server
import socketserver
import os
import sys
import webbrowser
import threading

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class GISHandler(http.server.SimpleHTTPRequestHandler):
    """Statik dosyaları sunar; CORS ve cache-control başlıkları ekler."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Yerel geliştirme için CORS izni
        self.send_header("Access-Control-Allow-Origin", "*")
        # Tarayıcı önbelleğini devre dışı bırak — her yenilemede güncel dosyayı al
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, format, *args):
        # Sadece hataları ve ilk isteği göster, 304 gürültüsünü gizle
        if args and str(args[1]) not in ("304", "200"):
            super().log_message(format, *args)


def open_browser(url: str):
    """Sunucu hazır olduktan sonra tarayıcıyı aç."""
    threading.Timer(0.8, webbrowser.open, args=[url]).start()


def main():
    os.chdir(DIRECTORY)

    # index.html yoksa uyar
    if not os.path.exists(os.path.join(DIRECTORY, "index.html")):
        print("⚠️  UYARI: index.html bu klasörde bulunamadı.")
        print(f"   Klasör: {DIRECTORY}")

    # ek1.mp4 yoksa uyar
    if not os.path.exists(os.path.join(DIRECTORY, "ek1.mp4")):
        print("⚠️  UYARI: ek1.mp4 bu klasörde bulunamadı.")
        print("   Intro videosu çalışmayacak; otomatik geçiş devreye girecek.")

    url = f"http://localhost:{PORT}"

    try:
        with socketserver.TCPServer(("", PORT), GISHandler) as httpd:
            httpd.allow_reuse_address = True
            print("─" * 48)
            print("  🌍  3D GIS Explorer — Geliştirme Sunucusu")
            print("─" * 48)
            print(f"  Adres  : {url}")
            print(f"  Klasör : {DIRECTORY}")
            print("  Durdurmak için Ctrl+C")
            print("─" * 48)
            open_browser(url)
            httpd.serve_forever()
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"\n❌  Port {PORT} zaten kullanımda.")
            print(f"   Farklı bir port için: PORT={PORT+1} python server.py")
        else:
            print(f"\n❌  Sunucu hatası: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n✓  Sunucu durduruldu.")


if __name__ == "__main__":
    main()
