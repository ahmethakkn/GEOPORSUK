# 🌍 3D GIS Explorer

A fully client-side, zero-dependency 3D Geographic Information System built with pure HTML, CSS, and Three.js. Draw any polygon on an interactive globe, then instantly generate a 3D terrain model of that exact area — textured with real OpenStreetMap tiles, no API key required.

---

## ✨ Features

### 🌐 Interactive Globe
- Real-time rotating Earth rendered with Three.js WebGL
- Satellite texture loaded from CDN with a procedural canvas fallback
- Dual-layer atmosphere glow effect
- 9,000-star skybox with uniform spherical distribution
- Smooth orbit camera with exponential easing (lerp interpolation)
- Full mouse drag, scroll-to-zoom, and pinch-to-zoom (touch) support

### ✏️ Polygon Drawing System
- Click-to-place vertices on the globe surface using GPU raycasting
- Visual markers and live edge preview as you draw
- Undo last point, clear all, or close polygon via double-click / right-click
- Minimum 3 points enforced before terrain generation

### 🏔️ Polygon-Shaped 3D Terrain
- Terrain geometry is **cut to the exact polygon shape** — no square planes, no overflow
- Centroid-clip algorithm removes all grid quads outside the drawn boundary
- Procedural height via **fBm (Fractional Brownian Motion)** noise with ridge blending
- Heights applied only to vertices inside the polygon
- Dynamic camera distance automatically adapts to polygon size

### 🗺️ OpenStreetMap Texture (No API Key)
- Automatically fetches OSM tile mosaic for the drawn area
- Zoom level auto-selected based on polygon extent (Z8 → Z16)
- Tiles assembled on a canvas and applied as a Three.js texture
- Placeholder color shown instantly; texture swaps in when tiles load
- Failed tile fetches degrade gracefully (no crash)

### 💧 Volumetric Water System
- Water rendered as an **ExtrudeGeometry solid**, not a flat plane
- Side faces visible when viewing from any angle
- Slider controls physical water level (0 → MAXH metres)
- `scale.y` technique keeps the water base fixed at Y=0 while only the top surface rises
- Live metre readout both in sidebar and as an on-canvas overlay pill
- Opacity fixed at 72% — always shows terrain colour beneath

### 🪵 Polygon-Shaped Wooden Base
- Extrusion follows the exact same polygon outline as the terrain
- Procedural wood grain texture generated via Canvas 2D API

### 🎛️ Real-Time Controls (All Wired)
| Control | Effect |
|---|---|
| Rotation slider | Rotates the globe camera target angle |
| Height exaggeration | Changes terrain MAXH on next build |
| Grid density | Changes mesh segment count (32–128) on next build |
| Sun intensity | Updates `DirectionalLight.intensity` live |
| Ambient intensity | Updates `AmbientLight.intensity` live |
| Water level | Moves water surface up/down physically in real time |

### 📸 Screenshot Export
- One-click PNG download of the active canvas (globe or terrain)
- Uses `requestAnimationFrame` + `toDataURL` to capture a complete render frame
- Green toast notification on success

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| 3D Rendering | [Three.js r128](https://threejs.org/) (CDN, no install) |
| Map Tiles | [OpenStreetMap](https://www.openstreetmap.org/) standard tile server |
| Terrain Height | Procedural fBm (Fractional Brownian Motion) noise |
| Coordinate System | Equirectangular projection (centroid-centred) |
| Language | Vanilla JavaScript (ES5-compatible IIFE) |
| Styling | Pure CSS with CSS custom properties |
| Build Tool | None — single HTML file |

---

## 🚀 Getting Started

No installation, no build step, no package manager.

```bash
git clone https://github.com/your-username/3d-gis-explorer.git
cd 3d-gis-explorer
```

Open `index.html` in any modern browser.

> **Recommended browsers:** Chrome 90+, Firefox 88+, Edge 90+  
> WebGL must be enabled (it is by default in all modern browsers).

### Running with a local server (optional but recommended for tile CORS)

```bash
# Python 3
python -m http.server 8080

# Node.js
npx serve .
```

Then open `http://localhost:8080`.

---

## 🎮 How to Use

1. **Watch the intro** or click **ATLA →** to skip
2. **Rotate the globe** by dragging; scroll / pinch to zoom
3. Open the **Çizim** panel in the sidebar
4. Click **Polygon Çiz** to enter drawing mode
5. **Click on the globe** to place vertices (minimum 3)
6. **Double-click** or **right-click** to close the polygon
7. The 3D terrain view opens automatically — OSM tiles load within seconds
8. Use the **Su** slider to raise and lower the water level
9. Use the **Işık** sliders to adjust sun and ambient light
10. Click **⬇ Ekran Görüntüsü Al** to save a PNG
11. Click **← Haritaya Dön** to return to the globe

---

## 📁 Project Structure

```
3d-gis-explorer/
└── index.html          # Entire application — CSS + HTML + JS in one file
```

Everything is self-contained. The only external resources fetched at runtime are:

- `https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js` — Three.js library
- `https://tile.openstreetmap.org/{z}/{x}/{y}.png` — Map tiles
- `https://raw.githubusercontent.com/mrdoob/three.js/...earth_atmos_2048.jpg` — Globe texture (falls back to canvas if unavailable)
- `ek1.mp4` — Intro video (optional; skipped automatically if missing)

---

## 🧠 Architecture

### Coordinate Pipeline

```
Globe click
  → Raycasting (NDC → world space)
  → Sphere intersection → lat/lon
  → Centroid-centred equirectangular projection
  → Local metre space
  → Three.js units (scale factor sc)
  → 2D polygon (pts2D)
```

### Terrain Generation Pipeline

```
pts2D polygon
  → Bounding box grid (SEG × SEG quads)
  → Centroid-clip: remove quads outside polygon
  → fBm height per vertex (7 octaves + ridge noise)
  → Min/max normalise → multiply by MAXH
  → OSM UV mapping per vertex
  → BufferGeometry (position + uv + index)
  → computeVertexNormals()
  → Async OSM tile mosaic → CanvasTexture applied
```

### Water Volume Math

```
ExtrudeGeometry(polyShape, depth=MAXH) + rotateX(-π/2)

scale.y = waterLevel / MAXH
position.y = 0 (always)

bottom_face = 0 - (MAXH/2)·scale.y + MAXH/2·scale.y = 0  ✓
top_face    = MAXH · scale.y = waterLevel               ✓
```

---

## ⚙️ Configuration

All tunable constants are exposed as sidebar sliders. The key values in code:

| Variable | Default | Description |
|---|---|---|
| `INTRO_MS` | `4000` | Intro screen duration (ms) |
| `MAXH` | `slider×2+75` | Maximum terrain height (Three.js units) |
| `SEG` | `32–128` | Grid segment count (slider-driven) |
| `SEED` | `random` | fBm noise seed (new terrain each build) |
| `tZ` | `8–16` | OSM tile zoom (auto-selected) |
| Water opacity | `0.72` | Fixed — adjust in `tWaterMat` |

---

## 🌐 OpenStreetMap Usage

Map tiles © [OpenStreetMap contributors](https://www.openstreetmap.org/copyright), licensed under [ODbL](https://opendatacommons.org/licenses/odbl/).

This project complies with the [OSM Tile Usage Policy](https://operations.osmfoundation.org/policies/tiles/):
- Tiles are fetched on demand, only for the area the user explicitly draws
- No bulk downloading or caching beyond the browser's native HTTP cache
- The application is non-commercial and open source

---

## 🔧 Known Limitations

- **CORS on tiles:** Some browsers block cross-origin tile requests when opening `index.html` directly from the filesystem. Use a local HTTP server to resolve this.
- **Large polygons:** Very large areas (continent scale) may load slowly due to tile count. The auto-zoom selection keeps tile requests reasonable.
- **Height data:** Elevation is procedural (fBm noise), not real-world DEM data. The OSM texture reflects real geography; the terrain shape is artistic.
- **Memory:** Each `buildTerrain` call disposes previous GPU objects. Rapid repeated polygon drawing is safe.

---

## 🔮 Possible Extensions

- [ ] Real elevation data via [OpenTopoData](https://www.opentopodata.org/) (free, no key)
- [ ] Export terrain as `.glb` / `.obj`
- [ ] Animate water rise/fall over time
- [ ] Multiple polygon layers with colour coding
- [ ] Measurement tools (area, perimeter in km²)
- [ ] Search/geocode box using [Nominatim](https://nominatim.org/) (free, no key)

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙏 Acknowledgements

- [Three.js](https://threejs.org/) — WebGL abstraction
- [OpenStreetMap](https://www.openstreetmap.org/) — Free map tiles
- Inspired by GIS visualization tools like QGIS and CesiumJS
