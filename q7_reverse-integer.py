def reverse(x):
    """
    给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

    示例 1:
    输入: 123
    输出: 321

    示例 2:
    输入: -123
    输出: -321

    示例 3:
    输入: 120
    输出: 21

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/reverse-integer
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    if x >= 0:
        res = int(str(x)[::-1])
        return res if res < 2**31 else 0
    else:
        res = -int(str(-x)[::-1])
        return res if -2**31 <= res else 0


if __name__ == '__main__':
    a1 = reverse(123)
    a2 = reverse(-123)
    a3 = reverse(120)
    a4 = reverse(1534236469)
    a5 = reverse(-2147483648)
    pass
