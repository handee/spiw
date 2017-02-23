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
bpixels=[] # set up an empty list for us to save our pixels
gpixels=[] # set up an empty list for us to save our pixels

for filename in filelist:
   im=cv2.imread(filename)
   pixel=im[x,y] 
   rpixels.append(pixel[2]) # add pixel red to our list
   bpixels.append(pixel[0]) # add pixel blue to our list
   gpixels.append(pixel[1]) # add pixel green to our list
   im[x-10:x+10,x-10:x+10]=[255,0,0] 
   small_im=cv2.resize(im,size)
   cv2.imshow('Plant Image',small_im)
   ch=cv2.waitKey(5) 

plt.ylim(0,255)
plt.plot(rpixels,"r") 
# now plot the blue pixels bpixels against the numbers 0 to "count", 
# using blue lines "b", and the green pixels using green lines "g"
plt.plot(bpixels,"b") 
plt.plot(gpixels,"g") 
plt.show()
