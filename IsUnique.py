# Write an algorithm to determine if a string has all unique characters.

def isUnique(string):
    """
    :param string: string is in ASCII characters and in key sensitive format.
    :return: True if all characters are unique in a given string, False otherwise.
    """
    dict = {}
    for char in string:
        if char in dict:
            return False
        else:
            dict[char] = 1
    return True

if __name__ == '__main__':
    print(isUnique("Hazem Sayed"))