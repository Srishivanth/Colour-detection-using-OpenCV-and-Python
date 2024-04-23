import os
import cv2 as cv

base_dir=r'/home/srishivanth/Desktop/OpenCV tutorial'
img_path=os.path.join(base_dir,'img','my_photo-1.jpg')

img=cv.imread(img_path)

resized_img =cv.resize(img,(1500,1000))

print(resized_img.shape)

cv.imshow('im',resized_img)
cv.imshow('well',img)

cv.waitKey(0)
cv.destroyAllWindows()