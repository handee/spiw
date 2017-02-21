import cv2
import sys

# create a window
cv2.namedWindow('Plant Image')

# read in one of our pictures
im=cv2.imread('images/2017-02-13_12.27.34.png')

# put the picture in the window
cv2.imshow('Plant Image',small_im)

#wait 5 seconds
ch=cv2.waitKey(5000)
    
