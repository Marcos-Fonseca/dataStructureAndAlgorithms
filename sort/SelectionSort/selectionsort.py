import random

def SelectionSort(vector):
    index = 0

    while index < len(vector):
        minimum = vector[index]

        for x in range(index+1, len(vector)):
            if minimum > vector[x]:
                minimum = vector[x]

        index2 = vector.index(minimum)
        vector[index], vector[index2] = vector[index2], vector[index]
        index += 1

if __name__ == "__main__":
    vector = [x for x in range(100)]
    random.shuffle(vector)

    print(f'original vector = {vector}')
    SelectionSort(vector)
    print(f'sorted vector = {vector}')