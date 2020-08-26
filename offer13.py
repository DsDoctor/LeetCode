def movingCount(m, n, k):
    """
    地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
    一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
    也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，
    因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
    请问该机器人能够到达多少个格子？

    示例 1：
    输入：m = 2, n = 3, k = 1
    输出：3

    示例 2：
    输入：m = 3, n = 1, k = 0
    输出：1

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    matrix = [[0 for j in range(n)] for i in range(m)]

    def dfs(m, n):
        if not 0 <= m < len(matrix) or not 0 <= n < len(matrix[0]):
            return 0
        if sum(int(s) for s in str(m)) + sum(int(s) for s in str(n)) > k:
            return 0
        if not matrix[m][n]:
            matrix[m][n] = 1
            return 1 + dfs(m+1, n) + dfs(m, n+1) + dfs(m-1, n) + dfs(m, n-1)
        else:
            return 0

    return dfs(0, 0)


if __name__ == '__main__':
    a1 = movingCount(2, 3, 1)
    a2 = movingCount(3, 1, 0)
    a3 = movingCount(16, 8, 4)
    pass
