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

print("sir party")