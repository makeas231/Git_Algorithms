 
def binary_search(list, el):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == el:
            return mid
        elif list[mid] > el:
            high = mid - 1
        elif list[mid] < el:
            low = mid + 1
    return None

list_ = [1, 2, 3, 6, 8, 12]
print(binary_search(list_, 8))

        
            