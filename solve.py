import cv2
import numpy as np
import glob
import re
from PIL import Image,ImageDraw

def get_number(filename):
match = re.search(r'\d+',filename)
return int(match.group())

def find_dot(filename):
img = cv2.imread(filename)
white = np.array([255,255,255])
not_white = np.any(img !=white, axis=2)
coords = np.argwhere(not_white)

if len(coords) == 0:
return None

center = coords.mean(axis=0)
row, col = int(center[0]), int(center[1])

b,g,r = img[row,col]
color_rgb = (int(r), int(g), int(b))

position = (col, row)
return position, color_rgb

image_files = glob.glob("Layer *.png")
sorted_files = sorted(image_files, key=get_number )

results = []
for filename in sorted_files:
dot = find_dot(filename)
results.append(dot)

print("total images processed:", len(results))
print("number of blank images:", results.count(None))

