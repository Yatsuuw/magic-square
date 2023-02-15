def check_square_magic(square):
    # Recover the order of the square
    n = len(square)

    # Calculates the expected sum for each row, column and diagonal of the square
    expected_sum = n * (n**2 + 1) // 2

    # Checks if the sum of each row, column and diagonal is equal to the expected sum
    for i in range(n):
        row_sum = sum(square[i])
        if row_sum != expected_sum:
            print("The line {} does not satisfy the magic square condition.".format(i))
            return False

    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += square[i][j]
        if col_sum != expected_sum:
            print("The {} column does not meet the magic square condition.".format(j))
            return False

    diag_sum1 = 0
    diag_sum2 = 0
    for i in range(n):
        diag_sum1 += square[i][i]
        diag_sum2 += square[i][n-i-1]
    if diag_sum1 != expected_sum or diag_sum2 != expected_sum:
        print("The diagonals do not satisfy the magic square condition.")
        return False

    # If all sums are equal to the expected sum, the square is magic
    return True

# Asks the user to enter the order of the square
n = int(input("Please enter the order of the square: "))

# Initialize a 2D array to store the values of the square
square = []
for i in range(n):
    row = []
    for j in range(n):
        # Asks the user to enter the value of each box
        val = int(input("Please enter the value of the box ({},{}) : ".format(i, j)))
        row.append(val)
    square.append(row)

# Vérifie si le carré est magique
if check_square_magic(square):
    print("Congratulations! Your square is magic.")
else:
    print("Sorry, your square does not meet the magic square condition.")
