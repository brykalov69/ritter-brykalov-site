from PIL import Image

src = "public/images/hero-skaters-cutout.png"
dst = "public/images/hero-skaters-cutout.png"

img = Image.open(src).convert("RGBA")
bbox = img.getbbox()

if bbox:
    cropped = img.crop(bbox)
    cropped.save(dst)
    print("Trimmed:", bbox)
else:
    print("No visible pixels found")