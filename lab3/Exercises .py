import time
import math
import random

def linear_search(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices if indices else -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left  

comparison_count = 0

def count_comparisons(func):
 
    def wrapper(*args, **kwargs):
        global comparison_count
        comparison_count = 0
        result = func(*args, **kwargs)
        return result
    return wrapper

@count_comparisons
def binary_search_with_count(arr, target):
   
    left, right = 0, len(arr) - 1
    
    while left <= right:
        global comparison_count
        mid = (left + right) // 2
        comparison_count += 1 
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left  

def jump_search(arr, target):
   
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return prev
    return -1

def compare_search_algorithms(arr, target):
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time

    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search_with_count(arr_sorted, target)
    binary_time = time.time() - start_time

    start_time = time.time()
    jump_result = jump_search(arr_sorted, target)
    jump_time = time.time() - start_time
    
    print(f"Linear Search: Found at indices {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Comparisons: {comparison_count}, Time: {binary_time:.6f} seconds")
    print(f"Jump Search: Found at index {jump_result}, Time: {jump_time:.6f} seconds")

def main():
    test_list = [random.randint(1, 10) for _ in range(20)]  # Smaller range for repeat values
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  
    print(f"\nSearching for: {target}")
    
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at indices {result}")
    
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(10000)), random.randint(0, 9999))

if __name__ == "__main__":
    main()






        
