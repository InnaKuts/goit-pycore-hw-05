def caching_fibonacci():
    # Creating dictionary for caching results
    cache = {}

    def fibonacci(n):
        # Exeptions check
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # Cache check
        if n in cache:
            return cache[n]
        
        # Calculations with recursion & saving it in cache
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result

    return fibonacci

# Examples
fib = caching_fibonacci()
print(fib(10))  
print(fib(15))  