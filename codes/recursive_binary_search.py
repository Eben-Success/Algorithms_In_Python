def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        mid = (len(list) // 2)

        if list[mid] == target:
            return True

        else:
            if list[mid] < target:
                return recursive_binary_search(list[mid+1:], target)
            else:
                if list[mid] > target:
                    return recursive_binary_search(list[:mid], target)
