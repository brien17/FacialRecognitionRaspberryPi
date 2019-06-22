# PersonalProject
This repository is for a personal project completed for my COP 2001 Programing methodology course. The goal of this project was to build a system that could run on the raspberry pi that could detect and recognize faces from a live video feed. More information about the project can be found in the problem statement file in this repository.

This project was made with help from this tutorial: https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826. 

# Timelog
## Week 1:
### 4 hours
### Accomplished
Installed rapbian on a micro sd

Updated the default python install on the pi

Created a virtual environment for python

Installed numpy on the pi

Downloaded and compiled opencv

### Learned
How to set up a new pi

How to create a python virtual environment on the pi

How to compile software on the pi

## Week 2:
### 5 hours
### Accomplished
Set up pi camera to work with open cv

Got open cv to be able to stream video from the pi camera

Configured open cv to be able to detect faces in the live video feed

Got open cv draw boxes in the video feed over where it found faces in real time

### Learned
How to configure open cv with a camera

How to use pretrained models in open cv to perform complex tasks

How to train new open cv models

How to make open cv draw things in the video feed

## Week 3:
### 3 hours
### Accomplished
Got open cv to be able to collect a data sample from the faces it sees in the video feed and save them as images

Trained a model based on the images collected by open cv

Ran the trained model and used it to recognize faces in the video feed

### Learned
How to use open cv to collect data about specific things when they are detected in the video feed

How to train a model on open cv to be able to detect specific things in the video feed

How to run a trained model for detection with a video feed

## Week 4:
### 2 hours
### Accomplished 
Wired led lights on a breadboard connected to the pi

Configured the lights to light up when they see a face

Made it so that the light that lights up coresponds with who the pi sees in the video

### Learned
How to set up wires with the pi on a breadboard

How to control led lights with python

## Week 5:
### 4 hours
### Accomplished
Installed flask-ask and ngrok to the raspberry pi

Created an amazon developer account

Created an alexa intent for my program

Got the pi and the alexa to do basic communication tasks

### Learned 
How to work with flask-ask

How to use the amazon developer tools to create an alexa intent

How to use ngrok 

## Week 6:
### 4 hours
### Accomplished
Created a flask-ask python file to run as the backend of my alexa function

Integrated facial recognition into the flask-ask function

Optimized the function to be able to run fast enough to seem responsive over alexa (most of the time)

### Learned
How to create a functional program with alexa and flask-ask

How to optimize code that is used with alexa
