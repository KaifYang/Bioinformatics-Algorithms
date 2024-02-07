from collections import defaultdict


def DeBruijnString(Text, k):
    graph = defaultdict(list)
    
    kmers = []

    for i in range(0, len(Text)-k+1):
        kmers.append(Text[i:i+k])
    

    for k in kmers:
        prefix = k[:-1]
        suffix = k[1:]
        graph[prefix].append(suffix)
    
    
    return graph

file = open('dataset_865399_6.txt')

k = int(file.readline().strip())
txt = file.readline().strip()

graph = DeBruijnString(txt, k)


output = open('output', 'w')

for key in graph:
    string = key + ': '
    for g in graph[key]:
        string = string + g + ' '
    
    output.write(string + '\n')