import cv2 as cv
import time


class Backgroundsub:
    def __init__(self, fileloc):
        self.infile = fileloc[:-4]
        self.cap = cv.VideoCapture(fileloc)
        self.backsub = cv.createBackgroundSubtractorMOG2()
        self.backsub.setDetectShadows(0)

    def savebgs(self):
        fsize = (int(self.cap.get(cv.CAP_PROP_FRAME_WIDTH)), (int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT))))
        outfile = self.infile + "__" + str(time.time()) + ".wmv"
        video = cv.VideoWriter(outfile, cv.VideoWriter_fourcc('W', 'M', 'V', '1'), 30, fsize, False)
        if video.isOpened() is False:
            raise ValueError('No file could be opened.')
        while True:
            ret, frame = self.cap.read()
            if frame is None:
                break
            fgmask = self.backsub.apply(frame)
            frameinverted = cv.bitwise_not(fgmask)
            video.write(frameinverted)
            cv.imshow("frameinverted", frameinverted)
            if cv.waitKey(1) & 0xFF == ord('p'):
                cv.imwrite(self.infile + "__" + str(time.time()) + ".jpg", frameinverted)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        video.release()
        cv.destroyAllWindows()
        return outfile
