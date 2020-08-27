class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(head, val):
    """
    给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
    返回删除后的链表的头节点。
    注意：此题对比原题有改动

    示例 1:
    输入: head = [4,5,1,9], val = 5
    输出: [4,1,9]
    解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

    示例 2:
    输入: head = [4,5,1,9], val = 1
    输出: [4,5,9]
    解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    if head.val == val:
        return head.next
    tmp = head
    while tmp.next:
        if tmp.next.val == val:
            if tmp.next.next:
                tmp.next = tmp.next.next
            else:
                tmp.next = None
            return head
        else:
            tmp = tmp.next


if __name__ == '__main__':
    l1 = ListNode(4)
    l1.next = ListNode(5)
    l1.next.next = ListNode(1)
    l1.next.next.next = ListNode(9)
    a1 = deleteNode(l1, 5)

    pass
