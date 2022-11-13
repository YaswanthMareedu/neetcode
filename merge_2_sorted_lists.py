class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=curr=ListNode()

        while list1 and list2:
            if list1.val<list2.val:
                curr.next = list1
                curr=list1
                list1=list1.next
            else:
                curr.next=list2
                curr=list2
                list2=list2.next
        if list1:
            curr.next=list1

        else:
            curr.next=list2
        return dummy.next