import numpy as np    #modified code for faces and eyes detection
import cv2
face_cascade = cv2.CascadeClassifier("C:\\Users\\Rajat arya\\Desktop\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("C:\\Users\\Rajat arya\\Desktop\\haarcascade_eye.xml")
 
img = cv2.imread("image.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),10)
     roi_gray = gray[y:y+h, x:x+w]
     roi_color = img[y:y+h, x:x+w]
     eyes = eye_cascade.detectMultiScale(roi_gray)
     for (ex,ey,ew,eh) in eyes:
         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),5)
resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
        
cv2.imshow("image",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
