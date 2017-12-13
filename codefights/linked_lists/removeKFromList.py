# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    curr = l
    while curr:
        if curr.next and curr.next.value == k:
            curr.next = curr.next.next
        else:
            curr = curr.next
    if l and l.value == k:
        return l.next
    return l
    

