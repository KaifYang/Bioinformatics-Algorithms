def LongestPathLength(n: int, m: int, Down: list[list[int]], Right: list[list[int]]):
    lengthmatrix = [ [ 0 for a in range(m+1) ] for b in range(n+1) ]
    lengthmatrix[0][0] = 0
    
    for i in range(1, n+1):
        lengthmatrix[i][0] = lengthmatrix[i-1][0] + Down[i-1][0]
    
    for j in range(1, m+1):
        lengthmatrix[0][j] = lengthmatrix[0][j-1] + Right[0][j-1]

    for i in range(1, n+1):
        for j in range(1, m+1):
            lengthmatrix[i][j] = max((lengthmatrix[i-1][j] + Down[i-1][j]), (lengthmatrix[i][j-1] + Right[i][j-1]))

    return lengthmatrix[n][m]


file = open('Chapter4\dataset_865445_10.txt')
nm = file.readline().strip().split()
n = int(nm[0])
m = int(nm[1])

down = []
right = []

for i in range(n):
    line = file.readline().strip().split()
    line = [int(k) for k in line]
    down.append(line)

file.readline()

for j in range(n+1):
    line = file.readline().strip().split()
    line = [int(h) for h in line]
    right.append(line)

print(LongestPathLength(n, m, down, right))