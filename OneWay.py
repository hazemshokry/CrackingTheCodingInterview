# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.

def oneWay (string1, string2):
    """
    :param string1:
    :param string2:
    :return: return True if they are one edit or zero edits, False otherwise.
    """
    if abs(len(string1) - len(string2)) > 1:
        return False
    elif (len(string1) == len(string2)):
        return checkForReplacement(string1,string2)
    else:
        return checkForInsertOrRemove(string1,string2)


def checkForInsertOrRemove(string1, string2):
    """
    :param string1:
    :param string2:
    :return: return True iff both are identical but one string has one more character
    """
    smallString = min(string1,string2)
    largeString = max(string1,string2)

    i = 0 # Used for indexing in the small string
    j = 0 # Used for indexing in the large string
    while (i < len(smallString) and j < len(largeString)):
        if smallString[i] != largeString[j] :
            if (i != j):
                return False
            j+=1
        i+=1
        j+=1
    return True

def checkForReplacement(string1, string2):
    """
    :param string1:
    :param string2:
    :return: return True iff both are identical but not for one character.
    """
    if string1 == string2:
        return True

    flag = False
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            if flag:
                return False
            flag = True
        else:
            continue
    return True

if __name__ == '__main__':
    print(oneWay("pale", "ple"))
    print(oneWay("pales", "pale"))
    print(oneWay("pale", "bale"))
    print(oneWay("pale", "bae"))
    print(oneWay("Hazem", "Hazeem"))