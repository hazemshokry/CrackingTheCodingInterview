# Assume you have a method isSubstring which checks if one word is substring of another.
# Given two strings s1, s2 write code to check if s2 is a rotation of s1
# using only one call to isSubstring (eg. waterbottle is a rotation of erbottlewat

def isSubstring (s1, s2):
    """
    :param s1:
    :param s2:
    :return: True if one string is a substring of the another
    """
    if s1 in s2:
        return True
    elif s2 in s1:
        return True
    else:
        return False

def stringRotation (s1, s2):
    """
    :param s1:
    :param s2:
    :return: True if s2 is a rotation of S1
    """
    if len(s1) != len(s2) and len(s1) > 0:
        return False

    return isSubstring(s1+s1, s2)

if __name__ == '__main__':
    print(stringRotation("waterbottle", "erbottlewat"))
