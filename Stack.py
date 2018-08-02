# -*- coding: utf-8 -*-

# python栈的实现
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# s = Stack()
#
# s=Stack()
#
# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())

# 括号匹配

def parChecker(symbol):
    s = Stack()
    balanced = True
    index = 0
    while balanced and index < len(symbol):
        x = symbol[index]
        if x == '(':
            s.push(x)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

# print(parChecker('(((())))'))
# print(parChecker('(((()))))'))

# 符号匹配


def parChecker2(symbol):
    s = Stack()
    balanced = True
    index = 0
    while balanced and index < len(symbol):
        x = symbol[index]
        if x in '([{':
            s.push(x)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, x):
                    balanced = False

        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

# print(parChecker2('{{([][])}()}'))
# print(parChecker2('[{()]'))

# 十进制转二进制


def divideBy2(decNumber):
    s = Stack()
    while decNumber > 0:
        rest = decNumber % 2
        s.push(rest)
        decNumber = decNumber // 2

    binString = ""
    while not s.isEmpty():
        binString = binString + str(s.pop())

    return binString

# print(divideBy2(142857))


# 改进，变成十进制转换为任何进制(2~16)

def divideByn(decNumber, base):
    digits = "0123456789ABCEDF"
    s = Stack()
    while decNumber > 0:
        rest = decNumber % base
        s.push(rest)
        decNumber = decNumber // base

    binString = ""
    while not s.isEmpty():
        binString = binString + digits[s.pop()]

    return binString

# print(divideByn(123456789, 16))

