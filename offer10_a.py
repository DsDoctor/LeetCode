def fib(n):
    """
    写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
    F(0) = 0, F(1) = 1
    F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
    斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
    答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

    示例 1：
    输入：n = 2
    输出：1

    示例 2：
    输入：n = 5
    输出：5

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    # from math import sqrt
    # s5 = sqrt(5)
    # return int((1/s5)*(((1+s5)/2)**n-((1-s5)/2)**n) % 1000000007)
    if n < 2:
        return n
    fib_1, fib_2 = 0, 1
    for i in range(1, n):
        fib_n = fib_1 + fib_2
        fib_1, fib_2 = fib_2, fib_n
    return fib_n % 1000000007


if __name__ == '__main__':
    a1 = fib(2)
    a2 = fib(5)
    a3 = fib(45)
    a4 = fib(72)
    pass
