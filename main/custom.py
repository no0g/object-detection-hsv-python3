#!/bin/env python
import cv2 
import numpy as np

# Get file 
def getImage(img):
    return cv2.imread(img)

# Take Red 
def custom(inputImg,low,up):
    while(1):
        img = getImage(inputImg)

        # Boundaries
        lower = np.array(low)
        upper = np.array(up)

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
    custom('../img/RGB.png')
