def reverseWords(s):
    return ' '.join([_[::-1] for _ in s.split(' ')])


if __name__ == '__main__':
    print(reverseWords("Let's take LeetCode contest"))
