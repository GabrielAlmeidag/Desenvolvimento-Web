import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

hero_a_match = re.search(r'<header class="hero-a" id="inicio">.*?</header>', html, re.DOTALL)
if hero_a_match:
    hero_a = hero_a_match.group(0)
    # create structurally identical hero-b
    hero_b = hero_a.replace('hero-a', 'hero-b').replace('id="inicio"', 'id="inicio-b"').replace('videoA', 'videoB')
    
    html = re.sub(r'<header class="hero-b" id="inicio-b">.*?</header>', hero_b, html, flags=re.DOTALL)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced Hero B with Hero A's structure.")
else:
    print('Hero A not found')
