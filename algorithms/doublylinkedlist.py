class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head == None:
            print("the list is empty")
        else:
            print(self.head.data)
            next = self.head.next
            while next is not None:
                print("-", next.data)
                next = next.next


    def insert_head(self, info):
        node = Node(data=info)
        if self.head:
            node.next = self.head
            self.head.prev = node
        self.head = node

    def insert_after(self, prev, info):
        node = Node(data=info)
        node.prev = prev
        next_current = prev.next
        prev.next = node
        node.next = next_current

    def insert_before(self, next, info):
        node = Node(data=info)
        node.next = next
        current_prev = next.prev
        current_prev.next = node

    def append(self, info):
        if self.head == None:
            print("the list is empty")
        else:
            new_node = Node(data=info)
            next_node = self.head.next
            while next_node.next is not None:
                next_node = next_node.next
            next_node.next = new_node


dl = DLinkedList()
dl.insert_head("Father")
dl.insert_after(dl.head,"Mother")
dl.traversal()
dl.insert_after(dl.head.next, "Daughter1")
dl.traversal()
dl.insert_after(dl.head.next, "Son")
dl.traversal()
dl.append("Cat")
dl.traversal()
dl.append("Dog")
/dl.traversal()
dl.insert_head("GrandMa")
dl.traversal()


