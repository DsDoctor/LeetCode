def isSubStructure(A, B):
    def is_sub_tree(t1, t2):
        if not t2:
            return True
        if not t1 or t1.val != t2.val:
            return False
        return is_sub_tree(t1.left, t2.left) and is_sub_tree(t1.right, t2.right)
    if A is None or B is None:
        return False
    return is_sub_tree(A, B) or isSubStructure(A.left, B) or isSubStructure(A.right, B)


if __name__ == '__main__':
    from tools.tree import build_tree
    t1 = build_tree([1,2,3])
    t2 = build_tree([3,1])
    a1 = isSubStructure(t1, t2)
    t1 = build_tree([3,4,5,1,2])
    t2 = build_tree([4,1])
    a2 = isSubStructure(t1, t2)
    pass
