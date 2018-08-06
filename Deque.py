# -*- coding: utf-8 -*-


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


# 回文检查
def palChecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    isEqual = True

    while chardeque.size() > 1 and isEqual:
        if chardeque.removeFront() != chardeque.removeRear():
            isEqual = False

    return isEqual

print(palChecker('12345ss54321'))