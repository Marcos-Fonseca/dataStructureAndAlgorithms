import random

def SelectionSort(vector):
    sortedVector = []

    while len(vector) > 0:
        min = vector[0]

        for x in range(1, len(vector)):
            if min > vector[x]:
                min = vector[x]

        sortedVector.append(min)
        del(vector[vector.index(min)]) # delete selected element from original vector

    return sortedVector

if __name__ == "__main__":
    vector = [x for x in range(100)]
    random.shuffle(vector)

    print(f'original vector = {vector}')
    vector = SelectionSort(vector)
    print(f'sorted vector = {vector}')