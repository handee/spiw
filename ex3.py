import cv2
import sys
import glob #import a library which lets us list files

# create a window
cv2.namedWindow('Plant Image')


# Create a variable
subdir="images/"
# List the files in our directory 
filelist=glob.glob(subdir+"*.png")
# sort that list
filelist.sort()

# just to test it works, print that list out
# We are printing one at a time, using a "for loop"
# This sets the variable "filename" to be each 
# element in "filelist", one at a time
for filename in filelist:
   # this prints out the filename
   print (filename)

    

# read in one of our pictures
im=cv2.imread('images/2017-02-13_12.27.34.png')


# create a variable called size, with 640 and 480
size=(640,480)

# resize our image
small_im=cv2.resize(im,size)

# put the picture in the window
cv2.imshow('Plant Image',small_im)

#wait 5 seconds
ch=cv2.waitKey(5000)
    
