import sys, re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the test sections TESTE A and TESTE B completely
content = re.sub(
    r'<!-- ============================================== -->\s*<!-- SEÇÃO TESTE A.*?<!-- SEÇÃO TESTE B.*?</section>', 
    '', 
    content, 
    flags=re.DOTALL
)

# 2. Fix the commented out especialidades block (make it visible again)
content = content.replace('<!-- Áreas de Especialidades (OCULTADO TEMPORARIAMENTE PARA TESTE A/B)\n', '<!-- Áreas de Especialidades -->\n')
content = content.replace('<!-- Áreas de Especialidades (OCULTADO TEMPORARIAMENTE PARA TESTE A/B)\r\n', '<!-- Áreas de Especialidades -->\r\n')
# Need to remote the trailing '-->' of the comment
content = content.replace('            </div>\n        </div>\n    </section>\n    -->', '            </div>\n        </div>\n    </section>')
content = content.replace('            </div>\r\n        </div>\r\n    </section>\r\n    -->', '            </div>\r\n        </div>\r\n    </section>')

# 3. Handle Hero A and B
hero_match = re.search(r'<header id="inicio".*?</header>', content, re.DOTALL)
if hero_match:
    hero_original = hero_match.group(0)
    
    # Hero A: Dark (images/justica.jpg as background) + navy overlay
    hero_a = hero_original
    hero_a = re.sub(
        r'style="min-height: 100vh; background: #080c16; padding-top: 100px;"', 
        r'style="min-height: 100vh; background: url(\'images/justica.jpg\') no-repeat center center; background-size: cover; padding-top: 100px;"', 
        hero_a
    )
    
    # Add dark navy overlay 
    # Find position of background layers
    overlay_escuro = '<div class="position-absolute top-0 start-0 w-100 h-100" style="background: rgba(8, 12, 28, 0.88); z-index: 1;"></div>'
    
    # We replace the first comment inside hero to insert the overlay
    hero_a = hero_a.replace('<!-- Fundo Escuro com Detalhes Ouro Sutis -->', '<!-- Overlay Azul Marinho Escuro -->\n        ' + overlay_escuro + '\n\n        <!-- Fundo Escuro com Detalhes Ouro Sutis -->')
    
    # Hero B: Light (images/justica.jpg as background) + light overlay
    hero_b = hero_original.replace('id="inicio"', 'id="inicio-b"')
    hero_b = re.sub(
        r'style="min-height: 100vh; background: #080c16; padding-top: 100px;"', 
        r'style="min-height: 100vh; background: url(\'images/justica.jpg\') no-repeat center center; background-size: cover; padding-top: 100px;"', 
        hero_b
    )
    
    overlay_claro = '<div class="position-absolute top-0 start-0 w-100 h-100" style="background: rgba(255, 255, 255, 0.90); z-index: 1;"></div>'
    hero_b = hero_b.replace('<!-- Fundo Escuro com Detalhes Ouro Sutis -->', '<!-- Overlay Claro Suave -->\n        ' + overlay_claro + '\n\n        <!-- Fundo Escuro com Detalhes Ouro Sutis -->')

    # Color changes for B
    hero_b = hero_b.replace('text-white', 'text-dark')
    hero_b = hero_b.replace('color: rgba(255,255,255,0.8)', 'color: rgba(0,0,0,0.7)')
    hero_b = hero_b.replace('border-color: rgba(255,255,255,0.15)', 'border-color: rgba(0,0,0,0.15)')
    hero_b = hero_b.replace('background: rgba(255,255,255,0.05)', 'background: rgba(0,0,0,0.05)')
    # Custom light theme adjustments
    hero_b = hero_b.replace('btn-outline-light', 'btn-outline-dark')
    hero_b = hero_b.replace('text-shadow: 0 4px 15px rgba(0,0,0,0.8);', 'text-shadow: 0 4px 15px rgba(0,0,0,0.3);')
    hero_b = hero_b.replace('class="hero-section', 'class="hero-section bg-light')

    # Replace the old hero with both new versions
    new_hero = f"<!-- ============================= -->\n    <!-- VERSÃO A - HERO ESCURO -->\n    <!-- ============================= -->\n    {hero_a}\n\n    <!-- ============================= -->\n    <!-- VERSÃO B - HERO CLARO -->\n    <!-- ============================= -->\n    {hero_b}"
    
    content = content.replace(hero_original, new_hero)

# 4. Scrollspy fixes. 
# Make sure Início active bug is fixed.
content = content.replace('class="nav-link active" href="#inicio"', 'class="nav-link" href="#inicio"')
# Change data-bs-target if needed, scrollspy root margin
# Ensure it looks at #mainNav or id of the Navbar
# Make sure body has standard scrollspy
content = re.sub(
    r'<body.*?>',
    '<body data-bs-spy="scroll" data-bs-target="#mainNav" data-bs-root-margin="0px 0px -40%" data-bs-smooth-scroll="true">',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Transformation successful.")