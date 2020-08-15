#pip install pip install opencv-python 
import cv2
from random import randrange

#load some pretrained data on face frontals from open cv (haar cascade algotithm (git hub opencv the data ))
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#choose an image to detect faces
webcam = cv2.VideoCapture(0)

#iterate over frames
while True:

    #read current frame
    successful_frame_read, frame = webcam.read()


    #convert to greyscale
    greyscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect faces
    face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)

    #draw rectangle
    for (x , y, w, h) in face_coordinates:
        #(x , y, w, h)=face_coordinates[0]
        cv2.rectangle(frame ,(x, y), (x+w , y+h) , (randrange(256), randrange(256), randrange(256)), 5)
    
    #display
    cv2.imshow("sabya's Face detection app" ,frame)
    
    #one is added so that the frame change evry 1millisecond without key press
    key = cv2.waitKey(1)

    if key == 27: # exit on ESC
        break
#release video capture
webcam.release()


print("code completed")