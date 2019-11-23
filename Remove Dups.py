# Write code to remove duplicates from an unsorted linked list.
import LinkedList

def remove_dups(linked_list):
    dict = {}
    current = linked_list.head
    previous = None
    while current.next:
        if current.value in dict:
            previous.next = current.next
        else:
            previous = current
            dict[current.value] = ''

        current = previous.next
    print(dict)


if __name__ == '__main__':
    linked_list = LinkedList.LinkedList(LinkedList.Node(1))
    linked_list.insert(3)
    linked_list.insert(7)
    linked_list.insert(8)
    linked_list.insert(7)
    linked_list.insert(568)

    remove_dups(linked_list)
    linked_list.print()
