# Method 1: Using a Simple For Loop
def print_pattern(n):
    for i in range(1, n+1):
        print('* ' * i)

input_lines = int(input("Enter number of lines: "))  # Input number of lines
print_pattern(input_lines)
