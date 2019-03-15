import cv2 as cv
import time

class Backgroundsub:
    def __init__(self, fileloc):
        self.cap = cv.VideoCapture(fileloc)
        self.backsub = cv.createBackgroundSubtractorMOG2()
        self.backsub.setDetectShadows(0)

    def applybgs(self):
        while True:
            ret, frame = self.cap.read()
            if frame is None:
                break
            fgmask = self.backsub.apply(frame)
            frameinverted = cv.bitwise_not(fgmask)
            cv.imshow("frameinverted", frameinverted)

    def savebgs(self):
        out = cv.VideoWriter("backsubout/" + str(time.time()), -1, 20.0, (640, 480))
        while True:
            ret, frame = self.cap.read()
            if frame is None:
                break
            fgmask = self.backsub.apply(frame)
            frameinverted = cv.bitwise_not(fgmask)
            out.write(frame)
            cv.imshow("frameinverted", frameinverted)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        out.release()
        cv.destroyAllWindows()
