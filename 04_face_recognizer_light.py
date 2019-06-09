import cv2
import numpy as np
import os 
import RPi.GPIO as GPIO
import time
# Settings for the led
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
# Creating a recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
# Telling the recognizer to use data from the previously trained model
recognizer.read('trainer/trainer.yml')
# Setting the path for the facial detector
cascadePath = "Cascades/haarcascade_frontalface_default.xml"
# Initializing the facial detector
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX
# Initialize id
id = 0
# names related to ids
names = ['Cameron','Cameron','Cameron', 'Val'] 
# Initialize and start realtime video capture
cap = cv2.VideoCapture(0)
cap.set(3, 640) # set video widht
cap.set(4, 480) # set video height
# Define min window size to be recognized as a face
minW = 0.1*cap.get(3)
minH = 0.1*cap.get(4)
# Setting up a variable to tell if there is a face in frame for the light
face = True

while True:
    ret, img =cap.read()
    img = cv2.flip(img, -1) # Flip vertically
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        # Lower confidence is more sure
        if (confidence < 100):
            id = names[id]
            face = True
            confidence = "  {0}%".format(round(100 - confidence))
            if id in [names[0],names[1],names[2]]:
                GPIO.output(18,GPIO.HIGH)   
            if id in [names[3]]:
                GPIO.output(23,GPIO.HIGH)
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
    if face == False:
       GPIO.output(18,GPIO.LOW)
       GPIO.output(23,GPIO.LOW)
    # Resting the face to false for the next loop
    face = False
    # Showing the image
    cv2.imshow('camera',img)
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cap.release()
cv2.destroyAllWindows()
