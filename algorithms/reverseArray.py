import math
import array as arr

# reverse array

def reverseArray(array):
    # loop up until the midpoint in array for odd numbers math.floor array length / 2
    length = len(array)
    mid = math.floor(length/2)

    for i in range(mid):
        # create a temp var to hold value
        temp = array[i]

        # with first iteration begin by assigning the first index of array to last item in array
        # and assign the last item in array to the first value stored in temp
        # then continue swapping values of array at indices as you continue moving toward the mid point in array from both ends
        array[i] = array[length - 1 - i]
        array[length - 1 - i] = temp

    return array

result = reverseArray([1, 2, 3, 4, 5])
print(result)

arrayOfIntegers = arr.array('i', [1, 2, 3])
print(reverseArray(arrayOfIntegers))