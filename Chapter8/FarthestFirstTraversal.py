
def FarthestFirstTraversal(Data, k, m):
    centers = []

    centers.append(Data[0])

    while len(centers) < k:
        max = 0
        
        for point in Data:
            distance = float('inf')
            for center in centers:
                suum = [(x-y)**2 for x,y in zip(point, center)]
                currd = (sum(suum))**(1/2)

                if currd < distance:
                    distance = currd

            if distance > max:
                max = distance
                datapoint = point

        centers.append(datapoint)

    return centers

file = open('Chapter8\dataset_865504_2.txt')

lines = file.readlines()

data = []

count = 0

for line in lines:
    sepline = [float(x) for x in line.split()]
    if count == 0:
        k = sepline[0]
        m = sepline[1]
    
    else:
        data.append(sepline)
    
    count += 1

result = FarthestFirstTraversal(data, k, m)

for r in result:
    for num in range(len(r)):
        if num == len(r) - 1:
            print(r[num])
        else:
            print(r[num], end = ' ')