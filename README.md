These scripts utilize opencv to convert an image to an array of RGB values. After the conversion is complete, the RGB values and associated metadata are placed into a json file

Install opencv and additional dependencies via pip3

```
pip3.7 install opencv-python numpy six wheel
```

Run the `convert_image_to_json.py` script to convert image to an array, and place it into a JSON file

```
python convert_image_to_json.py <image_file>
```

The resulting json file will look like so

```
{
  "values": [255,255,255,...],
  "dimensions": "(1200, 1478, 3)",
  "file_name": "image_file_name.png"
}
```

Use the `load_image_from_json.py` script to convert the array of rgb values back into a image

```
python load_image_from_json.py <json_file>
```
