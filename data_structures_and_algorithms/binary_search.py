def linear_search(data, target):
    for i in data:
        if i == target:
            return True
    return False

def binary_search_iterative(data, target):
    i = 0
    j = len(data) - 1

    while i <= j:
        mid = (i + j) // 2

        if data[mid] == target:
            return True
        elif data[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
    return False

def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2

        if data[mid] == target:
            return True
        elif data[mid] > target:
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, high)

def find_highest_number(A):
    low = 0
    high = len(A) - 1

    if len(A) < 3:
        return None
    
    while low <= high:
        mid = (low + high) // 2
        mid_left = A[mid - 1] if mid-1 >= 0 else float('-inf')
        mid_right = A[mid + 1] if mid+1 < len(A) else float('inf')

        if mid_left < A[mid] and mid_right > A[mid]:
            low = mid + 1
        elif mid_left > A[mid] and mid_right < A[mid]:
            high = mid - 1
        elif mid_left < A[mid] and mid_right < A[mid]:
            return A[mid]

def find(A, target):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if A[mid - 1] != target:
                return mid
            high = mid - 1

def integer_square_root(k):    
    low = 0
    high = k 

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1

data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 37

print(linear_search(data, target))
print(binary_search_iterative(data, target))
print(binary_search_recursive(data, target, 0, len(data)-1))


A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 2, 3, 4, 5]
print(find_highest_number(A))
A = [5, 4, 3, 2, 1]
print(find_highest_number(A))

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108
print(find(A, target))

k = 300
print(integer_square_root(k))