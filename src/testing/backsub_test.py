from main.BackgroundSubtraction import Backgroundsub
import cv2 as cv
import os
import numpy as np


def test_pixelh():
    # read in original file
    PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testing', 'testdata', 'sync_1_1.mp4')
    bgs = Backgroundsub(PATH)
    # read in background subtracted video
    out = bgs.savebgs()
    out = cv.VideoCapture(out)

    pixeltotal = 1920 * 1080

    # read first frame beforehand because it will always be black
    out.read()

    # take the first 3 frames and count number of white pixels
    result = []
    for i in range(0, 3):
        ret, frame = out.read()
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        result.append(float(cv.countNonZero(frame))/float(pixeltotal))
    assert np.average(result) > 0.98


def test_pixelv():
    # read in original file
    PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sampledata', 'sync_2_1.mp4')
    bgs = Backgroundsub(PATH)
    # read in background subtracted video
    out = bgs.savebgs()
    out = cv.VideoCapture(out)

    pixeltotal = 1920 * 1080

    # read first frame beforehand because it will always be black
    out.read()

    # take the first 3 frames and count number of white pixels
    result = []
    for i in range(0, 3):
        ret, frame = out.read()
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        result.append(float(cv.countNonZero(frame))/float(pixeltotal))
    assert np.average(result) > 0.5
