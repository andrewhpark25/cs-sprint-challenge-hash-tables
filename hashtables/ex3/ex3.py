def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = dict()
    result = []
    
    for arr in arrays:
        for n in arr:
            if n in cache:
                cache[n] += 1
                if cache[n] == len(arrays):
                    result.append(n)
            else:
                cache[n] = 1


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
