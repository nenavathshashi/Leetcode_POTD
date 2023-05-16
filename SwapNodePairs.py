class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr=head
        if not ptr:
            return ptr
        ptr1=head.next
        while(ptr and ptr1) :
            print(ptr.val, ptr1.val) 
            ptr.val, ptr1.val=ptr1.val, ptr.val
            ptr=ptr1.next
            if ptr:
                ptr1=ptr.next
        return head
