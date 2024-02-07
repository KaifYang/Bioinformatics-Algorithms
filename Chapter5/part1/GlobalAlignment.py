from collections import defaultdict
import sys
def Getbacktrack(match_reward: int, mismatch_penalty: int, indel_penalty: int, s: str, t: str) :
    n = len(s)
    m = len(t)
    
    #calculate the weight of each node and get the backtrack 
    weight = defaultdict()
    backtrack = [ [ 0 for a in range(m+1) ] for b in range(n+1) ]

    weight[(0, 0)] = 0

    for c in range(1, n+1):
        weight[(c, 0)] = weight[(c-1, 0)] - indel_penalty
    
    for d in range(1, m+1):
        weight[(0, d)] = weight[(0, d-1)] - indel_penalty
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            down = weight[(i-1, j)] - indel_penalty
            right = weight[(i, j-1)] - indel_penalty
            if s[i-1] == t[j-1] :
                dr = weight[(i-1, j-1)] + match_reward
            else:
                dr = weight[(i-1, j-1)] - mismatch_penalty

            weight[(i, j)] = max(down, right, dr)

            if weight[(i, j)] == down:
                backtrack[i][j] = 'down'
            elif weight[(i, j)] == right:
                backtrack[i][j] = 'right'
            if weight[(i, j)] == dr:
                backtrack[i][j] = 'dr'

    return (weight[n, m], backtrack)


def OutputPathV(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ''
    #print(i)
    #print(j)
    
    if backtrack[i][j] == 'down':
        #print(str(i) + 'down')
        return OutputPathV(backtrack, v, i-1, j) + v[i-1]
    elif backtrack[i][j] == 'right':
        #print(str(i) + 'right')
        return OutputPathV(backtrack, v, i, j-1) + '-'
    else:
        #print(str(i) + 'dr')
        return OutputPathV(backtrack, v, i-1, j-1) + v[i-1]

def OutputPathW(backtrack, w, i, j):
    if i == 0 or j == 0:
        return ''
    #print(i)
    #print(j)
    
    if backtrack[i][j] == 'down':
        return OutputPathW(backtrack, w, i-1, j) + '-'
    elif backtrack[i][j] == 'right':
        return OutputPathW(backtrack, w, i, j-1) + w[j-1]
    else:
        #print(v)
        return OutputPathW(backtrack, w, i-1, j-1) + w[j-1]


def GlobalAlignment(match_reward: int, mismatch_penalty: int, indel_penalty: int, s: str, t: str) -> tuple[int, str, str]:
    
    tup = Getbacktrack(match_reward, mismatch_penalty, indel_penalty, s, t)

    score = tup[0]
    backtrack = tup[1]
    print(backtrack)
    stringV = OutputPathV(backtrack, s, len(s), len(t))
    stringW = OutputPathW(backtrack, t, len(s), len(t))

    return (score, stringV, stringW)

sys.setrecursionlimit(10000)
file = open('Chapter4\dataset_865449_3.txt')
file.readline()
string1 = file.readline().strip()
string2 = file.readline().strip()

for a in GlobalAlignment(1, 1, 5, string1, string2):
    print(a)