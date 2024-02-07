from collections import defaultdict
import sys

def BuildDag(match_reward, mismatch_penalty, indel_penalty, s, t):
    n = len(s)
    m = len(t)
    
    dag = defaultdict(list)

    for i in range(0, n):
        for j in range(0, m):
            dag[(i, j)].append(((i+1, j), -indel_penalty))
            dag[(i, j)].append(((i, j+1), -indel_penalty))
            if s[i] == t[j]:
                dag[(i, j)].append(((i+1, j+1), match_reward))
            else:
                dag[(i, j)].append(((i+1, j+1), -mismatch_penalty))
            
            
    for a in range(0, n):
        dag[(a, m)].append(((a+1, m), -indel_penalty))

    for b in range(0, m):
        dag[(n, b)].append(((n, b+1), -indel_penalty))

    for c in range(1, n+1):
        dag[(0, 0)].append(((c, 0), 0))
    
    for d in range(0, m):
        dag[(n, d)].append(((n, m), 0))
    
    return dag


def LongestPath(s: str, t: str, indel_penalty:int, match_reward, mismatch_penalty) -> tuple[int, list[int]]:

    dag = BuildDag(match_reward, mismatch_penalty, indel_penalty, s, t)
    
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


    current = (len(s), len(t))

    score = weight[( (len(s), len(t)))]
    
    string1 = ''
    string2 = ''

    while not current[1] == 0:
        if current == (len(s), len(t)):
            prev = predecessor[current]
            current = prev
            continue
        #print(current)
        prev = predecessor[current]

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
    
    result = (score, string1, string2)

    return result


BLOSUM62 = defaultdict(defaultdict)

fil = open('Chapter4\BLOSUM62.txt')

aa = fil.readline().strip().split()

line = fil.readline().strip().split()

while line:
    acid = line[0]

    for i in range(1, len(line)):
        BLOSUM62[aa[i-1]][acid] = int(line[i])
    
    line = fil.readline().strip().split()


file = open('Chapter4\dataset_865450_7.txt')
file.readline()
s = file.readline().strip()
t = file.readline().strip()
#s = 'GAGA'
#t = 'GAT'
mr = 1
mp = 1
ip = 2

result = LongestPath(s, t, ip, mr, mp)

for r in result:
    print(r)
