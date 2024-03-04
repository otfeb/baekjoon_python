# linked list 생성
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        init = Node(input())
        self.head = init
        self.tail = init

    def append(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode

l = LinkedList()
l.append(input())
l.append(input())
l.append(input())

print(l.head.next.data)