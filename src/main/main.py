from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np

parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. You can process both videos and images.')
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='videos_march/test1_edit.mp4')
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
args = parser.parse_args()

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

# Set up the detector with default parameters.
detector = cv.SimpleBlobDetector_create(params)
f = open("data.csv", "w")
f.write("")



capture = cv.VideoCapture(args.input)

    keypoints = detector.detect(frameinverted)

    im_with_keypoints = cv.drawKeypoints(frameinverted, keypoints, np.array([]), (0, 0, 255),
                                          cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv.imshow("Keypoints", im_with_keypoints)

    # f = open("data.csv", "a")
    # #if len(keypoints) is 0:
    # # TODO actually calculate negative here
    # for x in keypoints:
    #     f.write("-" + str(int(x.pt[1])) + " ; " + str(int(x.pt[0])) + "\n")
