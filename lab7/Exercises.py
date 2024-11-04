def quick_sort_in_place(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


test_arr = [64, 34, 25, 12, 22, 11, 90]
quick_sort_in_place(test_arr, 0, len(test_arr) - 1)
print("In-Place Quick Sort Result:", test_arr)

def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  
    return arr


test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort_optimized(test_arr.copy())
print("Optimized Bubble Sort Result:", sorted_arr)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_hybrid(arr):
    if len(arr) <= 10:  
        insertion_sort(arr.copy())
        return arr
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort_hybrid(arr[:mid])
    right = merge_sort_hybrid(arr[mid:])
    
    return merge(left, right)

test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort_hybrid(test_arr)
print("Hybrid Merge Sort Result:", sorted_arr)
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort_hybrid(test_arr)
print("Hybrid Merge Sort Result:", sorted_arr)

import matplotlib.pyplot as plt

def visualize_bubble_sort(arr):
    n = len(arr)
    plt.ion() 
    fig, ax = plt.subplots()
    bar_container = ax.bar(range(len(arr)), arr, align="center")
    ax.set_ylim(0, max(arr) + 10)
    plt.title("Bubble Sort Visualization")
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
                
                for rect, height in zip(bar_container, arr):
                    rect.set_height(height)
                
                plt.pause(0.1)  
        if not swapped:
            break
    
    plt.ioff()  
    plt.show()

test_arr = [64, 34, 25, 12, 22, 11, 90]
visualize_bubble_sort(test_arr.copy())
