import cv2,os
import numpy as np
from PIL import Image
import sys

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    faceSamples=[]
    Ids=[]
    count = 1

    for imagePath in imagePaths:
        pilImage=Image.open(imagePath).convert('L')
        
        imageNp=np.array(pilImage,'uint8')
        
        Id = int(os.path.split(imagePath)[-1].split(".")[0])
        
        faces=detector.detectMultiScale(imageNp)

        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            Ids.append(Id)
    return faceSamples,Ids


faces,Ids = getImagesAndLabels('Test_pics')

recognizer.train(faces, np.array(Ids))
recognizer.save('./trainner.yml')