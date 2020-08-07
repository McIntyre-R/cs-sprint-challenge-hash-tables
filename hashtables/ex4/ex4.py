def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for e in a:
        if abs(e) in cache:
            cache[abs(e)] += 1
        else:
            cache[abs(e)] = 0
    result = [x for x in cache if cache[x] == 1]


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
