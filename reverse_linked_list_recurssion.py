# Definition for singly-linked list.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        ans=self.reverseList(head.next)
        q=head.next
        q.next=head
        head.next=None
        return ans
        