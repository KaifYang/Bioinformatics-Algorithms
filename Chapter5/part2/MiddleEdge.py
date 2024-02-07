from collections import defaultdict

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
                next = (i+1, mid)
            elif ts_col[i][1] == 'right':
                next = (i, mid+1)
            elif ts_col[i][1] == 'diagonal':
                next = (i+1, mid+1)

    return (midnode, next)

file = open('Chapter5(2)\dataset_865452_12.txt')
file.readline()
t = file.readline().strip()
s = file.readline().strip()

#s = 'AATCCC'
#t = 'T'

mr = 1
mp = 1
ip = 5

result = MiddleEdge(s, t, ip, mr, mp)

for r in result:
    print(r[0], end=' ')
    print(r[1])