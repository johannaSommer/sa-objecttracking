import cv2 as cv

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
        # TODO: fix
        fsize = (int(self.cap.get(cv.CAP_PROP_FRAME_WIDTH)), (int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT))))
        video = cv.VideoWriter("forground_Test.wmv", cv.VideoWriter_fourcc('W', 'M', 'V', '1'), 30, fsize, False)
        if video.isOpened() is False:
            print("nope")
        while True:
            ret, frame = self.cap.read()
            if frame is None:
                break
            fgmask = self.backsub.apply(frame)
            frameinverted = cv.bitwise_not(fgmask)
            video.write(frameinverted)
            cv.imshow("framinverted", frameinverted)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        video.release()
        cv.destroyAllWindows()
