def spiralOrder(matrix):
    """
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

    示例 1：
    输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
    输出：[1,2,3,6,9,8,7,4,5]

    示例 2：
    输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    输出：[1,2,3,4,8,12,11,10,9,5,6,7]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    if not matrix:
        return []
    if len(matrix) == 1:
        return matrix[0]
    if len(matrix[0]) == 1:
        return [matrix[i][0] for i in range(len(matrix))]
    traveled = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
    i, j = 0, 0
    res = []
    directs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0
    while not traveled[i][j]:
        traveled[i][j] = 1
        res.append(matrix[i][j])
        next_i, next_j = i + directs[d][0], j + directs[d][1]
        if (not 0 <= next_i < len(matrix)) or (not 0 <= next_j < len(matrix[i])) or traveled[next_i][next_j]:
            d = (d + 1) % 4
        i, j = i + directs[d][0], j + directs[d][1]
    return res


if __name__ == '__main__':
    a1 = spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
    a2 = spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    a3 = spiralOrder([])
    a4 = spiralOrder([[1]])
    a5 = spiralOrder([[2, 3]])
    a6 = spiralOrder([[3], [2]])
    pass
