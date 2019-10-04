# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 05:44:06 2019

@author: Rajat arya
"""

import numpy as np 
import cv2 
import matplotlib.pyplot as plt 
%matplotlib inline 
image = cv2.imread("index.png") 
rows,cols = image.shape[:2] 
#(col/2,rows/2) is the center of rotation for the image 
# M is the cordinates of the center 
M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1) 
dst = cv2.warpAffine(image,M,(cols,rows)) 
plt.imshow(dst)