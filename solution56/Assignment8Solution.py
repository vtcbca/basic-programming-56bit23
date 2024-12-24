# Method 1: Using a Simple For Loop with String Formatting
def print_pattern(n):
    for i in range(1, n+1):
        # Print leading spaces
        print(' ' * (n - i), end='')
        
        # Print increasing characters
        for j in range(1, i+1):
            print(chr(64 + j), end=' ')
        
        # Print decreasing characters
        for j in range(i-1, 0, -1):
            print(chr(64 + j), end=' ')
        
        print()  # Move to the next line

input_lines = int(input("Enter the number of lines: "))  # Input number of rows
print_pattern(input_lines)
