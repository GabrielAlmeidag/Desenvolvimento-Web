import re
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

hero_b = re.search(r'<header id="inicio-b".*?</header>', text, re.DOTALL)

if hero_b:
    b_content = hero_b.group(0)
    
    # 1. Update text wrapper
    b_content = b_content.replace(
        '<div class="hero-badge',
        '<div style="background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(15px); padding: 45px; border-radius: 12px; box-shadow: 0 15px 40px rgba(0,0,0,0.08); border: 1px solid rgba(255,255,255,0.5);">\n                        <div class="hero-badge'
    )
    b_content = b_content.replace(
        '                            Nossas Áreas\n                        </a>\n                    </div>\n                </div>',
        '                            Nossas Áreas\n                        </a>\n                    </div>\n                    </div>\n                </div>'
    )
    
    # Remove bg-light from hero-section if it's there
    b_content = b_content.replace('class="hero-section bg-light position-', 'class="hero-section position-')
    b_content = b_content.replace('background: rgba(255,255,255,0.02)', 'background: rgba(255,255,255,0.7)')
    
    # Replace in file
    text = text.replace(hero_b.group(0), b_content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Updated Versao B with blur block.')