"""
TASK: 03 Queue Simulation

# Queue Simulation using OOP
Make a Queue class with:
- enqueue, dequeue, peek, size
Simulate customers joining/leaving.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

class Queue():
    def __init__(self):
        self.values = []
        self.size = 0

    def enqueue(self, value):
        self.values.append(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return "Queue empty"
        self.size -= 1
        return self.values.pop(0)

    def peek(self):
        if self.size == 0:
            return "Queue empty"
        return self.values[0]

def main():
    customers = Queue()
    customers.enqueue("Pat")
    customers.enqueue("John")
    customers.enqueue("Lynnie")
    print(f"Dequeuing:\t{customers.dequeue()}")
    print(f"Peeking:\t{customers.peek()}")
    print(f"Dequeuing:\t{customers.dequeue()}")
    customers.enqueue("Ben")
    print(f"Peeking:\t{customers.peek()}")
    customers.enqueue("Alice")
    print(f"Size:\t{customers.size}")

if __name__ == "__main__":
    main()
