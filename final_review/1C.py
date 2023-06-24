class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


def print_reverse(dll_head):
    current = dll_head

    # Traverse to the last node
    while current.next is not None:
        current = current.next

    # Traverse backward and print the values
    while current is not None:
        print(current.value)
        current = current.prev