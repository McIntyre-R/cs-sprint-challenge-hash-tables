def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for e in range(length):
        if weights[e] in cache:
            return [e, cache[weights[e]]]
        needed = limit - weights[e]
        cache[needed] = e

            
    return None
