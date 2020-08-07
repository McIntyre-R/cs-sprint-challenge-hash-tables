def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for e in arrays:
        for k in e:
            if k in cache:
                cache[k] += 1
            else:
                cache[k] = 1
    result = [x for x in cache if cache[x] == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
