import os
import re

root_dir = r"c:\Users\upscv\OneDrive\Desktop\borokai"

for dirpath, dirnames, filenames in os.walk(root_dir):
    for f in filenames:
        if f.endswith(".html"):
            full_path = os.path.join(dirpath, f)
            try:
                with open(full_path, "r", encoding="utf-8") as file:
                    content = file.read()
                # Find occurrences of history page or organic
                if "history" in content.lower():
                    print(f"File: {full_path}")
                    # Find all sections or divs with id containing history or timeline
                    matches = re.findall(r"(<div[^>]*id=[\"\']history[\"\'][^>]*>.*?</div>)", content, re.DOTALL | re.IGNORECASE)
                    print(f"  Found history div matches: {len(matches)}")
                    # print snippet of first match if found
                    if matches:
                        print("  Snippet:", matches[0][:300])
            except Exception as e:
                print(f"Error reading {full_path}: {e}")
