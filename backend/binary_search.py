numbers = [2, 5, 8, 12, 16]

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1