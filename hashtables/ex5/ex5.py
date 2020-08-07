# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for e in queries:
        cache[e] = []
    for k in files:
        kspli = k.split('/')
        if kspli[len(kspli)-1] in cache:
            cache[kspli[len(kspli)-1]].append(k)
    for e in cache.items():
        result += e[1]
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
