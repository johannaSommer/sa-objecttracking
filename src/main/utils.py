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
    return False
