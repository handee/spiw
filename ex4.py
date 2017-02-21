import cv2
import sys
import glob #import a library which lets us list files

cv2.namedWindow('Plant Image')
subdir="images/"
filelist=glob.glob(subdir+"*.png")
filelist.sort()
# we use the same size every time so that does not have to be 
# in the loop
size=(640,480)

for filename in filelist:
   print (filename)
# if we indent (put some spaces in front of) the lines, they become
# part of the loop and get done for every filename
# by doing this we make our own "video player"
   im=cv2.imread(filename)
   small_im=cv2.resize(im,size)
   cv2.imshow('Plant Image',small_im)
# If we wait 0.1 seconds it won't take so long
   ch=cv2.waitKey(100)
    
