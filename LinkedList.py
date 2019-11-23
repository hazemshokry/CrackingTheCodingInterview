class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        current = self.head
        previous = None

        if current.value == value:
            self.head = current.next

        while current.next:
            if current.value == value:
                previous.next = current.next
                break
            else:
                previous = current

            current = previous.next

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


if __name__ == '__main__':
    linked_list = LinkedList(Node(1))
    linked_list.insert(2)
    linked_list.insert(7)
    linked_list.insert(5)
    linked_list.insert(7)
    linked_list.insert_at_beginning(0)
    linked_list.delete(7)

    linked_list.print()
