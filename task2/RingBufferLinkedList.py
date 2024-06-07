class RingBufferLinkedList:

    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = self.Node()
        self.tail = self.head
        self.size = 0

    def push(self, value):
        if self.size == self.capacity:
            raise Exception("RingBuffer is full")
        self.tail.value = value
        self.tail.next = self.Node()
        self.tail = self.tail.next
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception("RingBuffer is empty")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value
