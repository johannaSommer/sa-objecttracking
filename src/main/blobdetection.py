import cv2 as cv

class Blobdetection:
    def __init__(self, fileloc):
        # TODO create capture of file here
        self.cap = cap

    def applybd(self):
        # TODO insert rest here
        while True:
            ret, frame = self.cap.read()
            if frame is None:
                break
            cv.imshow("frameinverted", frameinverted)
            keyboard = cv.waitKey(30)
            if keyboard == 'q' or keyboard == 27:
                break

    def savebd(self):
        print("hello")



# Set up the detector with default parameters.
detector = cv.SimpleBlobDetector_create(params)
f = open("data.csv", "w")
f.write("")

    keypoints = detector.detect(frameinverted)

    im_with_keypoints = cv.drawKeypoints(frameinverted, keypoints, np.array([]), (0, 0, 255),
                                          cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv.imshow("Keypoints", im_with_keypoints)

    # f = open("data.csv", "a")
    # #if len(keypoints) is 0:
    # # TODO actually calculate negative here
    # for x in keypoints:
    #     f.write("-" + str(int(x.pt[1])) + " ; " + str(int(x.pt[0])) + "\n")


# Setup SimpleBlobDetector parameters.
params = cv.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200
filterByColor = False

# Filter by Area.
params.filterByArea = True
params.minArea = 40
# params.maxArea = 200

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.3

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.9

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0
