class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, header):
        next = self.head
        self.head = header
        self.head.next = next

    def search(self, x):
        current = self.head
        i = 0
        while current:
            if current.data == x:
                print(i, current.data)
                break
            i += 1
            current = current.next

    def delete_node(self, x):
        previous = self.head
        current = previous.next
        if previous.data == x:
            self.head = current
            return
        while current:
            if current.data == x:
                previous.next = current.next
                break
            previous = current
            current = current.next


father = Node("Bob")
mother = Node("Amy")
first_child = Node("Macy")
second_child = Node("Steven")
family = LinkedList()
family.head = father

father.next = mother
mother.next = first_child
first_child.next = second_child

family.traversal()
uncle = Node("Dave")

family.insert_new_header(uncle)

family.traversal()

family.search("Amy")

family.delete_node("Steven")

family.traversal()