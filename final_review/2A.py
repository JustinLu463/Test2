from time import time
from doublylinkedlist import DoublyLinkedList

def unknown(n: int):
    # unnecessary code

num_trials = 50
for n in range(1000,50001,1000):
    t1 = time()
    for t in range(num_trials):
        unknown(n)
    t2 = time()
    print(f"{(t2-t1)/num_trials:.6f}")