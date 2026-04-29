with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
a = re.search(r'<header id="inicio".*?</header>', text, re.DOTALL)
if a: print('Hero A:\n', a.group(0)[:1500])

b = re.search(r'<header id="inicio-b".*?</header>', text, re.DOTALL)
if b: print('Hero B:\n', b.group(0)[:1500])
