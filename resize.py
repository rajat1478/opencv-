# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 05:44:06 2019

@author: Rajat arya
"""

import cv2
img=cv2.imread("index.png",0)
print(img.shape)

resized_image = cv2.resize(img, (650,500))
cv2.imshow("image",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()