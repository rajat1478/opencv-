# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 05:44:06 2019

@author: Rajat arya
"""

import cv2
img=cv2.imread("C:\\Users\\Rajat arya\\Downloads\\index.png")
resize_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("image",resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()