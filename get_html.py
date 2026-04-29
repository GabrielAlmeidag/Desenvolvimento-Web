with open('index_old.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
nav = re.search(r'<nav.*?</nav>', text, re.DOTALL)
if nav: print('NAVBAR OLD:', nav.group(0))

hero = re.search(r'<header.*?</header>', text, re.DOTALL)
if hero: print('HERO OLD:', hero.group(0))
