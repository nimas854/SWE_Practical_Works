import time

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
   
    fib_list = []
    if n <= 0:
        return fib_list
    a, b = 0, 1
    fib_list.append(a)
    for _ in range(1, n):
        fib_list.append(b)
        a, b = b, a + b
    return fib_list

def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

def fibonacci_up_to_n(n):

    return fibonacci_iterative(n)

def index_of_first_exceeding_fibonacci(value):
   
    a, b = 0, 1
    index = 0
    while a <= value:
        a, b = b, a + b
        index += 1
    return index

def is_fibonacci_number(x):
    if x < 0:
        return False
    a, b = 0, 1
    while a < x:
        a, b = b, a + b
    return a == x

def fibonacci_ratios(n):

    ratios = []
    fib_list = fibonacci_up_to_n(n)
    for i in range(2, len(fib_list)):
        ratio = fib_list[i] / fib_list[i - 1]
        ratios.append(ratio)
    return ratios


if __name__ == "__main__":
    n = 30
    
    
    fib_list = fibonacci_up_to_n(n)
    print(f"Fibonacci numbers up to F({n}): {fib_list}")

    
    value = 50
    index = index_of_first_exceeding_fibonacci(value)
    print(f"Index of first Fibonacci number exceeding {value}: {index}")

    
    test_number = input("Enter a number:")

    if test_number is is_fibonacci_number:
        print("True")
    else:
        print("false")
  

    
    ratios = fibonacci_ratios(n)
    print(f"Ratios between consecutive Fibonacci numbers up to F({n}): {ratios}")

    
    recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
    iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

    print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
    print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")

    memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
    print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")







        
