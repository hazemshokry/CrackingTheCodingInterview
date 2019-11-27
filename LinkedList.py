class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

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

    def insert_at(self, value, position):
        new_node = Node(value)

        if position < 0:
            print("Invalid position - " + str(position))
            return

        if position is 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current:
            current = current.next

        current_next = current.next
        current.next = new_node
        new_node.next = current_next

    def delete_last(self):
        current = self.head

        if current is None:
            print("Empty list")
            return

        prev = None
        while current.next is not None:
            prev = current
            current = current.next

        prev.next = None

    def print(self):
        current = self.head
        result = ""
        while current:
            result += str(current.value) + " -> "
            current = current.next
        print(result[:-4])


if __name__ == '__main__':
    linked_list = LinkedList(Node(1))

    linked_list.insert(2)
    linked_list.insert(7)
    linked_list.insert(5)
    linked_list.insert(7)

    linked_list.print()
