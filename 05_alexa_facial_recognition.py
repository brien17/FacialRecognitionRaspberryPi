from flask import Flask
from flask_ask import Ask, statement, question
import cv2
import numpy as np
import os 

# creating the recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
# reading from the trained data from my previously created model
recognizer.read('trainer/trainer.yml')
# creating the face detector
cascadePath = "Cascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

app = Flask(__name__)
ask = Ask(app, '/')
# tells the user when the skill launches
@ask.launch
def launch():
    welcome_text = "Welcome to the computer vision skill. say look around and I will tell you who I see"  
    return statement(welcome_text)

# says the list of names of people in the room
@ask.intent('LookAround')
def facial_recog():
    # initialize id counter
    id = 0
    # names related to ids
    names = ['Cameron','Cameron','Cameron','Val','Val']    

    # Initialize and start realtime video capture
    cap = cv2.VideoCapture(0)
    cap.set(3, 640) # set video widht
    cap.set(4, 480) # set video height
    # Define min window size to be recognized as a face
    minW = 0.1*cap.get(3)
    minH = 0.1*cap.get(4)
    # initializing a list to store the names
    name_list = []
    # creating a variable to end the loop after 5 frames
    timer = 5
    # looping to view the video
    while timer > 0:
        ret, img =cap.read()
        img = cv2.flip(img, -1) # Flip vertically
        # using greyscale image
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # storing faces detected as faces
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )
        for(x,y,w,h) in faces:
            # using the recognizer to try to recognize the face
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            # Lower confidence is more sure
            if (confidence < 100):
                id = names[id]
                if id not in name_list:
                    name_list.append(id)
        timer -= 1
    #stopping capture
    cap.release()
    # initializing response text
    response_text = ""
    # for everyone who is seen in the video
    if len(name_list) == 0:
        response_text = "I don't see anyone"
    else:
        for person_num in range(len(name_list)):
            # if the person is the last one in the list
            if person_num == (len(name_list) - 1):
                person_name = name_list[person_num]
                response_text += "I see {}".format(person_name) 
            else:
                person_name = name_list[person_num]
                response_text += "I see {}".format(person_name) + " and "
    return statement(response_text) 
      
#shows us debugging things for flask 
if __name__ == '__main__':
    app.run(debug=True)

