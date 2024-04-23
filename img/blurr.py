import cv2 as cv
import os

base_dir=r'/home/srishivanth/Desktop/OpenCV tutorial'
img_path=os.path.join(base_dir,'img','★ one piece new opening_ (1074) (1).jpeg')

img=cv.imread(img_path)
good=cv.resize(img,(1080,720))

#cv.waitKey(0)

#defining the proximity pixels to calculate the blur
size=9
blurred=cv.blur(good,(size,size))
gaussian=cv.GaussianBlur(good,(size,size),5)
median=cv.medianBlur(good,size)

cv.imshow('original',good)
cv.imshow('blurred',median)
cv.waitKey(0)
