# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.
    '''
    Special cases? 
    1. They could have different number of digits! 
    2. The sum could have an extra digit!
    '''
    head = result = ListNode(0)
    while l1 or l2:
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0

        digitSum = l1Val + l2Val + c
        c = 1 if digitSum >= 10 else 0
        digitSum %= 10

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

        result.val = digitSum
        result.next = ListNode(c) if l1 or l2 or c else None
        result = result.next
    return head

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print result.val, 
  result = result.next
# 7 0 8