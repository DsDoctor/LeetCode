def isNumber(s):
    """
    请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
    例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，
    但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    import re
    # 正负号 数字.数字 e 指数
    patten = '^(\+|\-)?((\d+\.?\d*)|(\d*\.?\d+))((e|E)(\+|\-)?\d+)?$'
    res = re.match(patten, s.strip())
    return res is not None

    # try:
    #     float(s)
    #     return True
    # except ValueError:
    #     return False


if __name__ == '__main__':
    y1 = isNumber('+100')
    y2 = isNumber('-123')
    y3 = isNumber('5e2')
    y4 = isNumber('3.1416')
    y5 = isNumber('-1E-16')
    y6 = isNumber('0123')
    y7 = isNumber('.1')
    y8 = isNumber('8.')
    y9 = isNumber('-1.')
    y10 = isNumber('46.e3')
    y11 = isNumber(' 005047e+6')
    n7 = isNumber('12e')
    n8 = isNumber('1a3.14')
    n9 = isNumber('1.2.3')
    n10 = isNumber('+-5')
    n11 = isNumber('12e+5.4')
    n12 = isNumber('.')
    n13 = isNumber('0e')
    pass
