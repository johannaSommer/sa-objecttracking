
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

            if cv.waitKey(1) & 0xFF == ord('q'):
                maximum1 = max(active_traj_list, key=lambda i: len(i[0]))
                #active_traj_list.remove(maximum1)
                #maximum2 = max(active_traj_list, key = lambda i : len(i[0]))
                #out = maximum1[0] + maximum2[0]
                image = cv.imread("C:\Users\IBM_ADMIN\Desktop\GitHub\sa-objecttracking\src\snip2_0__1552679476.08.jpg")
                im_with_traj = cv.drawKeypoints(image, maximum1[0], np.array([]), (0, 0, 255), cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                while True:
                    cv.imshow("traj", im_with_traj)
                    if cv.waitKey(1) & 0xFF == ord('q'):
                        break