import random

def quickSort(vector):
    def _quickSort(v):
        if len(v) > 1:

            return _quickSort([x for x in v[1:] if x < v[0]]) + [v[0]] + \
                _quickSort([x for x in v[1:] if x > v[0]])
        else:
            return v

    # that keep the reference
    vector[:] = _quickSort(vector)

if __name__ == "__main__":
    vector = [x for x in range(100)]
    random.shuffle(vector)

    print(f'original vector = {vector}')
    quickSort(vector)
    print(f'sorted vector = {vector}')