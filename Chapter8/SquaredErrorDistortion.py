def SquaredErrorDistortion(Data, Centers, k, m):

    suum = 0
    n = len(Data)

    for point in Data:
        distance = float('inf')

        for center in Centers:
            distlist = [(x-y)**2 for x,y in zip(point, center)]
            currd = sum(distlist)

            if currd < distance:
                distance = currd

        suum = suum + distance
    
    return suum/n

file = open('Chapter8\dataset_865505_3.txt')

lines = file.read().splitlines()

centers = []
data = []

count = 0
stop = 0

for line in lines:

    if '-' in line:
        stop = lines.index(line)
        break

    sepline = [float(x) for x in line.split()]
    if count == 0:
        k = sepline[0]
        m = sepline[1]
    
    else:
        centers.append(sepline)
    
    count += 1

for l in range(stop+1, len(lines)):
    sepline = [float(x) for x in lines[l].split()]

    data.append(sepline)

print(SquaredErrorDistortion(data, centers, k, m))


