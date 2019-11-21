# Implement a method to perform basic string compression using the counts of repeated characters.
# For example: the string aabcccccaaa would be a2b1c5a3.
# Note: if the new string is larger than the older one, return the original.

def stringCompression(string):
    """
    :param string:
    :return: return a new string after compression
    """
    if len(string) == 0:
        return string

    count = 0
    finalString = ""
    curr = string[0]

    for c in string:
        if curr == c:
            count += 1
        elif curr != c:
            finalString += curr + str(count)
            count = 1
            curr = c
    finalString += curr + str(count)
    if len(finalString) > len(string):
        return string
    return finalString

if __name__ == '__main__':
    print(stringCompression("aabcccccaaa"))

