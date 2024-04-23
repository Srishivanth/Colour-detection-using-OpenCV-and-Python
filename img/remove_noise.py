import cv2 as cv
import os

base_dir=r'/home/srishivanth/Desktop/OpenCV tutorial'
img_path=os.path.join(base_dir,'img','noised_img.png')

img=cv.imread(img_path)
cv.imshow("noise",img)

size=15
blurred=cv.medianBlur(img,size)
cv.imshow('blurred',blurred)

#If we want to save the noiseless image, then:
#cv.imwrite(os.path.join(base_dir,'img','noise_removed_img.png'),blurred)

cv.waitKey(0)