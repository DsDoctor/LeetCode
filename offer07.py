class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    """
    输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
    例如，给出
    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]
    返回如下的二叉树：
        3
       / \
      9  20
        /  \
       15   7

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    if not len(preorder) == len(inorder):
        return None
    if len(inorder) == 0:
        return None
    root = TreeNode(preorder[0])
    left_in = inorder[:inorder.index(preorder[0])]
    right_in = inorder[inorder.index(preorder[0])+1:]
    left_pre = preorder[1:len(left_in)+1]
    right_pre = preorder[len(left_in)+1:]
    root.left = buildTree(left_pre, left_in)
    root.right = buildTree(right_pre, right_in)
    return root


if __name__ == '__main__':
    a1 = buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    pass
