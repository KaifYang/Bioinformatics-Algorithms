import random

def Lloyd(data, k, m):

    centers = [data[i] for i in range(k)]

    while True:
        #reset clusters
        clusters = []
        for j in range(len(centers)):
            clusters.append([])
        
        oldcenters = centers.copy()

        #reassign the clusters with the new centers
        for point in data:

            distance = float('inf')

            for center in centers:
                distlist = [(x-y)**2 for x,y in zip(point, center)]
                currd = sum(distlist)

                if currd < distance:
                    distance = currd
                    nearestcenter = center

            posi = centers.index(nearestcenter)

            clusters[posi].append(point)
        
        #calculate center of gravity for each cluster and make them the new centers
        for idx, cluster in enumerate(clusters):
            
            cog = []

            for axis in range(int(m)):
                axissum = 0
                for p in cluster:
                    axissum += p[axis]
                
                cog.append(axissum/len(cluster))
            
            centers[idx] = cog

        if centers == oldcenters:
            break
        
    return centers


file = open('Chapter8\dataset_865506_3.txt')

lines = file.readlines()

data = []

count = 0

for line in lines:
    sepline = [float(x) for x in line.split()]
    if count == 0:
        k = int(sepline[0])
        m = int(sepline[1])
    
    else:
        data.append(sepline)
    
    count += 1

result = Lloyd(data, k, m)

for r in result:
    for num in range(len(r)):
        if num == len(r) - 1:
            print(r[num])
        else:
            print(r[num], end = ' ')