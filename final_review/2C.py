from time import time
from doublylinkedlist import DoublyLinkedList

def unknown(n: int):
    # unnecessary code

num_trials = 200
t1 = time()
for t in range(num_trials):
    unknown(100)
t2 = time()
print((t2-t1)/num_trials)

