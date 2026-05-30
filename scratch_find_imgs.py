import re

file_path = r"c:\Users\upscv\OneDrive\Desktop\borokai\New folder (2)\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's find all img tags and extract src and alt attributes
img_tags = re.findall(r"<img\s+[^>]*>", content)
for i, tag in enumerate(img_tags, 1):
    src_match = re.search(r"src=[\'\"]([^\'\"]+)[\'\"]", tag)
    alt_match = re.search(r"alt=[\'\"]([^\'\"]+)[\'\"]", tag)
    src = src_match.group(1) if src_match else "No src"
    alt = alt_match.group(1) if alt_match else "No alt"
    print(f"{i:02d}: {src} | {alt}")
