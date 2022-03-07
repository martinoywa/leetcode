# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases
        if list1 == None and list2 == None:
            return None
        # when end of one list but not the other
        if list1 and list2 == None:
            return list1
        if list2 and list1 == None:
            return list2
        
        # megred
        merged = ListNode(None)
        
        # current for merged list
        c3 = merged
        
        # iteratate
        # comparing currents
        # if one less than other
        # add, then update current of other
        while list1 and list2:
            if list1.val < list2.val:
                c3.next = ListNode(list1.val)
                c3 = c3.next
                list1 = list1.next
            elif list2.val < list1.val:
                c3.next = ListNode(list2.val)
                c3 = c3.next
                list2 = list2.next
            else:
                c3.next = ListNode(list1.val)
                c3.next.next = ListNode(list2.val)
                c3 = c3.next.next
                list1 = list1.next
                list2 = list2.next
                
            # when end of one list but not the other
            if list1 and list2 == None:
                c3.next = list1
                break
            if list2 and list1 == None:
                c3.next = list2
                
        return merged.next
                
        
