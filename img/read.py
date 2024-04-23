import cv2 as cv
import os

#store image path to img variable
base_dir=r'/home/srishivanth/Desktop/OpenCV tutorial'
img_path=os.path.join(base_dir,'img','my_photo-1.jpg')
img=cv.imread(img_path)
#display image using gui
cv.imshow('PHOTO',img)

cv.imwrite(os.path.join(base_dir,'img','my_photo_001.jpg'),img)
cv.waitKey(0)