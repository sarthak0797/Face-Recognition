# Face-Recognition

What is face recognition? Or what is recognition? When you look at an apple fruit, your mind immediately tells you that this is an apple fruit. This process, your mind telling you that this is an apple fruit is recognition in simple words. So what is face recognition then? <br/>
It is quite simple and intuitive. Take a real life example, when you meet someone first time in your life you don't recognize him, right? While he talks or shakes hands with you, you look at his face, eyes, nose, mouth, color and overall look. This is your mind learning or training for the face recognition of that person by gathering face data. Then he tells you that his name is David. At this point your mind knows that the face data it just learned belongs to David. Now your mind is trained and ready to do face recognition on David's face. Next time when you will see David or his face in a picture you will immediately recognize him. This is how face recognition work.

Our Projects also works in the same manner.It's split into three major components:
#### 1) Camfeed
#### 2) Detector
#### 3) Recogniser

### 1) Camfeed
In this module we feed some test data to machine with two major components Photo/Video of a person and Id of that particular person.Then our machine breaks down that video into photos and extracts just the face of that person and saves them with the particular Id given by the user.

### 2) Detector
In this module our machine picks up each test photo and trains itself to recognize that person's face with the particular Id given by the user in previous module.Once the classifier/machine gets trained to identify the person's face, it starts recognising him with that particular Id, whenever he's seen somewhere.

### 3) Recogniser
This is the last module of our program, in this phase we our program starts interacting with the real world.As soon as our testing get's completed we can run this module to check whether or not our machine is working properly or now. We can give live feed from our webcam or we can give feed via video to check is it is identifying correctly or not.

After recognising any particular person our program also checks for any record of that person which are stored in the folder Crime_Record, if it matches a person with the same id as in the records, it will send the record of that person to any particular mail id which user has provided.

## Prerequisite
1) OpenCv
2) Python3
3) Numpy
4) Pillow

## Recogniser Used

We have used :

### Local Binary Patterns Histograms (LBPH) Face Recogniser

We know that Eigenfaces and Fisherfaces are both affected by light and in real life we can't guarantee perfect light conditions. LBPH face recognizer is an improvement to overcome this drawback.

Idea is to not look at the image as a whole instead find the local features of an image. LBPH alogrithm try to find the local structure of an image and it does that by comparing each pixel with its neighboring pixels.

Take a 3x3 window and move it one image, at each move (each local part of an image), compare the pixel at the center with its neighbor pixels. The neighbors with intensity value less than or equal to center pixel are denoted by 1 and others by 0. Then you read these 0/1 values under 3x3 window in a clockwise order and you will have a binary pattern like 11100011 and this pattern is local to some area of the image. You do this on whole image and you will have a list of local binary patterns.

## How to run the code

1) Download or Clone the repository
2) Download all the prerequisites
3) Store the Videos in the test_videos folder
4) After storing the Videos in the test folder open the module named camfeed.py and change the name of "robin.mp4" (in line number 4) to the name by which you have stored the video. Repeat the process until you have fed all this test videos one by one.
###### Note - Always assign numerical values to the id's
5) After feeding all the test videos run the module named detector.py so that you train the classifier to identify all the people whose samples you haven given to the previous module.
###### Note - You only need to run modules camfeed.py and detector.py once,when you have to train the classifier to identify any new person.
6) Once you train the classifier you just need to run the module recogniser.py to finally give you the real life implementation and identification of the people for whom you have trained the machine, if it matches the person with records stored it will send the record to the mail id you would have given.

## Applications

Facial Recognition can be used in multiple places and ways, however, our main focus here was to use it for these two purposes. <br/>

1) You can train the machine to recignise particular criminals who are on a run from police and whenever any camera spots them it will send a detailed location and record of that person to the police or whose mail id is given to the machine. <br/>
2) We can also use it to find the children who have lost their way to home, all we need to do is feed their video/image to the machine and train it to recognise him/her and wherever any camera spots them it will send their location to the concerned authority.

## End Notes

Although LBPH face recognizer is good but there are even better ways to perform face recognition like using Histogram of Oriented Gradients (HOGs) and Neural Networks. So the more advanced face recognition algorithms are now a days implemented using a combination of OpenCV and Machine learning.

This project is in joint contribution of @sachin-bisht 
