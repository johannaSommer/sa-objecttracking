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
