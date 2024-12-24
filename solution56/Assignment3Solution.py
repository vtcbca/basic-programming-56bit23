def fibonacci_for_loop(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Test the function
terms = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence (first {terms} terms): {fibonacci_for_loop(terms)}")