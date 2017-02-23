import cv2
import sys
import glob 
import numpy as np #lets us manipulate numbers
import matplotlib.pyplot as plt #lets us draw graphs

cv2.namedWindow('Plant Image')
subdir="images/"
filelist=glob.glob(subdir+"*.png")
filelist.sort()
size=(640,480)

x=330
y=330

rpixels=[] # set up an empty list for us to save our pixels

for filename in filelist:
   im=cv2.imread(filename)
   pixel=im[x,y] 
   rpixels.append(pixel[2]) # add pixel red to our list
   im[x-10:x+10,x-10:x+10]=[255,0,0] 
   small_im=cv2.resize(im,size)
   cv2.imshow('Plant Image',small_im)
   ch=cv2.waitKey(5) #make this quicker by making the wait shorter

plt.ylim(0,255) # set plot limits of the y axis to be from 0 to 255
# now plot the red pixels rpixels against the numbers 0 to "count", 
# using red lines "r"
plt.plot(rpixels,"r") 
plt.show()
