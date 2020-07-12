def findRepeatNumber(nums):
    dic = {}
    for n in nums:
        if dic.get(n):
            return n
        else:
            dic[n] = True


if __name__ == '__main__':
    a1 = findRepeatNumber([2, 3, 1, 0, 2, 5, 3])
    pass
