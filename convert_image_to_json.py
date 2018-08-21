import cv2
import numpy as np
import json
import sys

# load image file as array
image_file_name = sys.argv[1]
img = cv2.imread(image_file_name)

# print dimensions of image pixel array
# ex ouput. (1200, 1478, 3)
# image height, width, number of colors (rgb)
# each pixel represented by a rgb array, [255, 255, 255]
print(img.shape)

# flatten multidimensional matrix to 1d vector
values = img.flatten().tolist()
d = {
  "values": values,
  "dimensions": img.shape,
  "file_name": image_file_name
}
with open(image_file_name + '.json', 'w') as outfile:
    json.dump(d, outfile)

