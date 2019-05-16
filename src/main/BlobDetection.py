import cv2 as cv
import numpy as np
from utils import match_traj
from datahandling import  writetocsv

class Blobdetection:
    def __init__(self, fileloc, video, long):
        self.infile = fileloc[:-4]
        if video is True:
            self.cap = cv.VideoCapture(fileloc)
        else:
            self.cap = cv.imread(fileloc)
        self. long = long

        params = cv.SimpleBlobDetector_Params()
        params.minThreshold = 10
        params.maxThreshold = 200
        params.filterByArea = True
        params.filterByCircularity = True
        params.filterByConvexity = False
        params.filterByInertia = True
        if self.long == True:
            params.minArea = 70
            params.maxArea = 700
            params.minCircularity = 0.3
        else:
            params.minArea = 100
            # params.minArea = 150
            params.maxArea = 900
            params.minCircularity = 0.2
        params.minInertiaRatio = 0.2

        self.detector = cv.SimpleBlobDetector_create(params)
        self.threshold = 150

    def showbd(self):
        #active_traj_list=[[[[kp, frame], [kp, frame], [kp, frame]], current_frame],[kp, kp, kp], current_frame]
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
                active_traj_list = match_traj(kp, active_traj_list, self.threshold, frame_num, False)
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
                out = max(active_traj_list, key=lambda i: len(i[0]))
                normalized = []
                for x in out[0]:
                    if type(x) != int:
                        normalized.append(x[0])
                if self.long == True:
                    image = cv.imread("C:\Users\IBM_ADMIN\Desktop\GitHub\sa-objecttracking\src\main\laenge.jpg")
                else:
                    image = cv.imread("C:\Users\IBM_ADMIN\Desktop\GitHub\sa-objecttracking\src\main\lbreite.PNG")
                im_with_traj = cv.drawKeypoints(image, normalized, np.array([]), (0, 0, 255),
                                                cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                while True:
                    cv.imshow("traj", im_with_traj)
                    if cv.waitKey(1) & 0xFF == ord('q'):
                        break
                return out


    def showbdimg(self):
        keypoints = self.detector.detect(self.cap)
        im_with_keypoints = cv.drawKeypoints(self.cap, keypoints, np.array([]), (0, 0, 255),
                                             cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        while True:
            cv.imshow("Keypoints", im_with_keypoints)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
