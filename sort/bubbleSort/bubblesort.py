import random

def bubbleSort(vector):
    changed = True
    
    while changed:
        changed = False

        for x in range(len(vector)-1):
            if vector[x] > vector[x+1]:
                vector[x], vector[x+1] = vector[x+1], vector[x]
                changed = True

if __name__ == "__main__":
    vector = [x for x in range(100)]
    random.shuffle(vector)

    print(f'original vector = {vector}')
    bubbleSort(vector)
    print(f'sorted vector = {vector}')