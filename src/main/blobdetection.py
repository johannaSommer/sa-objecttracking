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
        params.minConvexity = 0.5
        params.filterByInertia = True
        params.minInertiaRatio = 0.05
        self.detector = cv.SimpleBlobDetector_create(params)
        self.threshold = 400

    def showbd(self):
        #traj_list=[[[kp, kp, kp], 2, c],[kp, kp, kp], 5, o]
        traj_list=[]
        while True:
            ret, frame = self.cap.read()
            if frame is None:
                break
            keypoints = self.detector.detect(frame)

            max = [10000, -1]
            for ind, traj in enumerate(traj_list):
                if traj_list[ind][2] == 'o':
                    traj_list[ind][1] += 1
            for kp in keypoints:
                for ind, traj in enumerate(traj_list):
                    if traj[2] == 'o':
                        dist = distance(kp, traj[0][-1])
                        if dist < max:
                            max = [dist, ind]
                if max[0] > self.threshold:
                    traj_list.append([[kp], 0, 'o'])
                else:
                    traj_list[max[1]][0].append(kp)
                    traj_list[max[1]][1] = 0
            for traj in traj_list:
                if traj[1] > 15:
                    traj[2] = 'c'

            im_with_keypoints = cv.drawKeypoints(frame, keypoints, np.array([]), (0, 0, 255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            cv.imshow("Keypoints", im_with_keypoints)
            for traj in traj_list:
                image = cv.imread("C:\Users\IBM_ADMIN\Desktop\GitHub\sa-objecttracking\src\snip2_0__1552679476.08.jpg")
                im_with_traj = cv.drawKeypoints(image, traj[0], np.array([]), (0, 0, 255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                while True:
                    cv.imshow("traj", im_with_traj)
                    if cv.waitKey(1) & 0xFF == ord('q'):
                        print(traj_list)
                        break
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
