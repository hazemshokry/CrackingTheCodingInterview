# Write a method to replace all spaces in string with '%20'. You may assume that string has sufficient space at the end
# to hold the additional characters, and that you are given the "tru" length of the string.

def urlify(string, length):
    """
    :param string: url that needs to be urlified.
    :param length: the actual length of the string that needs to be urlified.
    :return: new string that have every space replaced with '%20'
    """
    res = ["%20" if c == " " else c for c in string[:length]]
    return ''.join(res)


if __name__ == '__main__':
    print(urlify("Mr John Smith        ", 13))
