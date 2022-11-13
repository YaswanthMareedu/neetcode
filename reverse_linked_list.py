class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        curr=head
        while curr!=None:
            a.append(curr.val)
            curr=curr.next
        
        a=a[::-1]
        i=0
        curr=head
        while curr!=None:
            curr.val=a[i]
            i+=1
            curr=curr.next
        return head