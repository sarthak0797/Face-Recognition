import cv2
import os

cam = cv2.VideoCapture('robin.mp4')
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

pic_path = './Test_pics'

Id=input('enter your id')
sampleNum=0
count = 0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x-10,y-10),(x+w+30,y+h+30),(255,0,0),2)
        
        sampleNum=sampleNum+1
        cv2.imwrite(os.path.join(pic_path, Id+ ".%d.jpg" % count), gray[y:y+h,x:x+w])
        count += 1

        cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cam.release()
cv2.destroyAllWindows()
