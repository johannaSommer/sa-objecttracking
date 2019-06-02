import math


# function to match blob to nearest trajectory
def match_traj(keypoint, list, threshold, frame_num, rec):
    # preparation
    if rec is True:
        keypoint = keypoint[0]
    maximum = [10000, -1]
    sub = False
    # iterate through list and find nearest trajectory
    for ind, traj in enumerate(list):
        if traj[1] == frame_num:
            index = len(traj[0])
            dist = distance(keypoint, traj[0][index - 2][0])
            if dist < maximum:
                if distance(keypoint, traj[0][index - 2][0]) < distance(traj[0][-1][0], traj[0][index - 2][0]):
                    maximum = [dist, ind]
                    sub = traj[0][-1]
        else:
            dist = distance(keypoint, traj[0][-1][0])
            if dist < maximum[0]:
                maximum = [dist, ind]
                sub = False
    # if necessary, create new trajectory
    if maximum[0] > threshold:
        list.append([[[keypoint, frame_num]], frame_num])
        return list
    # append new blob to trajectory, if necessary call match function recursively
    else:
        list[maximum[1]][0].append([keypoint, frame_num])
        list[maximum[1]][1] = frame_num
        if sub is not False:
            list[maximum[1]][0].remove(sub)
            return match_traj(sub, list, threshold, frame_num, True)
        else:
            return list


# calculate distance according to formula
def distance(kp, traj):
    weight = 0.1
    co_eucd = math.sqrt(math.pow((kp.pt[0]-traj.pt[0]), 2) + math.pow((kp.pt[1]-traj.pt[1]), 2))
    area_eucd = math.sqrt(pow(((pow((kp.size/2), 2)*math.pi)-(pow((traj.size/2), 2)*math.pi)), 2))
    return (1-weight) * co_eucd + weight * area_eucd
