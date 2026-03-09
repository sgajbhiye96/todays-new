def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

print(even_odd(10))  # Output: Even
print(even_odd(7))   # Output: Odd

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


import math

def factorial_builtin(n):
    if n < 0 or not isinstance(n, int):
        # The built-in function handles this, but adding a check improves clarity/specific error messages
        raise ValueError("Factorial is only defined for non-negative integers.")
    return math.factorial(n)

# Example usage:
number = 5
print(f"The factorial of {number} is {factorial_builtin(number)}") 
# Output: The factorial of 5 is 120
