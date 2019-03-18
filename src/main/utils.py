def islight(x, frame):
    # submatrix = frame[int(x.pt[1] - x.size/4):int(x.pt[1] + x.size/4), int(x.pt[0]- x.size/4):int(x.pt[0]+x.size/4)]
    # if submatrix.sum()/submatrix.size > 220:
    #     print(submatrix.sum() / submatrix.size)
    
    point1 = x.pt
    x1 = int(point1[0])
    y1 = int(point1[1])
    R = int(frame[y1, x1][1])
    B = int(frame[y1, x1][0])
    G = int(frame[y1, x1][2])
    if (R+G+B)/3 > 220:
        return True
    return False
