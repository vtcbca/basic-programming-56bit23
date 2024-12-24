# Method 1: Using a Simple For Loop with String Formatting
def print_triangle(n):
    for i in range(1, n+1):
        # Print leading spaces for alignment
        print(' ' * (n - i), end='')
        # Print numbers in increasing order
        for j in range(1, 2*i):
            print(j, end=' ')
        print()  # Move to the next line

input_lines = int(input("Enter the number of rows: "))  # Input number of rows
print_triangle(input_lines)
