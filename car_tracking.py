import cv2

img_file="cars.jpg"

classifier_file = "cars.xml"

img = cv2.imread(img_file)

car_tracker = cv2.CascadeClassifier(classifier_file)

black_n_white = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

cars = car_tracker.detectMultiScale(black_n_white)

for (x, y, w, h) in cars:
    cv2.rectangle(img, (x,y) , (x+w , y+h), (0,0,255) , 5)

cv2.imshow("sabya's car detector" ,img )

cv2.waitKey()

print("code completed")