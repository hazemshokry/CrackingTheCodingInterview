# Given two strings, write a method to decide if one is a permutation of the other.
# Example, Dog is considered a permutation of God.

def checkPermutation (string1, string2):
    """
    :param string1: string #1 to check if it is considered as a permutation for string #2.
    :param string2: string #2 to check if it is considered as a permutation for string #1.
    :return: True if one string is a permutation of the other, False otherwise.
    """
    if sorted(string1.lower()) == sorted(string2.lower()):
        return True
    return False

if __name__ == '__main__':
    print(checkPermutation("dOg","God"))