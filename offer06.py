class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reversePrint(head):
    """
    输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

    示例 1：
    输入：head = [1,3,2]
    输出：[2,3,1]
    """
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res[::-1]


if __name__ == '__main__':
    LinkList = ListNode(1)
    LinkList.next = ListNode(3)
    LinkList.next.next = ListNode(2)
    a1 = reversePrint(LinkList)
    pass
