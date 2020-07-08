def isPalindrome(x):
    return True if str(x) == str(x)[::-1] else False


if __name__ == '__main__':
    a1 = isPalindrome(121)
    a2 = isPalindrome(-121)
    a3 = isPalindrome(10)
    pass
