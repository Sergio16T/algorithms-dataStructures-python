import math
# reverse array

def reverseArray(array):
    # loop up until the midpoint in array for odd numbers math.floor array length / 2
    length = len(array)
    mid = math.floor(length/2)

    for i in range(mid):
        # create a temp var to hold value
        temp = array[i]
        # length 3
        # index 3 - 1 - 0 which is 2
        array[i] = array[length - 1 - i] # assign first index of array to last item in array
        array[length - 1 - i] = temp # assign last item in array to value stored in temp variable

    return array

result = reverseArray([1, 2, 3, 4, 5])
print(result)