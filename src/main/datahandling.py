# write input trajectory to given file
def writetocsv(trajectory, name):
    f = open(name, "w")
    f.write("")
    f = open(name, "a")
    for x in trajectory[0]:
        f.write(str(x[0].pt[0]) + " ; " + str(x[0].pt[1]))
        f.write("\n")

# not used in project
# def adddimension(trajectory):
#     file = open('data.csv')
#     exi = file.readlines()
#     f = open("data2.csv", "w")
#     f.write("")
#     f = open("data2.csv", "a")
#     counter = 0
#     for x in trajectory[0]:
#         counter += 1
#         if x[1] == counter:
#             if exi[counter-1] == '\n':
#                 f.write(" ; " + " ; " + str(-int(x[0].pt[0])))
#                 f.write("\n")
#             else:
#                 strip = exi[counter-1].strip("\n")
#                 f.write(strip + " ; " + str(-int(x[0].pt[0])))
#                 f.write("\n")
#         else:
#             while counter < x[1]:
#                 print(x[1])
#                 print(len(exi))
#                 print(counter-1)
#                 print(exi[counter-1])
#                 f.write(exi[counter-1])
#                 counter += 1


# function to fill all empty frames
def datacleanse(fileloc):
    # open file
    file = open(fileloc)
    exi = file.readlines()
    f = open(fileloc, "w")
    f.write("")
    f = open(fileloc, "a")
    k = 0
    # parse content and catch empty cells
    while k < len(exi):
        strip = exi[k].strip("\n")
        if strip == ';;':
            exi[k] = [0, 0, 0]
        else:
            strip = exi[k].strip("\n")
            split = strip.split(';')
            if split[2] == '':
                exi[k] = [split[0], split[1], 0]
            elif split[0] == '' and split[1] == '':
                exi[k] = [0, 0, split[2]]
            else:
                exi[k] = [split[0], split[1], split[2]]
        k += 1
    dimensions = [0, 1, 2]
    # iterate through dimenstions
    for dim in dimensions:
        k = 0
        # iterate through rows and fill empty cells
        while k < len(exi):
            if exi[k][dim] == 0:
                counter = 1
                final = 0
                while counter + k < len(exi):
                    if exi[counter + k][dim] != 0:
                        final = exi[counter + k][dim]
                        break
                    else:
                        counter += 1
                steps = (int(final) - int(exi[k-1][dim]))/(counter+1)
                i = 0
                while i < counter:
                    exi[k + i][dim] = int(exi[k-1][dim]) + (steps * (i + 1))
                    i += 1
                k += counter
            k += 1
    for x in exi:
        f.write(str(x[0]) + ';' + str(x[1]) + ';' + str(x[2]) + '\n')


# function to recalculate all coordinates
def redim(fileloc):
    # open file
    file = open(fileloc)
    exi = file.readlines()
    f = open(fileloc, "w")
    f.write("")
    f = open(fileloc, "a")
    k = 0
    # resize coordinates according to provided formula
    while k < len(exi):
        strip = exi[k].strip("\n")
        split = strip.split(';')
        f.write(str(int(split[0]) - 315) + " ; " + str(int(split[1]) + 915) + " ; " + str(int(split[2]) - 1920))
        f.write("\n")
        k += 1
