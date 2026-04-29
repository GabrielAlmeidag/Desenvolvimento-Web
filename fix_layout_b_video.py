import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract inicio-b
match = re.search(r'<header id="inicio-b".*?</header>', html, re.DOTALL)
if match:
    old_b = match.group(0)
    
    new_b = '''<header id="inicio-b" class="hero-section position-relative overflow-hidden d-flex align-items-center" style="min-height: 100vh; background: url('images/justica.jpg') no-repeat center center; background-size: cover; background-attachment: fixed; padding-top: 100px; padding-bottom: 80px;">
        <!-- Overlay Claro Suave -->
        <div class="position-absolute top-0 start-0 w-100 h-100" style="background: rgba(255, 255, 255, 0.15); z-index: 1;"></div>

        <!-- Fundo Escuro com Detalhes Ouro Sutis (removido para deixar mais limpo ou apenas reter o suave) -->
        <div class="hero-background-layer position-absolute w-100 h-100" style="inset: 0; background: radial-gradient(circle at 80% 30%, rgba(212, 175, 55, 0.05) 0%, transparent 50%); pointer-events: none; z-index: 1;"></div>
        
        <div class="container-fluid px-4 px-xl-5 position-relative z-index-2 w-100">
            <div class="row align-items-center justify-content-center justify-content-xl-between gx-lg-5 h-100" style="max-width: 1400px; margin: 0 auto;">
                
                <!-- Texto (Esquerda) -->
                <div class="col-lg-6 col-xl-5 text-left mt-5 mt-lg-0 mb-5 mb-lg-0" data-aos="fade-up" data-aos-duration="1000">
                    <!-- Glassmorphism Card -->
                    <div class="hero-glass-card" style="background: rgba(255, 255, 255, 0.82); backdrop-filter: blur(8px); padding: 2.5rem; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.6); box-shadow: 0 15px 35px rgba(0,0,0,0.08); width: 100%; margin: 0 auto;">
                        
                        <div class="hero-badge d-inline-block px-3 py-1 mb-4" style="border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 50px; background: rgba(255,255,255,0.7); font-family: 'Lato', sans-serif; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; color: var(--gold); font-weight: 700;">
                            Escritório de Advocacia Especializada
                        </div>
                        
                        <h1 class="hero-title mb-4 text-dark" style="font-size: clamp(2.2rem, 3.5vw, 3rem); font-weight: 700; line-height: 1.15; letter-spacing: -0.5px;">
                            A EXCELÊNCIA NA DEFESA DOS <span style="color: var(--gold); display: block; margin-top: 5px;">SEUS DIREITOS.</span>
                        </h1>
                        
                        <blockquote class="premium-quote mb-5" style="border-left: 2px solid var(--gold); padding-left: 15px; font-family: 'Playfair Display', serif; font-style: italic; font-size: 1.05rem; color: rgba(0,0,0,0.8);">
                            "A injustiça num lugar qualquer é uma ameaça à justiça em todo o lugar."
                            <cite style="display: block; font-family: 'Lato', sans-serif; font-size: 0.85rem; font-style: normal; margin-top: 10px; color: var(--gold); text-transform: uppercase; letter-spacing: 1px; font-weight: 600;">— Martin Luther King</cite>
                        </blockquote>
                        
                        <div class="hero-buttons d-flex flex-wrap gap-3">
                            <a href="https://wa.me/5511944725587?text=Ol%C3%A1%20Dr.%20Natanael%2C%20gostaria%20de%20agendar%20uma%20avalia%C3%A7%C3%A3o%20do%20meu%20caso." target="_blank" class="btn btn-gold btn-lg px-4 d-flex align-items-center justify-content-center gap-2 shadow" style="border-radius: 6px; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; font-weight: 700; padding-top: 12px; padding-bottom: 12px; border: none; flex-grow: 1;">
                                <i class="fa-brands fa-whatsapp fs-5"></i> Agendar Avaliação
                            </a>
                            <a href="#especialidades" class="btn btn-outline-dark btn-lg px-4 d-flex align-items-center justify-content-center gap-2" style="border-radius: 6px; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; border-color: rgba(0,0,0,0.15); flex-grow: 1; font-weight: 600;">
                                Nossas Áreas
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Vídeo Integrado Premium (Direita) -->
                <div class="col-lg-6 col-xl-5 position-relative mt-5 mt-lg-0" data-aos="fade-left" data-aos-duration="1200" data-aos-delay="300">
                    <div class="hero-visual-composition position-relative mx-auto shadow-lg" style="max-width: 580px; border: 1px solid rgba(212, 175, 55, 0.4); border-radius: 16px; background: #000; overflow: hidden; box-shadow: 0 25px 50px rgba(0,0,0,0.4) !important;">
                        
                        <!-- Wrapper do Vídeo Visual Replica -->
                        <div class="ratio border-0 m-0 p-0" style="--bs-aspect-ratio: 125%; cursor: pointer;" id="videoWrapperB">
                            
                            <video id="heroVideoB" playsinline preload="metadata" muted loop autoplay style="width: 100%; height: 100%; object-fit: cover; object-position: center top; transition: opacity 0.5s ease;">
                                <source src="images/VIDEO1.mp4" type="video/mp4">
                            </video>

                            <!-- Controles Personalizados em Botões Flutuantes (Visual Only para não conflitar IDs) -->
                            <div class="video-custom-controls position-absolute w-100 h-100 top-0 start-0 pointer-events-none d-flex flex-column justify-content-end p-0" style="background: linear-gradient(to top, rgba(8,12,22,0.85) 0%, transparent 35%); opacity: 1; transition: opacity 0.3s ease; z-index: 2;">
                                
                                <div class="w-100 px-3 pb-3 pointer-events-auto" style="pointer-events: auto;">
                                    <div class="d-flex w-100 justify-content-between align-items-center mb-2 gap-2">
                                        <!-- Play / Pause -->
                                        <button class="btn rounded-circle text-white d-flex align-items-center justify-content-center video-control-btn shadow" title="Reproduzir/Pausar" onclick="let v=document.getElementById('heroVideoB'); if(v.paused){v.play();}else{v.pause();}">
                                            <i class="fa-solid fa-pause"></i>
                                        </button>
                                        
                                        <!-- Tempo de Progresso -->
                                        <span class="text-white" style="font-size:0.75rem; font-weight:600; opacity:0.8; font-family: 'Lato', sans-serif;">VISUALIZAÇÃO DE TESTE</span>
                                        <div class="video-progress-bar-container flex-grow-1 mx-2">
                                            <div class="video-progress-fill shadow" style="width: 50%;"></div>
                                        </div>

                                        <!-- Volume -->
                                        <button class="btn rounded-circle text-white d-flex align-items-center justify-content-center video-control-btn shadow" title="Mudo/Desmutar" onclick="let v=document.getElementById('heroVideoB'); v.muted=!v.muted;">
                                            <i class="fa-solid fa-volume-xmark"></i>
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>

            </div>
        </div>
    </header>'''

    html = html.replace(old_b, new_b)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("SUCCESS")
else:
    print("MATCH NOT FOUND")
