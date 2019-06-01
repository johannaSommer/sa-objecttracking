from main.analysis import categorize
from main.analysis import determine_speed
from main.BackgroundSubtraction import Backgroundsub
import numpy as np
import time
from main.datahandling import writetocsv
from main.BlobDetection import Blobdetection
import os
from main.utils import match_traj
from main.utils import distance
import cv2 as cv


def test_trajmatch():
    threshold = 150
    rec = False
    keypoint = cv.KeyPoint(10, 10, 10,  _angle=-1,  _response=0,  _octave=0,  _class_id=-1)
    frame_num = 2
    list = [
        [[[cv.KeyPoint(9, 9, 9,  _angle=-1,  _response=0,  _octave=0,  _class_id=-1), 1]], 1],
        [[[cv.KeyPoint(10, 10, 10,  _angle=-1,  _response=0,  _octave=0,  _class_id=-1), 1],
          [cv.KeyPoint(10, 9, 10,  _angle=-1,  _response=0,  _octave=0,  _class_id=-1), 2]], 2]
    ]
    ret = match_traj(keypoint, list, threshold, frame_num, rec)
    parsed = [
        [[ret[0][0][0][0].pt[0], ret[0][0][0][0].pt[1]], [ret[0][0][1][0].pt[0], ret[0][0][1][0].pt[1]]],
        [[ret[1][0][0][0].pt[0], ret[1][0][0][0].pt[1]], [ret[1][0][1][0].pt[0], ret[1][0][1][0].pt[1]]]
    ]
    expected = [
        [[9.0, 9.0], [10.0, 9.0]],
        [[10.0, 10.0], [10.0, 10.0]]
    ]
    assert parsed == expected


def test_distance():
    keypoint = cv.KeyPoint(1, 1, 1,  _angle=-1,  _response=0,  _octave=0,  _class_id=-1)
    trajectorykp = cv.KeyPoint(2, 2, 2,  _angle=-1,  _response=0,  _octave=0,  _class_id=-1)
    expected = 1.508
    assert expected == round(distance(keypoint, trajectorykp), 3)



def test_blobdecimgcount():
    PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testing', 'testdata', 'BlobTest.jpg')
    bd = Blobdetection(PATH, False, False)
    keypoints = bd.showbdimg()
    assert len(keypoints) == 16


def test_writecsv():
    filename = str(time.time()) + '.csv'
    trajectory = [
        [
            [cv.KeyPoint(1, 2, 3,  _angle=-1,  _response=0,  _octave=0,  _class_id=-1)],
            [cv.KeyPoint(3, 2, 1,  _angle=-1,  _response=0,  _octave=0,  _class_id=-1)]
        ]
        , 11]
    writetocsv(trajectory, filename)
    file = open(filename)
    result = file.readlines()
    testfile = open('testdata/TestData.csv')
    expected = testfile.readlines()
    assert result == expected


def test_datacleanse():
    file = open('testdata/sync_1_norm.csv')
    testdata = file.readlines()
    correct = True
    for x in testdata:
        temp = x.split(';')
        if len(temp) != 3:
            correct = False
    assert correct


def test_redim():
    file = open('testdata/sync_1_norm.csv')
    testdata = file.readlines()
    correct = True
    for x in testdata:
        temp = x.split(';')
        if int(temp[0]) > 1920 or int(temp[0]) < 0:
            correct = False
        if int(temp[1]) > 1080 or int(temp[1]) < 0:
            correct = False
        if int(temp[2]) > 0 or int(temp[2]) < -1920:
            correct = False
    assert correct

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
    PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testing', 'testdata', 'sync_2_1.mp4')
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


def test_cat():
    PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testing', 'testdata', 'AnalysisTest.csv')
    categorize(PATH)
    file = open(PATH)
    result = file.readlines()
    out = []
    for x in result:
        out.append(x.strip('\n').split(';'))
    speed = [x[3] for x in out]
    expected = ['1', '1', '1', '2', '2', '2']
    assert speed == expected


def test_speed():
    PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testing', 'testdata', 'AnalysisTest.csv')
    determine_speed(PATH, PATH)
    file = open(PATH)
    result = file.readlines()
    out = []
    for x in result:
        out.append(x.strip('\n').split(';'))
    speed = []
    for x in out:
        if len(x) == 5:
            speed.append(x[4])
    expected = ['20', '0', '20', '31']
    assert speed == expected