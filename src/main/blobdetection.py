import cv2 as cv

class Blobdetection:
    def __init__(self, fileloc):
        # TODO create capture of file here
        self.cap = cap

    def applybd(self):
        # TODO insert rest here
        while True:
            ret, frame = self.cap.read()
            if frame is None:
                break
            cv.imshow("frameinverted", frameinverted)
            keyboard = cv.waitKey(30)
            if keyboard == 'q' or keyboard == 27:
                break

    def savebd(self):
        print("hello")
