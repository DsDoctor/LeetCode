def myPow(x, n):
    """
    实现函数double Power(double base, int exponent)，求base的exponent次方。
    不得使用库函数，同时不需要考虑大数问题。

    示例 1:
    输入: 2.00000, 10
    输出: 1024.00000

    示例2:
    输入: 2.10000, 3
    输出: 9.26100

    示例3:
    输入: 2.00000, -2
    输出: 0.25000
    解释: 2-2 = 1/22 = 1/4 = 0.25

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    # if n == 0:
    #     return 1
    # elif n > 0:
    #     res = 1
    #     for _ in range(n):
    #         res *= x
    #     return res
    # else:
    #     res = 1
    #     for _ in range(-n):
    #         res *= (1/x)
    #     return res
    return x**n


if __name__ == '__main__':
    a1 = myPow(2.00000, 10)
    a2 = myPow(2.1000, 3)
    a3 = myPow(2.0000, -2)
    pass
