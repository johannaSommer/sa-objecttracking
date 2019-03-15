import cv2 as cv
import numpy as np

class Blobdetection:
    def __init__(self, fileloc):
        self.cap = cv.VideoCapture(fileloc)
        params = cv.SimpleBlobDetector_Params()
        params.minThreshold = 10
        params.maxThreshold = 200
        params.filterByArea = True
        params.minArea = 40
        # params.maxArea = 200
        params.filterByCircularity = True
        params.minCircularity = 0.3
        params.filterByConvexity = True
        params.minConvexity = 0.9
        params.filterByInertia = True
        params.minInertiaRatio = 0
        self.detector = cv.SimpleBlobDetector_create(params)

    def showbd(self):
        while True:
            ret, frame = self.cap.read()
            if frame is None:
                break
            keypoints = self.detector.detect(frame)
            im_with_keypoints = cv.drawKeypoints(frame, keypoints, np.array([]), (0, 0, 255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            cv.imshow("Keypoints", im_with_keypoints)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

    def applybd(self):
        f = open("data.csv", "w")
        f.write("")
        while True:
            ret, frame = self.cap.read()
            if frame is None:
                break
            keypoints = self.detector.detect(frame)
            im_with_keypoints = cv.drawKeypoints(frame, keypoints, np.array([]), (0, 0, 255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            f = open("data.csv", "a")
            # if len(keypoints) is 0:
            # TODO actually calculate negative here
            for x in keypoints:
                f.write("-" + str(int(x.pt[1])) + " ; " + str(int(x.pt[0])) + "\n")
            cv.imshow("Keypoints", im_with_keypoints)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break


    def savebd(self):
        # TODO: implment saving similarily to
        print("i have no programmed this path yet")
