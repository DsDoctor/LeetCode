class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    """
    将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

    示例：
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    head = ListNode()
    node = head
    while l1 and l2:
        if l1.val <= l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next
    node.next = l1 if l1 else l2
    return head.next


if __name__ == '__main__':
    l1 = ListNode(-9)
    l1.next = ListNode(3)
    # l1.next.next = ListNode(4)
    l2 = ListNode(5)
    l2.next = ListNode(7)
    # l2.next.next = ListNode(4)
    a1 = mergeTwoLists(l1, l2)
    pass
