import cv2 as cv
import numpy as np
from utils import match_traj
import operator

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
        params.minArea = 70
        params.maxArea = 700
        params.filterByCircularity = True
        params.minCircularity = 0.3
        params.filterByConvexity = True
        params.minConvexity = 0.0
        params.filterByInertia = False
        params.minInertiaRatio = 0.05
        self.detector = cv.SimpleBlobDetector_create(params)
        self.threshold = 150

    def showbd(self):
        #active_traj_list=[[[kp, kp, kp], current_frame],[kp, kp, kp], current_frame]
        active_traj_list = []
        dep_traj_list = []
        frame_num = 0
        while True:
            ret, frame = self.cap.read()
            if frame is None:
                break
            frame_num += 1
            keypoints = self.detector.detect(frame)

            for kp in keypoints:
                # manage return of function here
                active_traj_list = match_traj(kp, active_traj_list, self.threshold, frame_num)

                for traj in active_traj_list:
                    if (traj[1] - frame_num) > 15:
                        if len(traj[0]) < 30:
                            active_traj_list.remove(traj)
                        else:
                            dep_traj_list.append(traj)
                            active_traj_list.remove(traj)

            im_with_keypoints = cv.drawKeypoints(frame, keypoints, np.array([]), (0, 0, 255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            cv.imshow("Keypoints", im_with_keypoints)
            if cv.waitKey(1) & 0xFF == ord('q'):
                maximum1 = max(active_traj_list, key = lambda i : len(i[0]))
                #active_traj_list.remove(maximum1)
                #maximum2 = max(active_traj_list, key = lambda i : len(i[0]))
                #out = maximum1[0] + maximum2[0]
                image = cv.imread("C:\Users\IBM_ADMIN\Desktop\GitHub\sa-objecttracking\src\snip2_0__1552679476.08.jpg")
                im_with_traj = cv.drawKeypoints(image, maximum1[0], np.array([]), (0, 0, 255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                while True:
                    cv.imshow("traj", im_with_traj)
                    if cv.waitKey(1) & 0xFF == ord('q'):
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
