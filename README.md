✨ What It Does
GeoPorsuk is a fully browser-based WebGL application designed to let you draw a region of interest on a 3D Earth globe and transform that area into a procedurally generated, realistic 3D terrain.

🎬 How It Works
🌐 Launch the application → A rotating 3D Earth globe greets you.
✏️ Click the "Draw Polygon" button.
🖱️ Click on the globe to define the vertices of your desired region (minimum 3 points).
✅ Double-click, right-click, or click the "Complete" button to close the polygon.
🏔️ The system automatically generates a custom 3D terrain specifically for that region.
📸 Take and save a screenshot of your generated 3D landscape if desired.

Technologies Used
Three.js r128 — 3D rendering engine

WebGL — GPU-accelerated graphics

Canvas 2D API — Texture generation (earth, wood, clouds)

Vanilla JavaScript — Zero dependencies, zero frameworks

🚀 Installation & Setup
Option 1: Run Locally

Bash:
# Clone the repository
git clone https://github.com/your-username/geoporsuk.git
cd geoporsuk

# Run with any local development server
# If you have Python installed:
python -m http.server 8080

# If you have Node.js installed:
npx serve .


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
TÜRKÇE METİN
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 🌍 GeoPorsuk — 3D Dünya Haritası & Arazi Analizi

> *Bir polygon çiz. Dünyayı 3 boyuta taşı.*

![GeoPorsuk Banner](https://img.shields.io/badge/WebGL-3D%20GIS%20Explorer-4a9eff?style=for-the-badge&logo=opengl)
![Three.js](https://img.shields.io/badge/Three.js-r128-black?style=for-the-badge&logo=three.js)
![Vanilla JS](https://img.shields.io/badge/Vanilla-JavaScript-f7df1e?style=for-the-badge&logo=javascript)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## ✨ Ne Yapar?

GeoPorsuk, dünya küresi üzerinde istediğin bir bölgeyi çizmen ve o bölgeyi
**prosedürel olarak üretilmiş, gerçekçi 3D araziye** dönüştürmen için
tasarlanmış, tamamen tarayıcı tabanlı bir WebGL uygulamasıdır.

## 🎬 Nasıl Çalışır?
🌐 Uygulama açılır → Dönen dünya küresi karşılar
✏️ "Polygon Çiz" butonuna tıkla
🖱️ Küre üzerinde istediğin bölgenin köşelerine tıkla (min 3 nokta)
✅ Çift tık / Sağ tık / "Tamamla" butonu ile polygon'u kapat
🏔️ Sistem otomatik olarak o bölgeye özel 3D arazi oluşturur
📸 İstersen ekran görüntüsü al ve kaydet


### Kullanılan Teknolojiler
- **[Three.js r128](https://threejs.org/)** — 3D render motoru
- **WebGL** — GPU hızlandırmalı grafik
- **Canvas 2D API** — Doku üretimi (dünya, ahşap, bulut)
- **Vanilla JavaScript** — Sıfır bağımlılık, sıfır framework

---

## 🚀 Kurulum

### Seçenek 1: Doğrudan Aç
```bash
# Repo'yu klonla
git clone https://github.com/kullanici-adi/geoporsuk.git
cd geoporsuk

# Herhangi bir local sunucu ile aç
# Python varsa:
python -m http.server 8080

# Node.js varsa:
npx serve .



