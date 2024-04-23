import cv2 as cv
import os

webcam=cv.VideoCapture(0)
base_dir=r'/home/srishivanth/Desktop/OpenCV tutorial'
img_path=os.path.join(base_dir,'img','my_pic.jpeg')


while True:
    recv,frame=webcam.read()
    cv.imshow("fram",frame)
    key = cv.waitKey(1) & 0xFF
    if key == ord('p'):
        cv.imwrite(img_path, frame)
    elif key == ord('1'):
        break

webcam.release()
cv.destroyAllWindows()

