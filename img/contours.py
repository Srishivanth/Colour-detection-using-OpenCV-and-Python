import os
import cv2 as cv

base_dir=r'/home/srishivanth/Desktop/OpenCV tutorial'
img_path=os.path.join(base_dir,'img','led.jpg')

img=cv.imread(img_path)
new=cv.resize(img,(850,720))

grey=cv.cvtColor(new,cv.COLOR_BGR2GRAY)

ret,thresh= cv.threshold(grey,120,255,cv.THRESH_BINARY)

contours=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

for cnt in contours[0]:
    #print(cv.contourArea(cnt) )
    if cv.contourArea(cnt) > 200:
        cv.drawContours(new,cnt,-1,(0,255,0),2)
        (x,y),n=cv.minEnclosingCircle(cnt)
        x1,y1,w,h=cv.boundingRect(cnt)
        print(x,y)
        #cv.rectangle(new,(x1-5,y1-5),(x1+w+5,y1+h+5),(0,255,0),2)
        cv.circle(new,(int(x),int(y)),int(n),(0,255,0),2)


cv.imshow('thresh',new)
cv.waitKey(0)
cv.destroyAllWindows()