# Implement an algorithm to delete a node in linkedlist from middle.
# Any node but fist and last.

import LinkedList


def delete_from_middle(ls, value):
    current = ls.head
    previous = None

    if current.value == value:
        ls.head = current.next
        ls.size -= 1

    while current.next:
        if current.value == value:
            previous.next = current.next
            ls.size -= 1
            break
        else:
            previous = current

        current = previous.next


if __name__ == '__main__':
    linked_list = LinkedList.LinkedList(LinkedList.Node(1))
    linked_list.insert(2)
    linked_list.insert(7)
    linked_list.insert(5)
    linked_list.insert(7)
    linked_list.insert_at_beginning(0)

    delete_from_middle(linked_list, 5)

    linked_list.print()