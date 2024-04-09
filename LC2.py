#   Palindrome Number
# Given an integer x, return true if x is a
# palindrome,
# and false otherwise

def isPalindrome(x):
    str_num = str(x)
    new_num = ''
    for i in range(len(str_num), 0, -1):
        new_num += str_num[i-1]
    return new_num == str_num


# print(isPalindrome(1221))

def isPalindrome2(x):
    str_num = str(x)
    new_num = str_num[::-1]
    if new_num == str_num:
        return True
    else:
        return False


def isPalindrome3(x):
    # str_num = str(x)
    new_num = ''
    for i in range(len(str(x)), 0, -1):
        new_num += str_num[i-1]
    return new_num == str_num

print(isPalindrome(1221))