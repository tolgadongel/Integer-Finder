def find_integers():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    d = int(input("Enter the value of d: "))

    result = []

    # Iterate through a range of possible values for n
    for n in range(-1000, 1000):
        # Check if the denominator is zero
        if c * n + d != 0:
            # Check if the expression is an integer
            if (a * n + b) % (c * n + d) == 0:
                result.append(n)

    return result

# Call the function to get the integers
integers = find_integers()

# Print the resulting integers
print(integers)
