"""
Queue class used for Problem 1
"""
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

"""
Node class used for Problem 2-5
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, node):
        self.next = node



"""
1. Stack2 class
Implement stack data structure using queue
"""
class Stack2:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.buffer = Queue()
        
    def isEmpty(self):
        return self.q1.isEmpty()
    
    def push(self, item):
        if self.q1.isEmpty():
            self.q1.enqueue(item)
        
        else:
            q1Size = self.q1.size()
            
            for i in range(q1Size):
                obj = self.q1.items[-1]
                self.q2.enqueue(obj)
                self.q1.dequeue()
            
            self.q1.enqueue(item)
            
            for j in range(q1Size):
                obx = self.q2.items[-1]
                self.q1.enqueue(obx)
                self.q2.dequeue()
    
    def pop(self):
        return self.q1.dequeue()
    
    def peek(self):
        return self.q1.items[-1]
    
    def size(self):
        return len(self.q1.items)


"""
2. transform(lst)
Transform an unordered list into a Python list
Input: an (possibly empty) unordered list
Output: a Python list
"""
def transform(lst):
    def len_link(s):
        if not s:
            return 0
        else:
            return 1 + len_link(rest(s))
    
    def rest(s):
        assert s.getData() != None 
        return s.getNext()

    lst1 = []
    
    for i in range(len_link(lst)):
        lst1.append(lst.getData())
        lst = lst.getNext()
    
    return lst1




"""
3. concatenate(lst1, lst2)
Concatenate two unordered lists
Input: two (possibly empty) unordered list
Output: an unordered list
"""
def concatenate(lst1, lst2):
    
    if not lst1:
        return lst2
    
    if not lst2:
        return lst1
    
    end = lst1
    
    while end.next != None:
        end = end.next
    
    end.next = lst2
    
    return lst1





"""
4. removeNodesFromBeginning(lst, n)
Remove the first n nodes from an unordered list
Input:
    lst -- an (possibly empty) unordered list
    n -- a non-negative integer
Output: an unordred list
"""
def removeNodesFromBeginning(lst, n):
    if n <= 0:
        return lst
    curr = lst   
    while n > 0:
        curr = curr.getNext()
        n -= 1
    return curr



"""
5. removeNodes(lst, i, n)
Starting from the ith node, remove the next n nodes
(not including the ith node itself).
Assume i + n <= lst.length(), i >= 0, n >= 0.
Input:
    lst -- an unrdered list
    i -- a non-negative integer
    n -- a non-negative integer
Output: an unordred list

lst = [1, 2, 3, 4, 5]
i = 2
n = 2
return [1, 2, 5]

i = 1
n = 2
return [1, 4, 5]

i = 0
n = 2
return [3, 4, 5]
"""
def removeNodes(lst, i, n):
    j = i
    if i != 0:
        start = lst
        j -= 1
    
        while j > 0:
            start = start.next
            j -= 1
        
        end = start
        
    else:
        end = lst

    while n > 0:
        end = end.next
        n -= 1    
    
    if i != 0:
        start.next = end.next
    else:
        lst = end
    return lst








