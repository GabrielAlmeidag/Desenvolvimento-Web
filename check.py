import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

nav = re.search(r'<nav.*?</nav>', text, re.DOTALL)
print('Nav:', bool(nav))

style = re.search(r'<style>.*?</style>', text, re.DOTALL)
print('Style:', bool(style))

heroA = re.search(r'<header id="inicio".*?</header>', text, re.DOTALL)
print('HeroA:', bool(heroA))

heroB = re.search(r'<header id="inicio-b".*?</header>', text, re.DOTALL)
print('HeroB:', bool(heroB))

