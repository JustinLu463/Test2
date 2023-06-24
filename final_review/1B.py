class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def flip(head):
    if head is None or head.next is None:
        return head

    current = head
    prev = None

    # Traverse to the last node
    while current.next is not None:
        prev = current
        current = current.next

    # Move the last node to the front
    prev.next = None
    current.next = head
    head = current

    return head
