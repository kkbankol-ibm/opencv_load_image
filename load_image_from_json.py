import cv2
import numpy as np
import json
import sys

# load image from JSON, write to 
json_file_name = sys.argv[1]
with open(json_file_name, 'r') as file:
    data = json.load(file)
img = np.array(data['values']).reshape( data['dimensions'] )
print("writing " + data['file_name'])
cv2.imwrite(data['file_name'], img)
