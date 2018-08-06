# -*- coding: utf-8 -*-


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


# 丢手绢问题(直到剩下一个人）
def hotPotato(namelist, number):
    circlequeue = Queue()
    for name in namelist:
        circlequeue.enqueue(name)

    while circlequeue.size() > 1:
        for i in range(number):
            circlequeue.enqueue(circlequeue.dequeue())

        circlequeue.dequeue()

    return circlequeue.dequeue()

print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 8))