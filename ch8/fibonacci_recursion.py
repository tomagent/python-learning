import time

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(20,55,5): #Complete the fibonacci numbers from 20 all the way to 50, counting by fives
    start = time.time() # Start timer
    result = fibonacci(i) # Compute fibonacci
    end = time.time() # End timer
    duration = end - start # Compute duration
    print(i, result, duration) 