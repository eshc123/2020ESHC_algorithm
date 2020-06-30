# https://comdoc.tistory.com/entry/%EC%9B%90%ED%98%95-%EC%97%B0%EA%B2%B0-%EB%A6%AC%EC%8A%A4%ED%8A%B8Circular-linked-list-ADT-%ED%8C%8C%EC%9D%B4%EC%8D%AC 참고

class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = Node(0)
        self.head.next = self.head
        self.size = 1


    def find(self, item):
        cur_node = self.head
        while cur_node.element != item:
            cur_node = cur_node.next
        return cur_node
    def insert(self, new, item):
        new_node = Node(new)
        cur_node = self.find(item)
        new_node.next = cur_node.next
        cur_node.next = new_node
        self.size +=1


    def show(self):
        cur_node = self.head
        while cur_node.next.element != 0:
            print(cur_node.element, end=' -> ')
            cur_node = cur_node.next
        print(cur_node.element)


    def find_previous(self, item):
        cur_node = self.head
        while (cur_node.next is not None) and (cur_node.next.element != item):
            cur_node = cur_node.next
        return cur_node

    def find_next(self, item):
        cur_node = self.head
        while (cur_node.next is not None) and (cur_node.next.element != item):
            cur_node = cur_node.next
        return cur_node.next.next

    def remove(self, item):
        prev_node = self.find_previous(item)
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next
        self.size -= 1

T = int(input())
for i in range(T):
    N,K = map(int, input().split())
    cll = CircularLinkedList()
    cll.insert(0,0)
    cl=cll.head
    print(cl.element)
    for j in range(1,N):
        cll.insert(j,j-1)
        cl = cl.next
        print(cl.element)
    cl.next=cll.head
    el = 1
    while cll.size > 1 :
        r = cll.find(el)
        r1 = r
        for k in range(0,K):
            r1 = r1.next
        el = r1.element
        print(el)
        cll.remove(r.element)
    print(cll.head.element+1,cll.head.next.element+1)
