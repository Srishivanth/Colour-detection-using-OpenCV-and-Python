# import os
# import cv2 as cv

# base_dir=r'/home/srishivanth/Desktop/OpenCV tutorial'
# img_path=os.path.join(base_dir,'img','my_photo-1.jpg')

# img=cv.imread(img_path)

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 21,21)

# cv.imshow("original",thresh)
# cv.waitKey(0)


#THE BELOW SCRIPT IS NEARLY THE SAME AS ABOVE WHIVH WAS WRITTEN TO PRACTICE
import os
import cv2 as cv

base_dir=r'/home/srishivanth/Desktop/OpenCV tutorial'
img_path=os.path.join(base_dir,'img','★ one piece new opening_ (1074) (1).jpeg')

img=cv.imread(img_path)

new=cv.resize(img,(1080,720))
gray=cv.cvtColor(new,cv.COLOR_BGR2GRAY)

thresh=cv.adaptiveThreshold(gray,50,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,7,7)

cv.imshow('edited image',thresh)
cv.imshow('new',gray)
cv.waitKey(0)