import cv2 as cv
import time
import numpy as np
from utils import islight

class Backgroundsub:
    def __init__(self, fileloc):
        self.infile = fileloc[:-4]
        self.cap = cv.VideoCapture(fileloc)
        self.backsub = cv.createBackgroundSubtractorMOG2()
        self.backsub.setDetectShadows(0)
        params = cv.SimpleBlobDetector_Params()
        params.minThreshold = 10
        params.maxThreshold = 200
        params.filterByArea = True
        params.minArea = 120
        params.maxArea = 600
        params.filterByCircularity = True
        params.minCircularity = 0.3
        params.filterByConvexity = True
        params.minConvexity = 0.8
        params.filterByInertia = True
        params.minInertiaRatio = 0.05
        self.detector = cv.SimpleBlobDetector_create(params)

    def applybgs(self):
        f = open("data.csv", "w")
        f.write("")
        while True:
            ret, frame = self.cap.read()
            if frame is None:
                break
            fgmask = self.backsub.apply(frame)
            frameinverted = cv.bitwise_not(fgmask)
            keypoints = self.detector.detect(frameinverted)
            for x in keypoints:
                if islight(x, frame) is False:
                    keypoints.remove(x)
            im_with_keypoints = cv.drawKeypoints(frameinverted, keypoints, np.array([]), (0, 0, 255),
                                                 cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            f = open("data.csv", "a")
            for x in keypoints:
                f.write("-" + str(int(x.pt[1])) + " ; " + str(int(x.pt[0])) + " -- ")
            f.write("\n")
            cv.imshow("keypoints", im_with_keypoints)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

    def savebgs(self):
        fsize = (int(self.cap.get(cv.CAP_PROP_FRAME_WIDTH)), (int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT))))
        outfile = self.infile + "__" + str(time.time()) + ".wmv"
        video = cv.VideoWriter(outfile, cv.VideoWriter_fourcc('W', 'M', 'V', '1'), 30, fsize, False)
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
            if cv.waitKey(1) & 0xFF == ord('p'):
                cv.imwrite(self.infile + "__" + str(time.time()) + ".jpg", frameinverted)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        video.release()
        cv.destroyAllWindows()
        return outfile
