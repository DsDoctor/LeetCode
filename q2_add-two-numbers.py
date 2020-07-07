class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# def addTwoNumbers(l1, l2):
#     int1 = 0
#     int2 = 0
#     pos = 1
#     while l1:
#         int1 += pos*l1.val
#         l1 = l1.next
#         pos *= 10
#     pos = 1
#     while l2:
#         int2 += pos*l2.val
#         l2 = l2.next
#         pos *= 10
#     res = int1 + int2
#     root = ListNode(res % 10)
#     pos = 1
#     res //= 10 * pos
#     node = root
#     while res:
#         node.next = ListNode(res % 10)
#         node = node.next
#         res //= 10 * pos
#     return root

def addTwoNumbers(l1, l2):
    res = ListNode(0)
    node = res
    while l1 or l2:
        if node.next is None:
            node.next = ListNode(0)
        if l1 and not l2:
            val = node.next.val + l1.val
            l1 = l1.next
        elif l2 and not l1:
            val = node.next.val + l2.val
            l2 = l2.next
        else:
            val = l1.val + l2.val + node.next.val
            l1, l2 = l1.next, l2.next
        if val > 9:
            node.next.next = ListNode(1)
        node.next.val = val % 10
        node = node.next
    return res.next


if __name__ == '__main__':
    l1 = ListNode(9)
    l1.next = ListNode(1)
    l1.next.next = ListNode(6)
    l2 = ListNode(0)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)
    root = addTwoNumbers(l1, l2)
    pass
