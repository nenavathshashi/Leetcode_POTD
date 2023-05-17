class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l=[]
        start=head
        while(start) :
            l.append(start.val) 
            start=start.next
        ptr=0
        ptr1=len(l)-1
        maxi=float('-inf') 
        while(ptr<ptr1) :
            #print(l[ptr], l[ptr1]) 
            maxi=max(maxi, l[ptr]+l[ptr1]) 
            ptr+=1
            ptr1-=1
        return maxi
