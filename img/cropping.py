import os
import cv2 as cv

base_dir=r'/home/srishivanth/Desktop/OpenCV tutorial'
img_path=os.path.join(base_dir,'img','my_photo-1.jpg')

img=cv.imread(img_path)
cv.imshow('original image',img)

cropped_Array=img[68:488,71:472]
cv.imshow("cropped",cropped_Array)



cv.waitKey(0)

