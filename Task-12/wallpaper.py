from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import time
import os

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)

counter = 0

while True:
    img = Image.open("spider.jpg").copy()
    draw = ImageDraw.Draw(img)

    current_time = datetime.now().strftime("%H:%M:%S")
    draw.text((90, 80), current_time, fill=(128, 0, 0), font=font)

    # Alternate between two filenames so GNOME is forced to see a "new" path each time
    output_file = "output_a.png" if counter % 2 == 0 else "output_b.png"
    img.save(output_file)

    full_path = os.path.abspath(output_file)
    os.system(f'gsettings set org.gnome.desktop.background picture-uri "file://{full_path}"')
    os.system(f'gsettings set org.gnome.desktop.background picture-uri-dark "file://{full_path}"')

    print("Wallpaper updated:", current_time, "->", output_file)

    counter += 1
    time.sleep(1)
