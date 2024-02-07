from collections import defaultdict

def OverlapGraph(kmers:list[str]):
    overlap = defaultdict(list)
    
    for k in kmers:
        suffix = k[1:]
    
        rest = kmers.copy()
        rest.remove(k)
        
        for l in rest:
            prefix = l[:-1]
            
            if suffix == prefix:
                overlap[k].append(l)
    
    return overlap

file = open('Chapter3\dataset_865398_10.txt')

kmers = file.readline().strip().split()

graph = OverlapGraph(kmers)


output = open('output', 'w')

for key in graph:
    string = key + ': '
    for g in graph[key]:
        string = string + g + ' '
    
    output.write(string + '\n')
