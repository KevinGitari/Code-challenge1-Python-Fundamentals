#Calculate factoriol

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

    
if __name__ == "__main__":
    test_cases = [5, 0, 3, 7]
    for n in test_cases:
        result = calculate_factorial(n)
        print(f"The factorial of {n} is {result}")

