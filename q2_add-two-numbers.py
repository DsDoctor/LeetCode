class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    两数相加

    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

    示例：
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/add-two-numbers
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
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
