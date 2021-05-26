#!/bin/env python
import cv2 
import numpy as np

# Get file 
def getImage(img):
    return cv2.imread(img)

# Take Red 
def blue(inputImg):
    while(1):
        img = getImage(inputImg)
        hMin = 90
        sMin = 0 
        vMin = 0 
        
        hMax = 105
        sMax = 255
        vMax = 255
        # Boundaries
        lower = np.array([hMin,sMin,vMin])
        upper = np.array([hMax,sMax,vMax])

        # Convert to HSV

        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,lower,upper)
        result = cv2.bitwise_and(img,img,mask=mask)

        # Display 
        cv2.imshow('Original',img)
        cv2.imshow('Result',result)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    blue('../img/RGB.png')
