class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_link_list(lis):
    if not lis:
        return None
    head = ListNode(lis[0])
    node = head
    lis = lis[1:]
    while lis:
        node.next = ListNode(lis[0])
        lis = lis[1:]
        node = node.next
    return head


if __name__ == '__main__':
    lis = create_link_list([1,4,9,5])
    pass
