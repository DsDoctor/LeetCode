class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    """
    定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

    示例:
    输入: 1->2->3->4->5->NULL
    输出: 5->4->3->2->1->NULL

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    node = None
    while head:
        temp, head.next = head.next, node
        node, head = head, temp
    return node


if __name__ == '__main__':
    link_list = ListNode(1)
    link_list.next = ListNode(2)
    link_list.next.next = ListNode(3)
    link_list.next.next.next = ListNode(4)
    link_list.next.next.next.next = ListNode(5)
    a = reverseList(link_list)
    pass

# temp, head.next = head.next, node
# node, head = head, temp