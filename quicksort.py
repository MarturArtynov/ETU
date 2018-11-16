def sort(array):
    left = []
    middle = []
    right = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                left.append(x)
            if x == pivot:
                middle.append(x)
            if x > pivot:
                right.append(x)
        return sort(less)+equal+sort(greater)  
    else:  
        return array
