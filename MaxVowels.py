class Solution:
    def maxVowels(self, s: str, k: int) -> int:
    
        sets={'a','e','i','o','u'}
        maxi=0
        ptr=0
        n=len(s)
        
        count=0
        for i in range(k):
            if s[i] in sets:
                count+=1
        maxi=count
        ptr=0
        ptr1=k
        while(ptr<n and ptr1<n) :
            if s[ptr] in sets:
                count-=1
            if s[ptr1] in sets:
                count+=1
            maxi=max(count,maxi) 
            ptr+=1
            ptr1+=1
        return maxi