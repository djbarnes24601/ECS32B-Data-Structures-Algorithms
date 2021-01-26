class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print("pop() error: Stack is empty.")
            return None

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("peek() error: Stack is empty.")
            return None

    def size(self):
        return len(self.items)


"""
1. postfixEval
Input type: a list of strings
Output type: a floating point number
"""
def postfixEval(expr):
    s = Stack()
    
    for i in range(len(expr)):
        if isFloat(expr[i]):
            s.push(float(expr[i]))
        else:
            b = s.pop()
            a = s.pop()
            result = compute(expr[i], a, b)
            s.push(result)
    
    
    return s.pop()

def compute(operator, operand1, operand2):
    if operator == "*":
        return operand1 * operand2
    if operator == "-":
        return operand1 - operand2
    if operator == "+":
        return operand1 + operand2
    if operator == "/":
        return operand1/operand2

def isFloat(n):
    if n in "*+/-":
        return False
    else:
        return True


"""
2. validParentheses
Input type: a string
Output type: a Boolean
"""

"""
The function iterates through the string. If it finds starting parantheses it will push it to the stack
and if it finds an ending parantheses it will check to see if it has a cooresponding starting parentheses
in the stack. If this is true it will then remove it.
"""
def validParentheses(str):
    s = Stack() # create our stack
    valid = True
    i = 0 # index for while loop

    if len(str) == 1:
        return False

    while i < len(str):
        if str[i] in "{[(":
            s.push(str[i])
        else:
            if s.isEmpty(): # check if stack is empty
                valid = True
                return valid
            else:
                if str[i] in "{[()]}": # The function should only be removing brackets and parentheses and skip over alphabet letters. 
                    if matches(s.peek(), str[i]):
                        s.pop()
        i += 1
    
    if s.isEmpty() and valid:
        return True
    else:
        return False

"""
Matches is our helper function that detects whether or not
the top of the stack matches the current index in the string.
"""
def matches(top, base):
    opens = "([{"
    closers = ")]}"
    return opens.index(top) == closers.index(base)
    

    return valid

"""
3. reverseString
Input type: a string
Output type: a string
"""
def reverseString(s):
    stack = Stack() # create Stack
    reversedStr = "" # reversed string to be returned
    
    for i in range(len(s)):
        stack.push(s[i]) # pushes all chars into the stack
        
    for j in range(stack.size()):
        reversedStr = reversedStr + stack.pop() # removes all chars from the stack and appends to reversedStr

    return reversedStr # return our reversed string
        
        







