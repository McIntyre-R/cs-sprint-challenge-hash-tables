#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for e in tickets:
        cache[e.source] = e.destination
    route = [cache['NONE']]
    i = 0
    current = route[i]
    while current != 'NONE':
        route.append(cache[route[i]])
        i += 1
        current = cache[route[i]]
    route.append(cache[route[i]])
    return route

