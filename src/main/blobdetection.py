import cv2 as cv
import numpy as np
from utils import distance

class Blobdetection:
    def __init__(self, fileloc, video):
        self.infile = fileloc[:-4]
        if video is True:
            self.cap = cv.VideoCapture(fileloc)
        else:
            self.cap = cv.imread(fileloc)
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
        self.threshold = 300

    def showbd(self):
        #traj_list=[[[kp, kp, kp], 2],[kp, kp, kp], 5]
        traj_list=[]
        while True:
            ret, frame = self.cap.read()
            if frame is None:
                break
            keypoints = self.detector.detect(frame)

            max = [10000, -1]
            for ind, traj in enumerate(traj_list):
                traj_list[ind][1] += 1
            for kp in keypoints:
                for ind, traj in enumerate(traj_list):
                    dist = distance(kp, traj[0][-1])
                    if dist<max:
                        max=[dist, ind]
                if max[0]>self.threshold:
                    traj_list.append([[kp], 0])
                else:
                    traj_list[max[1]][0].append(kp)
                    traj_list[max[1]][1] = 0

            im_with_keypoints = cv.drawKeypoints(frame, keypoints, np.array([]), (0, 0, 255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            cv.imshow("Keypoints", im_with_keypoints)
            if cv.waitKey(1) & 0xFF == ord('q'):
                # f = open("data.csv", "w")
                # f.write("")
                # f = open("data.csv", "a")
                # for traj in traj_list:
                #     for kp in traj[0]:
                #         f.write("-" + str(int(kp.pt[1])) + " ; " + str(int(kp.pt[0])) + "\n")
                #     f.write("---- \n \n")
                break

    def showbdimg(self):
        keypoints = self.detector.detect(self.cap)
        im_with_keypoints = cv.drawKeypoints(self.cap, keypoints, np.array([]), (0, 0, 255),
                                             cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        while True:
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
                f.write("-" + str(int(x.pt[1])) + " ; " + str(int(x.pt[0])) + " -- ")
            f.write("\n")
            cv.imshow("Keypoints", im_with_keypoints)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
