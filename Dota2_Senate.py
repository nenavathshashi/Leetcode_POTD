from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r=deque()
        d=deque()
        n=len(senate)
        for i in range(n):
            if senate[i]=="R":
                r.append(i)
            else:
                d.append(i)
        j=0
        while(r and d):
            pos1=r.popleft()
            pos2=d.popleft()
            if pos1<pos2:
                r.append(n+j)
            else:
                d.append(n+j)
            j+=1
        if r:
            return 'Radiant'
        else:
            return 'Dire'
