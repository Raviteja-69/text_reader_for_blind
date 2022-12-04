# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 22:03:31 2022

@author: Raviteja Sandu
"""
#importing required packages
#for capturing image
import cv2
#convert image to text
import pytesseract
#convert text to speech
import pyttsx3
#adds image processing capabilities
from PIL import Image


#initializes the pyttsx3 package
engine = pyttsx3.init()
#set output audio speed
engine.setProperty("rate", 200)
#reads the given string
engine.say("I am ready to read. place the text under the camera.")
engine.runAndWait()

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
while True:
    try:
        check, frame = webcam.read()
        print(check) #prints true as long as the webcam is running
        print(frame) #prints matrix values of each framecd 
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break

# opening an image from the source path
img = Image.open('saved_img.jpg')
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
#prints the text extracted from the image
print(result)	
engine.setProperty("rate", 170)
engine.say(result) 
engine.runAndWait()
engine.setProperty("rate", 200)
engine.say("task completed sir")
engine.runAndWait()

