# Input (7 -> 1 -> 6) + (5 -> 9 -> 2) -- 617 + 295
# Input 2 -> 1 -> 9 -- 912
import LinkedList

def linkedlist_sum_list (ls1, ls2, carry):
    ls1_current = ls1.head
    ls2_current = ls2.head
    result = LinkedList.LinkedList
    value = carry

    while ls1_current or ls2_current:
        if ls1:
            value += ls1_current.value
            ls1_current = ls1_current.next
        if ls2:
            value = ls2_current.value
            ls2_current = ls2_current.next


if __name__ == '__main__':

    linked_list1 = LinkedList.LinkedList(LinkedList.Node(7))
    linked_list1.insert(1)
    linked_list1.insert(6)

    linked_list2 = LinkedList.LinkedList(LinkedList.Node(5))
    linked_list2.insert(9)
    linked_list2.insert(2)

    print("ls1: " , linked_list1.print())
    print("ls2: " , linked_list2.print())

    print("-------------------------")

    #print("ls1 value: " + linkedlist_sum_list(linked_list1,linked_list2))
