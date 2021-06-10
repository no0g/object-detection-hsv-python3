#!/bin/env python3

import cv2
import numpy as np
from matplotlib import pyplot as plt


# get an image
img = cv2.imread("../img/480x360/8BIT/COLOR/img_480x360_3x8bit_RGB_color_bars_CMYKWRGB_100IRE.png")
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

## Converting to HSV
hsv_img = cv2.cvtColor(img_RGB, cv2.COLOR_RGB2HSV)

### Defining boundaries to mask original image
## Red
l_r = np.array([0,100,100])
u_r = np.array([0,255,255])
## Blue
l_b = np.array([91,100,100])
u_b = np.array([149,255,255])
## Green
l_g = np.array([31,100,100])
u_g = np.array([89,255,255])

## Mask image
mask_red = cv2.inRange(hsv_img,l_r,u_r)
mask_blue = cv2.inRange(hsv_img,l_b,u_b)
mask_green = cv2.inRange(hsv_img,l_g,u_g)

# Do bitwise AND operation to image
result_red = cv2.bitwise_and(img_RGB,img_RGB,mask=mask_red)
result_blue = cv2.bitwise_and(img_RGB,img_RGB,mask=mask_blue)
result_green = cv2.bitwise_and(img_RGB,img_RGB,mask=mask_green)

# Convert to RGB
result_red = cv2.cvtColor(result_red,cv2.COLOR_BGR2RGB)
result_green = cv2.cvtColor(result_green,cv2.COLOR_BGR2RGB)
result_blue = cv2.cvtColor(result_blue,cv2.COLOR_BGR2RGB)


print("'q' to close")

while True:
    #Display
    cv2.imshow('Original',img)
    cv2.imshow('Red',result_red)
    cv2.imshow('Green',result_green)
    cv2.imshow('Blue',result_blue)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

