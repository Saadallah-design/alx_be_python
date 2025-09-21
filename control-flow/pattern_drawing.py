rows = int(input("Enter the size of the pattern: "))
row = 0

while row < rows:
  col = 0
  while col < rows:
    print("*", end="")
    col += 1
  print()
  row += 1