import math

def islight(x, frame):
    point1 = x.pt
    x1 = int(point1[0])
    y1 = int(point1[1])
    R = int(frame[y1, x1][1])
    B = int(frame[y1, x1][0])
    G = int(frame[y1, x1][2])
    if (R+G+B)/3 > 230:
        print('over: ' + str(R) + " " + str(G) + " " + str(B))
        return True
    if abs(R-B)<50 and abs(R-G)<50 and abs(G-B)<50 and R>120 and G>120 and B>120:
        print(R, G, B)
        return True
    return

def distance(kp, traj):
    weight = 0.4
    co_eucd = math.sqrt(math.pow((kp.pt[0]-traj.pt[0]), 2) + math.pow((kp.pt[1]-traj.pt[1]), 2))
    area_eucd = math.sqrt(pow(((pow((kp.size/2), 2)*math.pi)-(pow((traj.size/2), 2)*math.pi)), 2))
    return (1-weight) * co_eucd + weight * area_eucd
