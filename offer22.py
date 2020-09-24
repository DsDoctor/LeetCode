class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getKthFromEnd(head, k):
    node = head
    for i in range(k):
        node = node.next
    while node:
        head = head.next
        node = node.next
    return head


if __name__ == '__main__':
    from tools.link_list import create_link_list
    l1 = create_link_list([1,2,3,4,5])
    a = getKthFromEnd(l1, 2)
    pass
