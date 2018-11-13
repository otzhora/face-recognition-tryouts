import face_recognition
import glob
import time

start_time = time.time()

unknown_images_path = "./yalefaces/unknown_persons/"
known_images_path = "./yalefaces/known_persons/"


known_faces = {}
for filename in glob.glob(known_images_path+"*.*"):
    try:
        name = filename[filename.rfind('/') + 1: filename.rfind('.')]
        image = face_recognition.load_image_file(filename)
        known_faces[name] = face_recognition.face_encodings(image)[0]

    except IndexError:
        print("something went wrong")

correct = 0
incorrect = 0
for filename in glob.glob(unknown_images_path+"*.*"):
    im = face_recognition.load_image_file(filename)
    try:
        face_encodings = face_recognition.face_encodings(im)
    except IndexError:
        print('no face found on photo {}'.format(filename))
        continue

    for name in known_faces:
        res = face_recognition.compare_faces(face_encodings, known_faces[name], 0.55)
        if True in res:
            ans_name = filename[filename.rfind('/') + 1: filename.rfind('.')]
            if ans_name != name:
                print("err. Found {} on {}".format(name, filename))
                incorrect += 1
            else:
                correct += 1

print(time.time() - start_time)
print("corr: {}".format(correct))
print("wrong: {}".format(incorrect))
