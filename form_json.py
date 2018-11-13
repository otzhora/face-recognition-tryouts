import face_recognition
import glob
import time
import sys
import json

start_time = time.time()

if len(sys.argv) == 3:
    unknown_images_path = "./{}".format(sys.argv[2])
    known_images_path = "./{}".format(sys.argv[1])
else:
    unknown_images_path = "./images/"
    known_images_path = "./known_images/"


known_faces = {}
for filename in glob.glob(known_images_path + "*.jpg"):
    try:
        name = filename[filename.rfind('/') + 1: filename.rfind('.jpg')]
        image = face_recognition.load_image_file(filename)
        known_faces[name] = face_recognition.face_encodings(image)[0]

    except IndexError:
        print("something went wrong")


JSON = {}
for filename in glob.glob(unknown_images_path + "*.jpg"):
    im = face_recognition.load_image_file(filename)
    try:
        face_locations = face_recognition.face_locations(im)
        face_encodings = face_recognition.face_encodings(im, known_face_locations=face_locations)
    except IndexError:
        print('no face found on photo {}'.format(filename))
        continue

    file_faces = []
    for name in known_faces:
        # inc tolerance to get more photos w/ 2+ known faces on them
        res = face_recognition.compare_faces(face_encodings, known_faces[name], 0.6)
        if True in res:
            file_faces.append({name: face_locations[res.index(True)]})

    if file_faces:
        JSON[filename] = file_faces

print(time.time() - start_time)

with open('faces.json', 'w') as fp:
    json.dump(JSON, fp)
