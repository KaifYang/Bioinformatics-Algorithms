def BreakPoints(P:list):
    permutation = P.copy()
    permutation.append(len(permutation)+1)
    permutation.insert(0, 0)

    count = 0

    for i in range(len(permutation)-1):
        if not permutation[i] == permutation[i+1] - 1:
            count += 1

    return count

file = open('Chapter6\dataset_865465_6 (1).txt')

li = file.readline().strip().split()
li = [int(a) for a in li]

print(BreakPoints(li))