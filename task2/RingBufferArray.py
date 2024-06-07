class RingBufferArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.readIndx = 0
        self.writeIndx = 0
        self.isFull = False
        self.isEmpty = True

    def push(self, value):
        if self.isFull:
            raise Exception("RingBuffer is full")
        self.buffer[self.writeIndx] = value
        self.writeIndx = (self.writeIndx + 1) % self.capacity
        self.isEmpty = False
        if self.writeIndx == self.readIndx:
            self.isFull = True

    def pop(self):
        if self.isEmpty:
            raise Exception("RingBuffer is empty")
        value = self.buffer[self.readIndx]
        self.buffer[self.readIndx] = None
        self.readIndx = (self.readIndx + 1) % self.capacity
        self.isFull = False
        if self.writeIndx == self.readIndx:
            self.isEmpty = True
        return value
