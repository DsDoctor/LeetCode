def numWays(n):
    """
    一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
    答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

    示例 1：
    输入：n = 2
    输出：2

    示例 2：
    输入：n = 7
    输出：21

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    if n <= 1:
        return 1
    step0, step1 = 1, 1
    for i in range(1, n):
        step = step1 + step0
        step0, step1 = step1, step
    return step % 1000000007


if __name__ == '__main__':
    a1 = numWays(2)
    a2 = numWays(7)
    pass
