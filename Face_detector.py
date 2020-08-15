#pip install pip install opencv-python 
import cv2
from random import randrange

#load some pretrained data on face frontals from open cv (haar cascade algotithm (git hub opencv the data ))
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#choose an image to detect faces
#img = cv2.imread("sabya.jpg")
img = cv2.imread("group.jpg")

#convert to greyscale
greyscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)

#draw rectangle 2 is thickness 0 255 0 is colour code x y h w coordinates in terminal  (rgb)
#change 0 1245 in face coordinetes for single 1 diff rectangles around diff faces

#cv2.rectangle(img, (97, 96),(97+276 , 96+276), (0,255,0),2) 
for (x , y, w, h) in face_coordinates:

    #(x , y, w, h)=face_coordinates[0]
    cv2.rectangle(img ,(x, y), (x+w , y+h) , (randrange(128,256), randrange(128,256), randrange(128,256)), 5)




#location of the face box
#print(face_coordinates)

#display image
#cv2.imshow("sabya's Face detection app" ,img)
cv2.imshow("sabya's Face detection app" ,img)
# to wait or else window will close very fast
cv2.waitKey()





print("code completed")