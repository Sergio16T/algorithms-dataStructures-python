# remove duplicates from list

def removeDuplicatesWithSet(listOfItems):
    return list(set(listOfItems))

def removeDuplicates(list):
    result = []
    for item in list:
        if item not in result:
            result.append(item)

    return result

print(removeDuplicatesWithSet([1, 2, 2, 4, 1, 3, 3])) # [1, 2, 3, 4]
print(removeDuplicates([1, 2, 2, 4, 1, 3, 3])) # [1, 2, 4, 3]
