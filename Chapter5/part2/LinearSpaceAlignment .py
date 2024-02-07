from collections import defaultdict

def getscore(s: str, t: str, indel_penalty:int, match_reward: int, mismatch_penalty:int):
    weight = defaultdict()

    weight[0, 0] = 0

    for a in range(1, len(s)+1):
        weight[(a, 0)] = weight[(a-1, 0)] - indel_penalty
    
    for b in range(1, len(t)+1):
        weight[(0, b)] = weight[(0, b-1)] - indel_penalty

    for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
        
                down = weight[(i-1, j)] - indel_penalty
                right = weight[(i, j-1)] - indel_penalty
                if s[i-1] == t[j-1]:
                    diagonal = weight[(i-1, j-1)] + match_reward
                else:
                    diagonal = weight[(i-1, j-1)] - mismatch_penalty
                
                weight[(i, j)] = (max(down, right, diagonal))

    return weight[(len(s), len(t))]


def getmidcol(s: str, t: str, indel_penalty:int, match_reward: int, mismatch_penalty:int, isfs: bool):
    mid = len(t)//2
    
    if isfs == False:
        mid = len(t) - mid

    fs = defaultdict()
    
    fs[0, 0] = 0

    for a in range(1, len(s)+1):
        fs[(a, 0)] = (fs[(a-1, 0)] - indel_penalty)

    for b in range(1, len(t)+1):
        fs[(0, b)] = (fs[(0, b-1)] - indel_penalty)

    mid_col = []

    if isfs == False:
            mid_col.append((fs[(0, mid)], 'right'))
    elif isfs == True:
            mid_col.append(fs[(0, mid)])

    for i in range(1, len(s)+1):
        for j in range(1, mid+1):

            down = fs[(i-1, j)] - indel_penalty
            right = fs[(i, j-1)] - indel_penalty
            if s[i-1] == t[j-1]:
                diagonal = fs[(i-1, j-1)] + match_reward
            else:
                diagonal = fs[(i-1, j-1)] - mismatch_penalty
            
            #print((i, j))
            #print(down)
            #print(right)
            #print(diagonal)

            fs[(i, j)] = (max(down, right, diagonal))


            #the two strings are reversed so the down and right are also reversed
            if j == mid and isfs == False:
                if fs[(i, j)] == down:
                    mid_col.append((fs[(i, j)], 'down'))
                elif fs[(i, j)] == right:
                    mid_col.append((fs[(i, j)], 'right'))
                elif fs[(i, j)] == diagonal:
                    mid_col.append((fs[(i, j)], 'diagonal'))
            elif j == mid and isfs == True:
                mid_col.append(fs[(i, j)])

    if mid == 0:
        for r in range(1, len(s)+1):
            mid_col.append(fs[(r, 0)])

    return mid_col


def MiddleEdge(s: str, t: str, indel_penalty:int, match_reward: int, mismatch_penalty) -> tuple[int, list[int]]:

    mid = len(t)//2
    
    #get FromSource
    fs_col = getmidcol(s, t, indel_penalty, match_reward, mismatch_penalty, True)

    #get ToSink
    rs = s[::-1]
    rt = t[::-1]

    ts_col = getmidcol(rs, rt, indel_penalty, match_reward, mismatch_penalty, False)
    ts_col.reverse()

    #print(fs_col)
    #print(ts_col)

    max = float('-inf')
    midnode = None
    next = None

    for i in range(0, len(s)+1):
        curr = fs_col[i] + ts_col[i][0]
        if curr > max:
            max = curr
            midnode = (i, mid)
            if ts_col[i][1] == 'down':
                next = 'Down'
            elif ts_col[i][1] == 'right':
                next = 'Right'
            elif ts_col[i][1] == 'diagonal':
                next = 'Diagonal'

    return (midnode, next)



def LinearSpaceAlignment(match_reward: int, mismatch_penalty:int, indel_penalty:int, s: str, t: str, top, bottom, left, righ):
    if left == righ:
        edges = []
        for i in range(0, bottom-top):
            edges.append('Down')
        return edges

    if top == bottom:
        edges = []
        for j in range(0, righ - left):
            edges.append('Right')
        return edges        
    
    edges = []

    middle = (left+righ)//2

    midEdge = MiddleEdge(s[top:bottom], t[left:righ], indel_penalty, match_reward, mismatch_penalty)
    #midNode ← vertical coordinate of the initial node of midEdge 
    midNode = midEdge[0][0] + top

    edges = [*LinearSpaceAlignment(match_reward, mismatch_penalty, indel_penalty, s, t, top, midNode, left, middle), *edges]

    edges.append(midEdge[1])

    if midEdge[1] == 'Right' or midEdge[1] == 'Diagonal':
        middle += 1
    
    if midEdge[1] == 'Down' or midEdge[1] == 'Diagonal':
        midNode += 1
    
    edges = [*edges, *LinearSpaceAlignment(match_reward, mismatch_penalty, indel_penalty, s, t, midNode, bottom, middle, righ)]

    return edges


def getresult(match_reward: int, mismatch_penalty:int, indel_penalty:int, s: str, t: str):

    edges = LinearSpaceAlignment(match_reward, mismatch_penalty, indel_penalty, s, t, 0, len(s), 0, len(t))

    string1 = ''
    string2 = ''
    currt = 0
    currs = 0
    for e in edges:
        
        if e == 'Right':
            string1 += '-'
            string2 += t[currt]
            currt += 1
        elif e == 'Down':
            string1 += s[currs]
            string2 += '-'
            currs += 1
        elif e == 'Diagonal':
            string1 += s[currs]
            string2 += t[currt]
            currs += 1
            currt += 1
    
    score = getscore(s, t, indel_penalty ,match_reward, mismatch_penalty)

    return (score, string1, string2)

file = open('Chapter5(2)\dataset_865452_14.txt')
file.readline()
s = file.readline().strip()
t = file.readline().strip()
#s = 'GAGA'
#t = 'GAT'
mr = 1
mp = 1
ip = 5

result = getresult(mr, mp, ip, s, t)

for r in result:
    print(r)