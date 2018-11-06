Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ##  drawing on a image

import cv2
import numpy as np

img = cv2.imread('C:\\project\\4.1.02.tiff',1)

#              start    end       b,g,r         pixel no.
cv2.line(img, (0,0) , (50,75) , (255,255,255) , 5)
cv2.rectangle(img , (20,20) , (100,150) , (0,255,0) , 5)
cv2.circle(img , (40,50) , 30 , (255,0,0), -2)            

cv2.imshow('image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
