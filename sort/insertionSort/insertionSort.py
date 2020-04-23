import random

def insertionSort(vector):
    for x in range(1, len(vector)):
        element = vector[x]
        index = x

        while index > 0 and vector[index-1] > element:
            vector[index] = vector[index-1]
            index -= 1
        else:
            vector[index] = element

if __name__ == "__main__":
    vector = [x for x in range(100)]
    random.shuffle(vector)

    print(f'original vector = {vector}')
    insertionSort(vector)
    print(f'sorted vector = {vector}')