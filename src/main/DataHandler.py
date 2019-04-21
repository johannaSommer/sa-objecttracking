import cv2 as cv
import numpy as np

class DataHandler:
    def writetocsv(self, trajectory, show):
        if show is True:
            image = cv.imread("C:\Users\IBM_ADMIN\Desktop\GitHub\sa-objecttracking\src\snip2_0__1552679476.08.jpg")
            im_with_traj = cv.drawKeypoints(image, trajectory[0], np.array([]), (0, 0, 255),
                                            cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            while True:
                cv.imshow("traj", im_with_traj)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
        # write trajectory to csv here
        f = open("data.csv", "w")
        f.write("")
        f = open("data.csv", "a")
        for x in trajectory[0]:
            f.write(str(-int(x.pt[1])) + " ; " + str(int(x.pt[0])))
            f.write("\n")
