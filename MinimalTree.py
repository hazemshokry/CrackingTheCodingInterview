# Given a sorted (increasing order) array with unique integers elements,
# write an algorithm to create a binary tree with minimal height.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def minimal_tree (arr):
    minimal_tree_helper(arr, 0, len(arr)-1)


def minimal_tree_helper (arr, left, right):
    if left > right:
        return
    else:
        mid_index = int((left+right) / 2)
        print("Inserting node..." + str(arr[mid_index]))
        node = Node(arr[mid_index])
        node.left = minimal_tree_helper(arr, left, mid_index-1)
        node.right = minimal_tree_helper(arr, mid_index+1, right)
        return node



if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    minimal_tree(arr)