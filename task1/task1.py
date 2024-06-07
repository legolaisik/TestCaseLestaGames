def isEven(value):
    return value & 1 == 0


def isEvenEtalon(value):
    return value % 2 == 0


if __name__ == '__main__':
    for value in range(-100, 100):
        if isEven(value) != isEvenEtalon(value):
            print(f"Incorrect result. Expected {isEvenEtalon(value)},"
                  f" Received {isEven(value)} when the value is {value}")
    else:
        print("All integer tests correct")
