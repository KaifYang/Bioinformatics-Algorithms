from collections import defaultdict
import sys

def BuildDag(s, t):
    n = len(s)
    m = len(t)
    
    dag = defaultdict(list)

    for i in range(0, n):
        for j in range(0, m):
            dag[(i, j)].append(((i+1, j), -1))
            dag[(i, j)].append(((i, j+1), -1))
            if s[i] == t[j]:
                dag[(i, j)].append(((i+1, j+1), 0))
            else :
                dag[(i, j)].append(((i+1, j+1), -1))
            
    for a in range(0, n):
        dag[(a, m)].append(((a+1, m), -1))

    for b in range(0, m):
        dag[(n, b)].append(((n, b+1), -1))
    
    return dag



def EditDistance(s: str, t: str) -> tuple[int, list[int]]:

    dag = BuildDag(s, t)

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




    result = weight[(len(s), len(t))]

    return result


file = open('Chapter4\dataset_865450_3.txt')

string1 = file.readline().strip()
string2 = file.readline().strip()

print(-EditDistance(string1, string2))