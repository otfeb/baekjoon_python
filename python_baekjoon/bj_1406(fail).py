# linked list 생성
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, data):
        init = Node(data)
        self.head = init
        self.tail = init

    def append(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

    def cursorInit(self):
        cur_node = self.tail
        return cur_node
        
    def cursor(self, command):
        cur_node = self.tail
        if command == 'L':
            if cur_node.prev is not None:
                cur_node = cur_node.prev
                self.tail = self.tail.prev
                return cur_node
        elif command == 'D':
            if cur_node.next is not None:
                cur_node = cur_node.next
                self.tail = self.tail.next
                return cur_node

    def insert(self, data, node):
        new_node = Node(data)
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        new_node.prev = node

        if new_node.next is None:
            self.tail = new_node


    def delete(self, prev_node):
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next

s = input()
m = int(input())

for i in range(len(s)):
    if i == 0:
        link = LinkedList(s[i])
    else:
        link.append(s[i])

first_cursor = link.cursorInit()

for i in range(m):
    command = list(input().split())
    c1 = command[0]

    cursor = link.cursorInit()

    if c1 == 'L':
        cursor = link.cursor(c1)
    elif c1 == 'D':
        cursor = link.cursor(c1)
    elif c1 == 'B':
        link.delete(cursor.prev)
    else:
        if link.tail == first_cursor:
            link.insert(command[1],cursor)
        else:
            link.insert(command[1],cursor.prev)

def printNodes(node:Node):
    crnt_node = node
    while crnt_node is not None:
        print(crnt_node.data, end='')
        crnt_node = crnt_node.next

printNodes(link.head)