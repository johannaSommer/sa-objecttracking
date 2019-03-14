import cv2 as cv

class Backgroundsub:
    def __init__(self, cap):
        self.cap = cap

    def applybgs(self):
        backsub = cv.createBackgroundSubtractorMOG2()
        backsub.setDetectShadows(0)
        while True:
            ret, frame = self.cap.read()
            if frame is None:
                break
            fgmask = backsub.apply(frame)
            frameinverted = cv.bitwise_not(fgmask)
        cv.imshow("frameinverted", frameinverted)
        #return 0 ??

    def savebgs(self):
        #TODO write code here to save