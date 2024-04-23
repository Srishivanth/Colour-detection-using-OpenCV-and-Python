import os
import cv2 as cv
import numpy as np

base_dir=r'/home/srishivanth/Desktop/OpenCV tutorial'
img_path=os.path.join(base_dir,'img','wₐₗₗₚₐₚₑᵣ (1).jpeg')

img=cv.imread(img_path)
new=cv.resize(img,(1300,720))

edge=cv.Canny(new,100,200)

edge_d=cv.dilate(edge,np.ones((5,5),dtype=np.int8))

edge_e=cv.erode(edge_d,np.ones((7,7),dtype=np.int8))

cv.imshow("img0",edge_d)
cv.imshow("img1",edge_e)


cv.waitKey(0)
cv.destroyAllWindows()