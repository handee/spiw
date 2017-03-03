import cv2
import sys
import glob #import a library which lets us list files

cv2.namedWindow('Plant Image')
subdir="images/"
filelist=glob.glob(subdir+"*.png")
filelist.sort()
size=(640,480)

# Choose x and y so that the image at this location is a bit 
# of white background
x=330
y=330

for filename in filelist:
   im=cv2.imread(filename)
   pixel=im[y,x] # find the value of the image at x,y
   print (pixel) # print out what this pixel value is
   im[y-10:y+10,x-10:x+10]=[255,0,0] # set that pixel value to be bright 
               # blue so you can see where it is in the image
   small_im=cv2.resize(im,size)
   cv2.imshow('Plant Image',small_im)
   ch=cv2.waitKey(100)
    
