class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start=head
        length=0
        while(start):
            length+=1
            start=start.next
        fromstart=length-k
        ptr=head
        ptr1=head
        while(k!=1) :
            ptr=ptr.next
            k-=1
        while(fromstart) :
            ptr1=ptr1.next
            fromstart-=1
        ptr.val, ptr1.val=ptr1.val, ptr.val
        return head
        
