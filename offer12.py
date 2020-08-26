def exist(board, word):
    """
    请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
    路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
    如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
    例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

    [["a","b","c","e"],
    ["s","f","c","s"],
    ["a","d","e","e"]]

    但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

    示例 1：
    输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    输出：true

    示例 2：
    输入：board = [["a","b"],["c","d"]], word = "abcd"
    输出：false

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def dfs(i, j, n):
        if not 0 <= i < len(board) or not 0 <= j < len(board[i]) or board[i][j] != word[n]:
            return False
        if n == len(word)-1:
            return True
        temp, board[i][j] = board[i][j], '/'
        res = dfs(i+1, j, n+1) or dfs(i-1, j, n+1) or dfs(i, j+1, n+1) or dfs(i, j-1, n+1)
        board[i][j] = temp
        return res

    for i in range(len(board)):
        for j in range(len(board[i])):
            if dfs(i, j, 0):
                return True
    return False


if __name__ == '__main__':
    a1 = exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], 'ABCCED')
    a2 = exist([["a", "b"], ["c", "d"]], 'abcd')
    a3 = exist([["a", "a"]], 'aaa')
    a4 = exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], 'ABCEFSADEESE')
    pass
