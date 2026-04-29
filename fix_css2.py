# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define new CSS blocks for Hero A and Hero B
new_hero_a_css = '''/* ------------- VERSÃO A (LUXURY MINIMAL DARK) ------------- */
.hero-a {
    position: relative;
    background: #050814; /* Deep Navy Base */
    min-height: 100vh;
    display: flex;
    align-items: center;
    overflow: hidden;
    color: #ffffff;
}
/* Subtle Texture / Gradient / Lighting */
.hero-a::before {
    content: "";
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: radial-gradient(circle at 60% 40%, rgba(212, 175, 55, 0.08) 0%, transparent 60%),
                radial-gradient(circle at 20% 90%, rgba(255, 255, 255, 0.03) 0%, transparent 40%),
                url('data:image/svg+xml,%3Csvg width="60" height="60" viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg"%3E%3Cg fill="none" fill-rule="evenodd"%3E%3Cpath d="M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z" fill="%23cca43b" fill-opacity="0.03" fill-rule="nonzero"/%3E%3C/g%3E%3C/svg%3E');
    z-index: 1;
}
/* Optional subtle watermark */
.hero-a::after {
    content: "JUSTITIA";
    position: absolute;
    top: 50%; left: 0%;
    transform: translateY(-50%) rotate(0deg);
    font-size: 20rem;
    font-weight: 700;
    color: rgba(255,255,255,0.015);
    font-family: 'Playfair Display', serif;
    letter-spacing: 2rem;
    white-space: nowrap;
    z-index: 0;
    pointer-events: none;
}'''

new_hero_b_css = '''/* ------------- VERSÃO B (EDITORIAL LUXURY) ------------- */
.hero-b {
    position: relative;
    background: #2a2522; /* Editorial Warm Charcoal / Bronze Dark */
    min-height: 100vh;
    display: flex;
    align-items: center;
    overflow: hidden;
    color: #ffffff;
    /* Removed padding-top and top-border to keep structure identical to A */
}
/* Lighting and Texture */
.hero-b::before {
    content: "";
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: radial-gradient(circle at 30% 20%, rgba(212, 175, 55, 0.15) 0%, transparent 55%),
                linear-gradient(135deg, rgba(20,20,20,0.8) 0%, transparent 100%),
                url('data:image/svg+xml,%3Csvg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"%3E%3Cfilter id="noiseFilter"%3E%3CfeTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" stitchTiles="stitch"/%3E%3C/filter%3E%3Crect width="100%25" height="100%25" filter="url(%23noiseFilter)" opacity="0.05"/%3E%3C/svg%3E');
    z-index: 1;
}
/* Classic editorial motif */
.hero-b::after {
    content: "";
    position: absolute;
    top: 5%; bottom: 5%; left: 3%; right: 3%;
    border: 1px solid rgba(212, 175, 55, 0.1);
    z-index: 0;
    pointer-events: none;
}'''

# Replace Hero A CSS
html = re.sub(r'/\* ------------- VERSÃO A \(LUXURY MINIMAL DARK\) ------------- \*/.*?\.hero-a-content', new_hero_a_css + '\n.hero-a-content', html, flags=re.DOTALL)

# Replace Hero B CSS
html = re.sub(r'/\* ------------- VERSÃO B \(EDITORIAL LUXURY\) ------------- \*/.*?(?=/\* Fix modal/buttons inside A/B \*/)', new_hero_b_css + '\n\n', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("CSS injected")
