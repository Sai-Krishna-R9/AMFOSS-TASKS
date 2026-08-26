import cv2
import numpy as np
import glob
import re
from PIL import Image, ImageDraw

def get_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group())

def find_dot(filename):
    img = cv2.imread(filename)
    white = np.array([255, 255, 255])
    not_white = np.any(img != white, axis=2)
    coords = np.argwhere(not_white)

    if len(coords) == 0:
        return None

    center = coords.mean(axis=0)
    row, col = int(center[0]), int(center[1])

    b, g, r = img[row, col]
    color_rgb = (int(r), int(g), int(b))

    position = (col, row)
    return position, color_rgb

image_files = glob.glob("Layer *.png")
sorted_files = sorted(image_files, key=get_number)

results = []
for filename in sorted_files:
    dot = find_dot(filename)
    results.append(dot)

print("Total images processed:", len(results))
print("Number of blank images:", results.count(None))

canvas = Image.new("RGB" , (512,512), color=(255, 255, 255))
draw = ImageDraw.Draw(canvas)

for i in range(len(results) - 1):
    current = results[i]
    next_one = results[i + 1]

    if current is None or next_one is None:
        continue

    current_pos, current_color = current
    next_pos, next_color = next_one

    draw.line([current_pos, next_pos], fill=current_color, width=3)

canvas.save("revealed_message.png")
print("Saved revealed_message.png")
