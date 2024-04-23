import cv2 as cv
import os

base_dir=r'/home/srishivanth/Desktop/OpenCV tutorial'
img_path=os.path.join(base_dir,'img','my_photo-1.jpg')

img=cv.imread(img_path)
cv.imshow('original',img)

gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

ret,thresh=cv.threshold(gray_img,80,255,cv.THRESH_BINARY)

blur=cv.blur(thresh,(5,5))
ret,threshh=cv.threshold(blur,80,255,cv.THRESH_BINARY)

cv.imshow("edited",threshh)
print(ret)
cv.waitKey(0) 