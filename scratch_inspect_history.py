with open(r"c:\Users\upscv\OneDrive\Desktop\borokai\3 meher baba, help me.html", "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = re.findall(r"(<div[^>]*id=[\"\']history[\"\'][^>]*>.*?</div>\s*<!--\s*end\s*#history)", content, re.DOTALL | re.IGNORECASE)
if matches:
    print("MATCH IN 3 meher baba, help me.html:")
    print(matches[0][:2000])
else:
    # Just print the first 2000 characters after id="history"
    idx = content.find('id="history"')
    if idx != -1:
        print("FOUND id='history' in 3 meher baba, help me.html:")
        print(content[idx:idx+2000])

print("="*40)
with open(r"c:\Users\upscv\OneDrive\Desktop\borokai\New folder\6 meher baba.html", "r", encoding="utf-8") as f:
    content2 = f.read()

idx2 = content2.find('id="history"')
if idx2 != -1:
    print("FOUND id='history' in New folder\\6 meher baba.html:")
    print(content2[idx2:idx2+2000])
