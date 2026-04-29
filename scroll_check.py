with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()
import re
print("BODY:", re.search(r'<body.*?>', text).group(0))
nav = re.search(r'<nav.*?</nav>', text, re.DOTALL).group(0)
links = re.findall(r'href="#(.*?)"', nav)
for link in set(links):
    print("Exists:", link, text.find('id="' + link + '"') > -1)
