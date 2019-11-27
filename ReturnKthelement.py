# Implement an algorithm to find the kth to the last element of a singly linked list.
import LinkedList

def return_kth_element(ls, k):
    current = ls.head
    i = 0
    while current:
        if ls.size-k == i:
            return current.value
        i += 1
        current = current.next

def return_kth_element_2(ls, k):
    p1 = ls.head
    p2 = ls.head

    for i in range (k):
        if p1 is None:
            return None
        p1 = p1.next

    while p1:
        p1 = p1.next
        p2 = p2.next

    return p2.value




if __name__ == '__main__':
    linked_list = LinkedList.LinkedList(LinkedList.Node(1))
    linked_list.insert(2)
    linked_list.insert(7)
    linked_list.insert(5)
    linked_list.insert(7)
    linked_list.insert_at_beginning(0)

    print("Kth element from last: " + str(return_kth_element(linked_list, 3)))
    print("Kth element from last: " + str(return_kth_element_2(linked_list, 3)))

    linked_list.print()