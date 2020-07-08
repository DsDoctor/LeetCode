def isValid(s):
    dic = {'(': ')',
           '[': ']',
           '{': '}'}
    stack = []
    for ch in s:
        if ch in dic:
            stack.append(ch)
        elif stack:
            if dic[stack.pop()] != ch:
                return False
        else:
            return False
    return not stack


if __name__ == '__main__':
    a1 = isValid('()')
    a2 = isValid('()[]{}')
    a3 = isValid('(]')
    a4 = isValid('([)]')
    a5 = isValid('{[]}')
    a6 = isValid(']')
    pass
