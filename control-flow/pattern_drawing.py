# The first line of code prompts the user to enter a number
# The input is converted to an integer and stored in the 'rows' variable.
# For example, if the user types '5', the value of 'rows' will be 5.
rows = int(input("Enter the size of the pattern: "))
    
# This is the outer loop.
# The 'range(rows)' function generates a sequence of numbers from 0 up to (but not including) the value of 'rows'.
# This loop controls how many new lines (rows) will be printed.
# If rows = 5, this loop will run 5 times (for i = 0, 1, 2, 3, 4).
for i in range(rows):
    
    # This is the inner loop.
    # It also uses 'range(rows)', so it will run the same number of times as the outer loop.
    # This loop controls how many '#' characters are printed on a single line.
    # For each iteration of the outer loop, this inner loop runs completely from start to finish.
    for j in range(rows):
        
        # This line prints the '#' character.
        # The 'end=""' argument is very important. It tells the 'print' function
        # NOT to add a new line after printing the character.
        # This causes all the '#' characters to be printed on the same line.
        print("#", end="")
        
    # This line is part of the outer loop.
    # It is executed after the inner loop has finished printing all the '#' characters for a single row.
    # The 'print()' function without any arguments simply prints a new line.
    # This moves the cursor down to the next line, so the next row of '#' characters will start on a new line.
    print()