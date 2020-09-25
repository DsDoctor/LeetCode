null = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree(lis):
    if not lis:
        return None
    lis = [TreeNode(v) if v else None for v in lis]
    root = lis.pop(0)
    stack = [root]
    while stack:
        node = stack.pop(0)
        if not lis:
            return root
        node.left = lis.pop(0)
        if node.left:
            stack.append(node.left)
        if not lis:
            return root
        node.right = lis.pop(0)
        if node.right:
            stack.append(node.right)
    return root


if __name__ == '__main__':
    a1 = build_tree([1,null,2,3])
    a2 = build_tree([3,4,5,1,2])
    pass
