# Write code to partition a linked list around a value x.
# such that all nodes less than x come before all nodes greater than x.
# Input: 3 -> 5 -> 8 -> 5 -> 2 -> 1 (partition around 5)
# output: 3 -> 1 -> 2 -> 5 -> 5 -> 5

import LinkedList


def partition_linked_list(ls, p):
    current = ls.head
    left = LinkedList.LinkedList()
    right = LinkedList.LinkedList()

    while current:
        if current.value < p:
            left.insert(current.value)
            left.head = current.next
        else:
            right.insert(current.value)
        current = current.next

    print("left: " + left.print())
    print("right: " + right.print())
    print(left.head.value)
    print(right.head.value)

    left.head.next = right.head
    return left



if __name__ == '__main__':
    linked_list = LinkedList.LinkedList(LinkedList.Node(1))
    linked_list.insert(2)
    linked_list.insert(7)
    linked_list.insert(5)
    linked_list.insert(7)
    linked_list.insert_at_beginning(0)
    linked_list = partition_linked_list(linked_list, 5)

    linked_list.print()
