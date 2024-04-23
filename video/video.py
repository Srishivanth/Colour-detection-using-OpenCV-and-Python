import cv2 as cv
import os

#initalize the base directory and the vedio directory
base_dir=r'/home/srishivanth/Desktop/OpenCV tutorial'
vedio_path=os.path.join(base_dir,'video','whycon.mp4')


capture =cv.VideoCapture(vedio_path)

#visualize vedio

ret=True
while ret==True:
    ret,frame=capture.read()

    if ret:
        cv.imshow('frames',frame)
        cv.waitKey(30)

capture.release()
cv.destroyAllWindows()
