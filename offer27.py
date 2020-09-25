class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mirrorTree(root):
    if not root:
        return None
    node = root.left
    root.left = mirrorTree(root.right) if root.right else None
    root.right = mirrorTree(node) if node else None
    return root


if __name__ == '__main__':
    from tools.tree import build_tree
    t1 = build_tree([4,2,7,1,3,6,9])
    a1 = mirrorTree(t1)
    pass
