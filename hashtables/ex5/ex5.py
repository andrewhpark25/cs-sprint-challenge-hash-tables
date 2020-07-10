# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = dict()
    result = []
    
    for path in files:
        item = path.split('/')[-1]
        # append path if item in cache
        if item in cache:
            cache[item].append(path)
        # create a list with path if not 
        else:
            cache[item] = [path]
      # check if each query in cache
    for query in queries:
        if query in cache:
            # add to result if in cache
           result.extend(cache[query])
                
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
