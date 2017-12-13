# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    head = l
    if head is None:
        return True

    fast = slow = head
    # find the mid point
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half
    p, curr = slow.next, None
    while p:
        next = p.next
        p.next = curr
        curr, p = p, next

    # check palindrome
    p1, p2 = curr, head
    while p1 and p1.value == p2.value:
        p1, p2 = p1.next, p2.next

    return p1 is None

