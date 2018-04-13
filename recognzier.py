import cv2
import numpy as np
import sys
import os 
import sms
import glob
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize

out_path_pic = '/home/humbel-fool/V_enviroment/Ongoing/Graphathon/Output_pic'
out_path_video = '/home/humbel-fool/V_enviroment/Ongoing/Graphathon/Output_video'
def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def make_video(outvid, images = None, fps=20, size=None,
               is_color=True, format="FMP4"):
 
    fourcc = VideoWriter_fourcc(*format)
    vid = None
    for image in images:
        if not os.path.exists(image):
            continue;

        img = imread(image)
        if vid is None:
            if size is None:
                size = img.shape[1], img.shape[0]
            vid = VideoWriter(outvid, fourcc, float(fps), size, is_color)
        if size[0] != img.shape[1] and size[1] != img.shape[0]:
            img = resize(img, size)
        vid.write(img)
    #vid.release()
    return vid

email = Id=input('enter the email to which result is to be mailed')

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('trainner.yml')

cascadePath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

cam = cv2.VideoCapture(0)

f = 0
f1 = 0
count = [0,0,0,0,0,0]
counts = 0

while True:
    ret, im =cam.read()

    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:

        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        imagePaths=[os.path.join('Crime_Record',f) for f in os.listdir('Crime_Record')]
        if(Id == 1 and confidence > 50):
            fname = 'Crime_Record/'+str(Id)+'.txt'
            count[1] += 1
            if fname in imagePaths and not f and count[1] > 20:
                ss = open(fname, 'r').read()
                sms.mail1(ss,email)
                f = 1
                Id = " Person Identified and a mail has been sent"
            else: 
                Id = "Sachin"
        elif(Id == 2 and confidence > 60):
            fname = 'Crime_Record/'+str(Id)+'.txt'
            count[2] += 1
            if fname in imagePaths and not f and count[2] > 20:
                ss = open(fname, 'r').read()
                sms.mail1(ss,email)
                f = 1
                Id = " Person Identified and a mail has been sent"
            else: 
                Id = "Sarthak"
        elif(Id == 3 and confidence > 60):
            fname = 'Crime_Record/'+str(Id)+'.txt'
            count[3] += 1
            if fname in imagePaths and not f and count[3] > 20:
                ss = open(fname, 'r').read()
                sms.mail1(ss,email)
                f = 1
                Id = " Person Identified and a mail has been sent"
            else: 
                Id = "Neeraj"
        elif(Id == 4 and confidence > 60):
            fname = 'Crime_Record/'+str(Id)+'.txt'
            count[4] += 1
            if fname in imagePaths and not f and count[4] > 20:
                ss = open(fname, 'r').read()
                sms.mail1(ss,email)
                f = 1
                Id = " Person Identified and a mail has been sent"
            else: 
                Id = "Prithvi"
        elif(Id == 5 and confidence > 60):
            fname = 'Crime_Record/'+str(Id)+'.txt'
            count[5] += 1
            if fname in imagePaths and not f and count[5] > 20:
                ss = open(fname, 'r').read()
                sms.mail1(ss,email)
                f = 1
                Id = " Person Identified and a mail has been sent"
            else: 
                Id = "Robin"
        else :  Id = "Unknown"

        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id), (x,y-40), font, 1, (255,255,255), 3)

    cv2.imshow('im',im)
    cv2.imwrite(os.path.join(out_path_pic, "%d.jpg" % counts), im)
    counts += 1
    if(f == 1 and not f1): 
        cv2.waitKey(10000)
        f1 = 1

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()

images = list(glob.iglob(os.path.join(out_path_pic, '*.*')))

images = sorted(images, key=lambda x: float(os.path.split(x)[1][:-3]))


outvid = os.path.join(out_path_video, "out1.mp4")
make_video(outvid, images, fps=20)

# Close all windows
cv2.destroyAllWindows()