import cv2 as cv
import numpy as np

class DataHandler:
    def writetocsv(self, trajectory, show):
        if show is True:
            keypoints = []
            for x in trajectory[0]:
                keypoints.append(x[0])
            image = cv.imread("C:\Users\IBM_ADMIN\Desktop\GitHub\sa-objecttracking\src\snip2_0__1552679476.08.jpg")
            im_with_traj = cv.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255),
                                            cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            while True:
                cv.imshow("traj", im_with_traj)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break

        f = open("data.csv", "w")
        f.write("")
        f = open("data.csv", "a")
        length = len(trajectory[0])
        counter = 0
        for x in trajectory[0]:
            counter += 1
            if x[1] == counter:
                f.write(str(int(x[0].pt[0])) + " ; " + str(-int(x[0].pt[1])))
                f.write("\n")
            else:
                while counter < x[1]:
                    f.write("\n")
                    counter += 1
