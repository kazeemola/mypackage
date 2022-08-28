def top_n(items, n):
    """Return the top n items in a list, in descending order.
    Args:
    items (list): list or array-like object containing numerical values.
    n (int): number of top items to return.
    Returns:
        list: top n items, in descending order.
    Examples:
        >>> top_n([8,3,2,7,4], 3)
        [8,7,4]
    """
    for i in range(n): # Keep sorting until we have the top n items
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:   #if this item is bigger than the next item..
                items[j], items[j+1] = items[j+1], items[j]    #swap the two!

    # Get the last two items
    top_n = items[-n:]
    # Return in descending order
    return top_n[::-1]
    