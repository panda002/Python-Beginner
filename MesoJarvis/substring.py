def ExactSame(str1, str2):
    size1 = len(str1)
    size2 = len(str2)
    if size1 == 0:
        return False
    if size2 == 0:
        return True
    if str1[0] == str2[0]:
        return ExactSame(str1[1:], str2[1:])
    return False


def issubstring(str1, str2):
    size1 = len(str1)
    size2 = len(str2)
    if size1 == 0:
        return False
    if size2 == 0:
        return True
    if str1[0] == str2[0]:
        return ExactSame(str1, str2)
    return issubstring(str1[1:], str2)


str1 = 'SIDHARTH'
str2 = 'SID'

print(issubstring(str1, str2))
