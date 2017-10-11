def rBinarySearch(list,element):
    if len(list) == 1:
        return element == list[0]
    mid = len(list)/2
    if list[mid] > element:
        return rBinarySearch( list[ : mid] , element )
    if list[mid] < element:
        return rBinarySearch( list[mid : ] , element)
    return True
