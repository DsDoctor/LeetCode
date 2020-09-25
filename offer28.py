def isSymmetric(root):
    def is_symmetric(l, r):
        if not l and not r:
            return True
        if not l or not r or l.val != r.val:
            return False
        return is_symmetric(l.left, r.right) and is_symmetric(l.right, r.left)
    return is_symmetric(root.left, root.right) if root else True


if __name__ == '__main__':
    from tools.tree import build_tree
    null = None
    t1 = build_tree([1,2,2,3,4,4,3])
    a1 = isSymmetric(t1)
    t2 = build_tree([1,2,2,null,3,null,3])
    a2 = isSymmetric(t2)
    pass
