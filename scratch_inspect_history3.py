with open(r"c:\Users\upscv\OneDrive\Desktop\borokai\New folder (3)\index.html", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find('id="history"')
if idx != -1:
    print("FOUND id='history' in New folder (3)\\index.html:")
    print(content[idx:idx+3500])
