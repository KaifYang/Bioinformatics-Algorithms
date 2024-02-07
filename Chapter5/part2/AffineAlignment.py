from collections import defaultdict

#0 index in the list is the weight, 1 index is the predecessor position, 2 index is the graph the predecessor is in
def LongestPath(match_reward: int, mismatch_penalty:int, go_penalty:int, ge_penalty:int, s: str, t: str) -> tuple[int, list[int]]:
    n = len(s)
    m = len(t)

    #only have edge going down
    downgraph = defaultdict(list)
    #only have edge going right
    rightgraph = defaultdict(list)
    #only have edge going diagonal
    middlegraph = defaultdict(list)

    weight = defaultdict(list)
 
    middlegraph[0, 0].append(0) 


    for q in range(1, n+1):
        if q == 1:
            rightgraph[(q, 0)].append(middlegraph[(q-1, 0)][0] - go_penalty)
            rightgraph[(q, 0)].append((q-1, 0))
            rightgraph[(q, 0)].append('M')
        else:
            rightgraph[(q, 0)].append(rightgraph[(q-1, 0)][0] - ge_penalty)
            rightgraph[(q, 0)].append((q-1, 0))
            rightgraph[(q, 0)].append('R')
        

        middlegraph[(q, 0)].append(rightgraph[(q, 0)][0])
        middlegraph[(q, 0)].append((q-1, 0))
        middlegraph[(q, 0)].append('R')

    for w in range(1, m+1):
        if w == 1:
            downgraph[(0, w)].append(middlegraph[(0, w-1)][0] - go_penalty)
            downgraph[(0, w)].append((0, w-1))
            downgraph[(0, w)].append('M')
        else:
            downgraph[(0, w)].append(downgraph[(0, w-1)][0] - ge_penalty)
            downgraph[(0, w)].append((0, w-1))
            downgraph[(0, w)].append('D')
        
        middlegraph[(0, w)].append(downgraph[(0, w)][0])
        middlegraph[(q, 0)].append((0, w-1))
        middlegraph[(q, 0)].append('D')


    for d in range(0, n+1):
        downgraph[(d, 0)].append(float('-inf'))

    for r in range(0, m+1):
        rightgraph[(0, r)].append(float('-inf'))


    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            
            #get down(i, j)
            d_ge = downgraph[(i-1, j)][0] - ge_penalty
            d_go = middlegraph[(i-1, j)][0] - go_penalty
            downgraph[(i, j)].append(max(d_ge, d_go))

            if downgraph[(i, j)][0] == d_ge:
                downgraph[(i, j)].append((i-1, j))
                downgraph[(i, j)].append('D')
            else:
                downgraph[(i, j)].append((i-1, j))
                downgraph[(i, j)].append('M')

            #get right(i, j)
            r_ge = rightgraph[(i, j-1)][0] - ge_penalty
            r_go = middlegraph[(i, j-1)][0] - go_penalty
            rightgraph[(i, j)].append(max(r_ge, r_go))

            if rightgraph[(i, j)][0] == r_ge:
                rightgraph[(i, j)].append((i, j-1))
                rightgraph[(i, j)].append('R')
            else:
                rightgraph[(i, j)].append((i, j-1))
                rightgraph[(i, j)].append('M')

            #get middle(i, j)
            dd = downgraph[(i, j)][0]
            rr = rightgraph[(i, j)][0]
            if s[i-1] == t[j-1]:
                mm = middlegraph[(i-1, j-1)][0] + match_reward
            else: 
                mm = middlegraph[(i-1, j-1)][0] - mismatch_penalty

            middlegraph[(i, j)].append(max(dd, rr, mm))

            if middlegraph[(i, j)][0] == dd:
                middlegraph[(i, j)].append((i, j))
                middlegraph[(i, j)].append('D')

            elif middlegraph[(i, j)][0] == rr:
                middlegraph[(i, j)].append((i, j))
                middlegraph[(i, j)].append('R')
            
            else:
                middlegraph[(i, j)].append((i-1, j-1))
                middlegraph[(i, j)].append('M')


    length = middlegraph[(len(s), len(t))][0]

    current = middlegraph[(len(s), len(t))]
    currposi = (len(s), len(t))

    string1 = ''
    string2 = ''

    while not currposi == (0, 0):
        
        if current[2] == 'D':
            prev = downgraph[current[1]]
        elif current[2] == 'R':
            prev = rightgraph[current[1]]
        elif current[2] == 'M':
            prev = middlegraph[current[1]]

        if current[1] == (currposi[0]-1, currposi[1]):
            string1 = s[currposi[0]-1] + string1
            string2 = '-' + string2 
        elif current[1] == (currposi[0], currposi[1]-1):
            string1 = '-' + string1 
            string2 = t[currposi[1]-1] + string2 
        elif current[1] == (currposi[0]-1, currposi[1]-1):
            string1 = s[currposi[0]-1] + string1 
            string2 = t[currposi[1]-1] + string2 

        currposi = current[1]
        current = prev
    
    result = (length, string1, string2)

    return result




#file = open('Chapter4\dataset_865449_10.txt')

mr = 1
mp = 5
go = 3
ge = 1
s = 'GCACCTTGAGAGCAATCATCGGGGTGCTAGTGATCCTCATAAAGGCTACGCTAGTCCAACTCTCCTTTCTCTGCTAAACGCCCGGGAGGT'
t = 'GGTACTTTGCACCGAGAGCAATCATCGGGGTGATGTTTTACAATGGCCCGGGATACGCGGGTTAGGCCAACTCTCGTCTAAACGCCCGGGTCGGGT'


result = LongestPath(mr, mp, go, ge, s, t)

for r in result:
    print(r)