"""
Problem 1
"""
def smallest(plist):
    if len(plist) == 1:
        return int(plist[0])
    if  len (plist) == 2 and type(plist) is list:
        plist.sort()
        return plist[0]
    if len(plist) <= 2:
        return int(str(plist))
    else:
        plist.sort(reverse = True)
        plist = plist.pop()
        return smallest(str(plist))


"""
Problem 2 (linear version)
"""
"""Linear Version"""
def linearSearchValueIndexEqual(plist):
    lst = []
    for i in range(len(plist)):
        if i == plist[i]:
            lst.append(plist[i])
    return lst



"""
Problem 2 (binary version)
"""
"""Binary Version"""
def binarySearchValueIndexEqual(plist):
    lst = []
    for i in range(len(plist)):
        item = search_binary(plist, i)
        if item == plist[i]:
            lst.append(item)
    
    return lst

def search_binary(plist, item):
        left = 0
        right = len(plist) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if item == plist[mid]:
                return mid
            elif item < plist[mid]:
                right = mid - 1
            else:
                left = mid + 1



"""
Problem 4
"""
from collections import Counter

def anonymousLetter(book, letter):
    bookCount = Counter(book)
    letterCount = Counter(letter)
    if letter == "":
        return True
    match = False
    for key in letterCount:
        if key not in bookCount:
            return False
        if letterCount[key] <= bookCount[key]:
            match = True
        else:
           return False

    if match == True:
        return True

