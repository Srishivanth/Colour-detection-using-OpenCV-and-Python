import os
import cv2 as cv
import numpy as np

base_dir=r'/home/srishivanth/Desktop/OpenCV tutorial'
img_path=os.path.join(base_dir,'img','my_photo-1.jpg')

img=cv.imread(img_path)

#gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)

#ret,thresh=cv.threshold(gray,0,255,cv.THRESH_BINARY)

cv.line(img,(0,0),(640,480),(250,250,0),5)
cv.circle(img,(320,240),50,(0,0,255),-1)
cv.rectangle(img,(200,120),(400,480),(255,0,0),5)
cv.putText(img,'HELLO',(200,300), cv.FONT_HERSHEY_COMPLEX,3,(0,255,0),1)

cv.imshow('img',img)

cv.waitKey(0)
cv.destroyAllWindows()