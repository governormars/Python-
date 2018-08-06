# -*- coding: utf-8 -*-


# 结点类
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.data = newnext


# 无序链表,链表本身不包含任何节点对象，它只保留对于头节点的引用
class UnorderedList:
    def __init__(self):
        self.head = None

    # def getheaddata(self):
    #     return self.head.getData()

    def isEmpty(self):
        return self.head == None

    # 链表在头节点之前添加新的节点，如 A->B->C->D->None,节点E加入，变成E->A->B->C->D->None,链表head指向E
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # 如果删除第一个节点的话，对应的链表head也需要移动
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext)


mylist = UnorderedList()
mylist.add(1)
print(mylist.search(1))
# mylist.add(2)
# print(mylist.size())
# print(mylist.isEmpty())
# print(mylist.head.getData())
# # mylist.remove(5)
# print(mylist.search(6))
node1 = Node(5)
print(node1.getData())