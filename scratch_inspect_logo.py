import os
from PIL import Image

logo_path = r"c:\Users\upscv\OneDrive\Desktop\borokai\New folder (2)\borokai logo.png"
if os.path.exists(logo_path):
    with Image.open(logo_path) as img:
        print(f"Logo Size: {img.size}")
        print(f"Format: {img.format}")
else:
    print("Logo file not found")
