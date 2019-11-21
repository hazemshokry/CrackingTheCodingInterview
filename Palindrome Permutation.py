# Given a string, write a function to check if it's a permutation of palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.
# Example - Input: Tact Coa -- Output: True ("taco cat, atco cta, etc...)

def palindromePermutation(string):
    """
    :param string: string to check whether it has a permutation or not
    :return: True if this string has a permeation, False otherwise
    """
    string = string.lower()
    dict = {char: string.count(char) for char in string if char != " "}
    oddCount = 0
    for i in dict:
        if dict[i] % 2 == 1:
            oddCount += 1
    if oddCount % 2 == 0:
        return False
    return True

if __name__ == '__main__':
    print(palindromePermutation("carerac"))