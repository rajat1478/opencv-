# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 05:44:06 2019

@author: Rajat arya
"""

import cv2 
import numpy as np 
import matplotlib.pyplot as plt                        
#print image
img=cv2.imread("index.png")
plt.imshow(img)                                                     ## opencv stores BGR image by default
plt.show()

#printing color image of an image
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img2)                                    ## original image               ## Convert BGR to RGB image
plt.show()
#printing hsv image of an image
hsv_image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)                   ## Convert BGR to HSV image 
plt.imshow(hsv_image)
plt.show()