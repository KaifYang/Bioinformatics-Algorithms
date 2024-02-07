def GreedySorting(P:list):
    permutation = P.copy()
    rd = 0
    steps = []

    #the permutation starts at 1, the actual index of k is i-1
    for i in range(1, len(permutation)+1):
        k = permutation[i-1]
        
        #check if element is at right position
        if not abs(k) == i:
            #find the position of the element
            for j in range(len(permutation)):
                if abs(permutation[j]) == i:
                    posi = j 
            
            #reverse it back to the correct position
            l = []
            for a in range(i-1, posi+1):
                l.append(-permutation[a])
            l.reverse()

            permutation = [*permutation[:i-1], *l, *permutation[posi+1:]]

            p = permutation.copy()

            steps.append(p)

            rd += 1
        
        if permutation[i-1] == -i:
            permutation[i-1] = i

            p = permutation.copy()

            steps.append(p)

            rd += 1

    return steps

file = open('Chapter6\dataset_865464_4.txt')

li = file.readline()
li = li.split()
li = [int(a) for a in li]

result = GreedySorting(li)

file.close()

with open('result.txt', 'w') as f:
    for r in result:
        st = ''
        for h in r:
            
            if h > 0:
                st = st + '+' + str(h) + ' '
            else:
                st = st + str(h) + ' '
        st = st[:-1]
        f.write(st + '\n')



    