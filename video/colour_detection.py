import cv2 as cv
import numpy as np
from PIL import Image

webcam = cv.VideoCapture(0)

yellow = [255,0,0]

class Object_Detect():

    def loop(self):
        while True:
            recv, frame = webcam.read()

            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

            lower_limit, upper_limit = self.colour_limits(colour=yellow)


            mask = cv.inRange(hsv, lower_limit, upper_limit)

            maskk=Image.fromarray(mask)
            bbox=maskk.getbbox()
            yellow_px=np.count_nonzero(mask)

            if bbox :
                if yellow_px>200:
                    x1,y1,x2,y2=bbox
                    frame=cv.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)
                    cv.imshow("fram", frame)
            cv.imshow("fram", frame)
                    
            

            
            key = cv.waitKey(1) & 0xFF

            if key == ord('1'):
                break

        webcam.release()
        cv.destroyAllWindows()

    def colour_limits(self, colour):
        c = np.uint8([[colour]])
        hsvc = cv.cvtColor(c, cv.COLOR_BGR2HSV)

        lowerlimit = hsvc[0][0][0] - 10, 100, 100
        upperlimit = hsvc[0][0][0] + 10, 255,255

        lowerlimit = np.array(lowerlimit, dtype=np.uint8)
        upperlimit = np.array(upperlimit, dtype=np.uint8)

        return lowerlimit, upperlimit

def main(args=None):
    detector = Object_Detect()
    detector.loop()

if __name__ == '__main__':
    main()