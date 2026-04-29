import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# New Style replacing the old one
new_style = '''<style>
/* =========================================================================
   STYLE A/B TEST - Navbar + Heros (Versões A e B)
   ========================================================================= */

/* ------------- NAVBAR PREMIUM ------------- */
.navbar {
    padding: 20px 0;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    background: transparent;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.navbar.scrolled {
    padding: 12px 0;
    background: rgba(8, 12, 22, 0.9) !important;
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(212, 175, 55, 0.2);
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
}
.brand-text-main {
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    color: #fff;
    font-size: 1.5rem;
    letter-spacing: 1px;
    margin-bottom: 0;
    line-height: 1;
}
.brand-text-sub {
    font-family: 'Lato', sans-serif;
    font-weight: 300;
    color: var(--gold);
    font-size: 0.75rem;
    letter-spacing: 4px;
    text-transform: uppercase;
}
.nav-link {
    font-family: 'Lato', sans-serif;
    font-size: 0.85rem;
    font-weight: 400;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: rgba(255,255,255,0.7) !important;
    position: relative;
    padding: 8px 12px !important;
    margin: 0 5px;
    transition: color 0.3s ease;
}
.nav-link:hover, .nav-link.active {
    color: #cca43b !important;
}
.nav-link::after {
    content: '';
    position: absolute;
    width: 0;
    height: 1px;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    background-color: #cca43b;
    transition: width 0.3s ease;
}
.nav-link:hover::after, .nav-link.active::after {
    width: 100%;
}
.btn-nav-outline {
    border: 1px solid rgba(212, 175, 55, 0.5);
    color: #cca43b !important;
    border-radius: 0;
    padding: 10px 24px !important;
    transition: all 0.3s ease;
}
.btn-nav-outline:hover {
    background: rgba(212, 175, 55, 0.1);
    color: #cca43b !important;
}

/* ------------- GLOBAL CLASSES ------------- */
:root {
    --gold: #cca43b;
    --gold-light: #e8c678;
    --dark-bg: #080a0f;
    --light-bg: #F9F8F5; /* off-white/champagne */
}
.gold-text { color: var(--gold); }
.gold-line {
    width: 40px;
    height: 1px;
    background: var(--gold);
    display: inline-block;
}
.gold-line-vert {
    width: 1px;
    height: 60px;
    background: var(--gold);
    margin: 0 auto;
}
.font-serif { font-family: 'Playfair Display', serif; }

/* ------------- VERSÃO A (LUXURY MINIMAL DARK) ------------- */
.hero-a {
    position: relative;
    background: var(--dark-bg);
    min-height: 100vh;
    display: flex;
    align-items: center;
    overflow: hidden;
    color: #ffffff;
}
/* Subtle Texture / Gradient */
.hero-a::before {
    content: "";
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: radial-gradient(circle at 70% 30%, rgba(212, 175, 55, 0.05) 0%, transparent 50%),
                radial-gradient(circle at 30% 80%, rgba(255, 255, 255, 0.02) 0%, transparent 40%);
    z-index: 1;
}
.hero-a-content {
    position: relative;
    z-index: 3;
}
.hero-a-title {
    font-size: clamp(3rem, 5vw, 4.5rem);
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: 25px;
}
.hero-a-subtitle {
    font-family: 'Lato', sans-serif;
    font-size: 1.1rem;
    font-weight: 300;
    color: #cfd4da;
    line-height: 1.8;
}
.trust-indicators {
    margin-top: 40px;
    display: flex;
    gap: 30px;
    align-items: center;
    border-top: 1px solid rgba(255,255,255,0.05);
    padding-top: 20px;
}
.trust-item {
    font-size: 0.8rem;
    color: rgba(255,255,255,0.6);
    letter-spacing: 1px;
    text-transform: uppercase;
}
.hero-a-video-wrapper {
    position: relative;
    z-index: 3;
    border: 1px solid rgba(212, 175, 55, 0.2);
    padding: 10px;
    background: rgba(255,255,255,0.02);
}
.hero-a-video-wrapper video {
    width: 100%;
    filter: brightness(0.9) contrast(1.1);
    display: block;
}

/* ------------- VERSÃO B (EDITORIAL LUXURY) ------------- */
.hero-b {
    position: relative;
    background: var(--light-bg);
    min-height: 100vh;
    display: flex;
    align-items: center;
    overflow: hidden;
    color: #1a1a1a;
    padding-top: 100px; /* offset for navbar */
    border-top: 2px solid var(--gold);
}
.hero-b-bg-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-family: 'Playfair Display', serif;
    font-size: 25vw;
    font-weight: 700;
    color: rgba(0,0,0,0.02);
    z-index: 0;
    white-space: nowrap;
    pointer-events: none;
}
.hero-b-content {
    position: relative;
    z-index: 2;
}
.hero-b-suptitle {
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--gold);
    display: block;
    margin-bottom: 15px;
}
.hero-b-title {
    font-size: clamp(3.5rem, 6vw, 5.5rem);
    font-weight: 600;
    line-height: 1;
    letter-spacing: -2px;
    margin-bottom: 30px;
    position: relative;
}
.hero-b-text {
    font-family: 'Lato', sans-serif;
    font-size: 1.15rem;
    font-weight: 300;
    color: #4a4a4a;
    line-height: 1.8;
    max-width: 90%;
}
.hero-b-video-wrapper {
    position: relative;
    z-index: 2;
    margin-top: -50px;
    box-shadow: 20px 20px 0px rgba(212, 175, 55, 0.1);
}
.hero-b-video-wrapper::before {
    content: "";
    position: absolute;
    top: -20px;
    right: -20px;
    width: 100px;
    height: 100px;
    border-top: 2px solid var(--gold);
    border-right: 2px solid var(--gold);
    z-index: -1;
}
.hero-b-video-wrapper video {
    width: 100%;
    display: block;
}

/* Fix modal/buttons inside A/B */
.btn-gold {
    background: var(--gold);
    color: #fff;
    border: none;
    border-radius: 0;
    padding: 15px 35px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: all 0.3s;
}
.btn-gold:hover { background: #b58d28; color: #fff; }
.btn-dark-outline {
    border: 1px solid #1a1a1a;
    color: #1a1a1a;
    border-radius: 0;
    padding: 15px 35px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: all 0.3s;
}
.btn-dark-outline:hover { background: #1a1a1a; color: #fff; }
.controls-overlay {
    position: absolute;
    bottom: 20px; right: 20px;
    z-index: 10;
    display: flex; gap: 10px;
}
.controls-overlay button {
    background: rgba(0,0,0,0.5);
    border: 1px solid rgba(255,255,255,0.2);
    color: white;
    width: 40px; height: 40px;
    display: flex; align-items: center; justify-content: center;
    cursor: pointer; transition: 0.3s;
}
.controls-overlay button:hover { background: var(--gold); border-color: var(--gold); }
</style>'''

html = re.sub(r'<style>.*?</style>', new_style, html, flags=re.DOTALL)

# Nav Replacement
new_nav = '''<!-- NAVBAR -->
<nav class="navbar navbar-expand-lg fixed-top" id="mainNav">
    <div class="container">
        <a class="navbar-brand text-center" href="#inicio">
            <div class="brand-text-main">Natanael Castro</div>
            <div class="brand-text-sub">Advocacia</div>
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            <i class="fa fa-bars" style="color: var(--gold); font-size: 1.5rem;"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav ms-auto py-4 py-lg-0 align-items-center">
                <li class="nav-item"><a class="nav-link" href="#inicio">Início (A)</a></li>
                <li class="nav-item"><a class="nav-link" href="#inicio-b">Início (B)</a></li>
                <li class="nav-item"><a class="nav-link" href="#especialidades">Especialidades</a></li>
                <li class="nav-item"><a class="nav-link" href="#about">Sobre</a></li>
                <li class="nav-item"><a class="nav-link" href="#galeria">Galeria</a></li>
                <li class="nav-item"><a class="nav-link" href="#duvidas">Dúvidas</a></li>
                <li class="nav-item ms-lg-3"><a class="nav-link btn btn-nav-outline" href="#contact">Fale Conosco</a></li>
            </ul>
        </div>
    </div>
</nav>'''

html = re.sub(r'<nav.*?</nav>', new_nav, html, flags=re.DOTALL)

# Hero A Replacement
new_hero_a = '''
    <!-- VERSÃO A: LUXURY MINIMAL DARK -->
    <header class="hero-a" id="inicio">
        <div class="container hero-a-content">
            <div class="row align-items-center gx-lg-5">
                <div class="col-lg-6 mb-5 mb-lg-0">
                    <span class="gold-line mb-3"></span>
                    <h1 class="hero-a-title font-serif">
                        Defesa Estratégica &<br> <span class="gold-text">Soluções Premium</span>
                    </h1>
                    <p class="hero-a-subtitle mb-5">
                        Assessoria jurídica boutique focada na excelência, discrição e resultados excepcionais para clientes exigentes em todo o Brasil.
                    </p>
                    <div class="d-flex gap-3">
                        <a class="btn btn-gold" href="#contact">Consultoria Exclusiva</a>
                    </div>
                    
                    <div class="trust-indicators">
                        <div class="trust-item"><i class="fa fa-balance-scale gold-text me-2"></i> Alta Complexidade</div>
                        <div class="trust-item"><i class="fa fa-shield gold-text me-2"></i> Atuação Nacional</div>
                    </div>
                </div>
                
                <div class="col-lg-6">
                    <div class="hero-a-video-wrapper shadow-lg">
                        <video id="videoA" loop muted playsinline poster="images/justica.jpg">
                            <source src="videos/video_bg.mp4" type="video/mp4">
                        </video>
                        <div class="controls-overlay">
                            <button onclick="var v=document.getElementById('videoA'); if(v.paused)v.play(); else v.pause();"><i class="fa fa-play"></i></button>
                            <button onclick="var v=document.getElementById('videoA'); v.muted = !v.muted;"><i class="fa fa-volume-up"></i></button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>
'''

html = re.sub(r'<header id="inicio".*?</header>', new_hero_a, html, flags=re.DOTALL)

# Hero B Replacement
new_hero_b = '''
    <!-- VERSÃO B: EDITORIAL LUXURY / MAGAZINE -->
    <header class="hero-b" id="inicio-b">
        <div class="hero-b-bg-text">DEFESA</div>
        <div class="container hero-b-content">
            <div class="row align-items-center gx-lg-5">
                <div class="col-lg-5 mb-5 mb-lg-0 z-index-2">
                    <span class="hero-b-suptitle">Natanael Castro Advocacia</span>
                    <h1 class="hero-b-title font-serif">
                        A Nova<br>Referência em<br>Direito.
                    </h1>
                    <div class="gold-line mb-4"></div>
                    <p class="hero-b-text mb-5">
                        Estratégia jurídica desenhada sob medida. Aliamos profundo conhecimento técnico a uma visão arquitetônica de cada caso, garantindo precisão formidável.
                    </p>
                    <a class="btn btn-dark-outline" href="#contact">Descubra Nossa Atuação</a>
                </div>
                
                <div class="col-lg-7">
                    <div class="hero-b-video-wrapper">
                        <video id="videoB" loop muted playsinline poster="images/justica.jpg">
                            <source src="videos/video_bg.mp4" type="video/mp4">
                        </video>
                        <div class="controls-overlay">
                            <button onclick="var v=document.getElementById('videoB'); if(v.paused)v.play(); else v.pause();"><i class="fa fa-play"></i></button>
                            <button onclick="var v=document.getElementById('videoB'); v.muted = !v.muted;"><i class="fa fa-volume-up"></i></button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>
'''

html = re.sub(r'<header id="inicio-b".*?</header>', new_hero_b, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")
