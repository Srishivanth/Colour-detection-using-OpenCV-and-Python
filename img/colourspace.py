import os
import cv2 as cv

base_dir=r'/home/srishivanth/Desktop/OpenCV tutorial'
img_path=os.path.join(base_dir,'img','★ one piece new opening_ (1074) (1).jpeg')

img=cv.imread(img_path)

new_img=cv.resize(img,(1080,720))
cv.imshow('original',new_img)

coloured_img=cv.cvtColor(new_img,cv.COLOR_BGR2HSV)
cv.imshow("coloured",coloured_img)

cv.waitKey(0)
cv.destroyAllWindows()