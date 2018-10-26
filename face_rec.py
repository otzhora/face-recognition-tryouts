import face_recognition
import glob
import time

start_time = time.time()

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


for filename in glob.glob(unknown_images_path + "*.jpg"):
    im = face_recognition.load_image_file(filename)
    try:
        face_encodings = face_recognition.face_encodings(im)
    except IndexError:
        print('no face found on photo {}'.format(filename))
        continue

    for name in known_faces:
        res = face_recognition.compare_faces(face_encodings, known_faces[name])
        if True in res:
            print("Ooh its {} face in {}".format(name, filename))

print(time.time() - start_time)