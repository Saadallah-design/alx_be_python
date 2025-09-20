# This script will ask the user to enter a number, then use a for loop to print the multiplication table for that number from 1 to 10.
number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    product = number * i
    print(f"{number} x {i} = {product}")# This script will generate and display the multiplication table for a number provided by the user.
# It demonstrates the use of a for loop to iterate through a range of numbers and perform multiplication.