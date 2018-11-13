## installation 
Для работы этих файлов нужны библиотеки face-recognition (https://github.com/ageitgey/face_recognition) и Pillow (https://pillow.readthedocs.io/en/5.3.x/installation.html)

Для установки Pillow нужно выполнить 
```bash
pip install Pillow
```

Для установки face-recognition на MacOS/Linux 
```bash
pip3 install face_recognition
```
А для устновки на Windows можно использоваить гайд: https://github.com/ageitgey/face_recognition/issues/175#issue-257710508

## Какие файлы есть в этом репозитории 
* face_detection.py
    Использование: 
```bash 
python3 face_detection.py image.jpg
```

* face_rec.py
    Запомнит все лица из папки known_images/ и попробует найти их в папке images/
    
    Использование 
```bash
python3 face_rec.py known_images/ images/
```

* georgia_bench.py и yale_bench.py
    
    Эти файлы покажут точность алгоритма на фото с известными лицами. При ошибочном распозновании в консоль будет выведено сообщение об этом, а в конце подсчитано количство правильных и неправильных ответов 
    
    Использование
```bash
python3 georgia_bench.py 
python3 yale_bench.py  
```

* form_json.py

    Размечает фотографии и формирует json файл faces.json
    
* mark_faces_from_json.py

    Считывает данные разметки из json файла (стандарно faces.json) и применяет их к фотографии (стандартно к 0 фотографии файла, но можно аргументом передать любую фотографию)
```bash
python3 mark_faces_from_json.py ./images/Robot_1.jpg
```
    