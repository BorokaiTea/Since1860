import struct

logo_path = r"c:\Users\upscv\OneDrive\Desktop\borokai\New folder (2)\borokai logo.png"
try:
    with open(logo_path, "rb") as f:
        # Check signature
        sig = f.read(8)
        if sig == b"\x89PNG\r\n\x1a\n":
            # IHDR chunk starts at byte 12 (length + chunk type 'IHDR')
            f.seek(12)
            chunk_type = f.read(4)
            if chunk_type == b"IHDR":
                width, height = struct.unpack(">II", f.read(8))
                print(f"PNG Width: {width}, Height: {height}, Aspect: {width/height:.2f}")
            else:
                print("Could not find IHDR chunk")
        else:
            print("Not a valid PNG file")
except Exception as e:
    print(f"Error: {e}")
