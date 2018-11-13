import json
from PIL import Image, ImageDraw
import sys

filename = 'faces.json'
with open(filename, 'r') as fp:
    faces = json.load(fp)

if len(sys.argv) == 2:
    image_path = sys.argv[1]
else:
    image_path = list(faces)[0]

im = Image.open(image_path)
draw = ImageDraw.Draw(im)

faces_on_photo = faces[image_path]
for face_data in faces_on_photo:
    for name in face_data:
        (top, right, bottom, left) = face_data[name]

        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 5), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

del draw

im.show()