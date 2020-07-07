def twoSum(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        if num in dic:
            return [dic[num], i]
        else:
            dic[target - num] = i


if __name__ == '__main__':
    print(twoSum([-3,4,3,90], 0))
