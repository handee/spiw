import cv2
import sys

# create a window
cv2.namedWindow('Plant Image')

# read in one of our pictures
im=cv2.imread('images/207-02-13_15.07.43.png')

# put the picture in the window
cv2.imshow('Plant Image',im)

#wait 5 seconds
ch=cv2.waitKey(5000)
    
