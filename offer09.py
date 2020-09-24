class CQueue:
    """
    用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
    分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

    示例 1：
    输入：
    ["CQueue","appendTail","deleteHead","deleteHead"]
    [[],[3],[],[]]
    输出：[null,null,3,-1]

    示例 2：
    输入：
    ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
    [[],[],[5],[2],[],[]]
    输出：[null,-1,null,null,5,2]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def __init__(self):
        self.push_s = []
        self.pop_s = []

    def appendTail(self, value):
        while self.pop_s:
            self.push_s.append(self.pop_s.pop())
        self.push_s.append(value)

    def deleteHead(self):
        while self.push_s:
            self.pop_s.append(self.push_s.pop())
        return self.pop_s.pop() if self.pop_s else -1


if __name__ == '__main__':
    obj = CQueue()
    obj.appendTail(3)
    param = obj.deleteHead()
    param = obj.deleteHead()

    obj = CQueue()
    param = obj.deleteHead()
    obj.appendTail(5)
    obj.appendTail(2)
    param = obj.deleteHead()
    param = obj.deleteHead()
    pass
