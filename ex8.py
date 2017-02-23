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

hpixels=[] # set up an empty list for us to save our pixels
spixels=[] # set up an empty list for us to save our pixels
vpixels=[] # set up an empty list for us to save our pixels

for filename in filelist:
   im=cv2.imread(filename)
   hsvim=cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
   pixel=hsvim[x,y] 
   vpixels.append(pixel[2]) # add pixel value to our list
   hpixels.append(pixel[0]) # add pixel hue to our list
   spixels.append(pixel[1]) # add pixel saturation to our list
   im[x-10:x+10,x-10:x+10]=[255,0,0] 
   small_im=cv2.resize(im,size)
   cv2.imshow('Plant Image',small_im)
   ch=cv2.waitKey(5) 

plt.ylim(0,255) 
#Plot hue in magenta "m"
plt.plot(hpixels,"m") 
#Plot saturation in yellow  "y"
plt.plot(spixels,"y") 
#Plot value in black "k" 
plt.plot(vpixels,"k") 
plt.show()
