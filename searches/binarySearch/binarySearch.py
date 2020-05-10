import time

def binarySearch(vector, element):
    leftPointer = 0
    rightPointer = len(vector) -1
    mediumPosition = (rightPointer - leftPointer) // 2

    while mediumPosition < rightPointer:
        if vector[mediumPosition] == element:
            return mediumPosition

        if element < vector[mediumPosition]:
            rightPointer = mediumPosition
        elif element > vector[mediumPosition]:
            leftPointer = mediumPosition + 1

        mediumPosition = ((rightPointer - leftPointer) // 2) + leftPointer

    return -1


if __name__ == "__main__":
    vector = [x for x in range(1000)]

    assert binarySearch(vector, 5) == 5
    assert binarySearch(vector, 1001) == -1
    assert binarySearch(vector, 57) == 57
    assert binarySearch(vector, -13) == -1
