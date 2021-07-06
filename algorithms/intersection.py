# takes two arguments (each an array/list) as input
# [1, 2, 4, 4, 5, 2, 10, 11], [2, 5, 2, 7, 8, 11, 7, 9]
# arrays/lists are unsorted

# 1) Create a set from array1 to remove duplicates
# 2) initialize a new array result
# 3) Loop through elements in the set created from array1 and check if array2 includes the element
# 4) if array2 does include the element push this element to the result array
# 5) after loop ends return the result array

def intersection(list1, list2):
    setOfItems = list(set(list1))
    result = []

    for item in setOfItems:
        if item in list2:
            result.append(item)

    return result

print(intersection([1, 2, 4, 4, 5, 2, 10, 11], [2, 5, 2, 7, 8, 11, 7, 9])) # [2, 5, 11]


