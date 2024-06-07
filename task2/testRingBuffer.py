import RingBufferArray
import RingBufferLinkedList

# [] -> [1] -> [1, 2] -> [1, 2, 3] -> [2, 3] -> [2, 3, 4] -> [3, 4] -> [4] - > [] fill and clear
def caseFillAndClear(RingBuffer):
    buffer = RingBuffer(3)
    buffer.push(1)
    buffer.push(2)
    buffer.push(3)
    if buffer.pop() != 1:
        return False
    buffer.push(4)
    if buffer.pop() != 2:
        return False
    if buffer.pop() != 3:
        return False
    if buffer.pop() != 4:
        return False
    return True


# [] -> error empty
def caseErrorEmpty(RingBuffer):
    buffer = RingBuffer(3)
    try:
        buffer.pop()
        return False
    except Exception as e:
        if e.args[0] != "RingBuffer is empty":
            return False
        return True



# [] -> [1] -> error full
def caseErrorFull(RingBuffer):
    buffer = RingBuffer(1)
    try:
        buffer.push(1)
        buffer.push(2)
        return False
    except Exception as e:
        if e.args[0] != "RingBuffer is full":
            return False
        return True


# [] -> [1] -> [1, 2] -> [2] -> [] -> [3] -> [3, 4] -> [3, 4, 5] -> [4, 5] -> [5] fill after clear
def caseFillAfterClear(RingBuffer):
    buffer = RingBuffer(3)
    buffer.push(1)
    buffer.push(2)
    if buffer.pop() != 1:
        return False
    if buffer.pop() != 2:
        return False
    buffer.push(3)
    buffer.push(4)
    buffer.push(5)
    if buffer.pop() != 3:
        return False
    if buffer.pop() != 4:
        return False
    return True


def testRingBuffer(RingBuffer):
    assert caseFillAndClear(RingBuffer)
    assert caseErrorEmpty(RingBuffer)
    assert caseErrorFull(RingBuffer)
    assert caseFillAfterClear(RingBuffer)
    print("All tests passed.")

if __name__ == "__main__":
    print("Testing RingBufferArray")
    testRingBuffer(RingBufferArray.RingBufferArray)
    print("Testing RingBufferLinkedList")
    testRingBuffer(RingBufferLinkedList.RingBufferLinkedList)
