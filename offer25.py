class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    if not (l1 and l2):
        return l1 if l2 is None else l2
    if l1.val <= l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next
    node = head
    while l1 and l2:
        if l1.val <= l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next
    if l1:
        node.next = l1
    elif l2:
        node.next = l2
    return head


if __name__ == '__main__':
    from tools.link_list import create_link_list
    l1 = create_link_list([1,2,4])
    l2 = create_link_list([1,3,4])
    a = mergeTwoLists(l1,l2)
    pass
