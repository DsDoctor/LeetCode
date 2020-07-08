def longestCommonPrefix(strs):
    """
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 ""。

    示例 1:
    输入: ["flower","flow","flight"]
    输出: "fl"

    示例 2:
    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。
    说明:
    所有输入只包含小写字母 a-z 。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/longest-common-prefix
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    i = 0
    res = ''
    if not strs:
        return ''
    length = min(len(s) for s in strs)
    while i < length:
        for j in range(len(strs)):
            if not strs[j][i] == strs[0][i]:
                break
        else:
            res += strs[0][i]
            i += 1
            continue
        break
    return res


if __name__ == '__main__':
    a1 = longestCommonPrefix(["flower", "flow", "flight"])
    a2 = longestCommonPrefix(["dog", "racecar", "car"])
    pass
