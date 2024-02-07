from collections import defaultdict
import sys

def BuildDag(PAM250, indel_penalty, s, t):
    n = len(s)
    m = len(t)
    
    dag = defaultdict(list)

    for i in range(0, n):
        for j in range(0, m):
            dag[(i, j)].append(((i+1, j), -indel_penalty))
            dag[(i, j)].append(((i, j+1), -indel_penalty))
            dag[(i, j)].append(((i+1, j+1), PAM250[s[i]][t[j]]))
            
    for a in range(0, n):
        dag[(a, m)].append(((a+1, m), -indel_penalty))

    for b in range(0, m):
        dag[(n, b)].append(((n, b+1), -indel_penalty))
    
    return dag


def LongestPath(s: str, t: str, indel_penalty:int, PAM250) -> tuple[int, list[int]]:

    dag = BuildDag(PAM250, indel_penalty, s, t)

    #give path from start and path to end to all nodes
    for s1 in dag:
        if not s1 == (0, 0):
            dag[(0, 0)].append((s1, 0))
    for s2 in dag:
        if not s2 == (len(s), len(t)):
            dag[s2].append(((len(s), len(t)), 0))


    previous = defaultdict(list)
    weight = dict()
    predecessor = dict()


    for e in dag:
        for i in dag[e]:
            next = i[0]
            w = i[1]
            previous[next].append((e, w))

    for b in previous:
        if b not in dag:
            dag[b] = []

    

    #loop through the nodes in topological order
    for i in range(0, len(s)+1):
        for j in range(0, len(t)+1):
            #if the node has no edge coming in its weight is 0
            if (i, j) not in previous:
                weight[(i, j)] = 0
                continue
            
            max = float('-inf')

            #loop through all the previous nodes
            for p in previous[(i, j)]:
                
                pre = p[0]
                wei = p[1]
                
                if weight[pre] + wei > max:
                    #update max weight
                    max = weight[pre] + wei
                    #update predecessor node
                    predecessor[(i, j)] = pre
            
            weight[(i, j)] = max




    length = weight[(len(s), len(t))]

    current = (len(s), len(t))

    string1 = ''
    string2 = ''

    while not current == (0, 0):
        #print(current)
        prev = predecessor[current]

        if current == (1, 1) and prev == (0, 0):
            if PAM250[s[0]][t[0]] < 0:
                current = prev
                continue
        
        if current == (len(s), len(t)) and prev == (len(s)-1, len(t)-1):
            if PAM250[s[len(s)-1]][t[len(t)-1]] < 0:
                current = prev
                continue


        if prev == (current[0]-1, current[1]):
            string1 = s[current[0]-1] + string1
            string2 = '-' + string2 
        elif prev == (current[0], current[1]-1):
            string1 = '-' + string1 
            string2 = t[current[1]-1] + string2 
        elif prev == (current[0]-1, current[1]-1):
            string1 = s[current[0]-1] + string1 
            string2 = t[current[1]-1] + string2 

        current = prev
    
    result = (length, string1, string2)

    return result


sys.setrecursionlimit(10000)

PAM250 = defaultdict(defaultdict)

fil = open('Chapter4\PAM250.txt')

aa = fil.readline().strip().split()

line = fil.readline().strip().split()

while line:
    acid = line[0]

    for i in range(1, len(line)):
        PAM250[aa[i-1]][acid] = int(line[i])
    
    line = fil.readline().strip().split()


file = open('Chapter4\dataset_865449_10.txt')
s = file.readline().strip()
t = file.readline().strip()
ip = 5

result = LongestPath(s, t, ip, PAM250)

for r in result:
    print(r)