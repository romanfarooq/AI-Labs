# (a) Initialize a list of 100 values from 0 to 99.

arr = [i for i in range(100)]

# or

# arr = list(range(100))

# (b) Print the values from index 40 till end

print("Values from index 40 till end:\n", arr[40:], end="\n\n")

# (c) Print all even index values

print("All even index values:\n", arr[::2], end="\n\n")

# (d) Print the 5th last element

print("5th last element:\n", arr[-5:], end="\n\n")

# (e) Print the values from 36th last index to 5th last index

print("Values from 36th last index to 5th last index:\n", arr[-36:-5], end="\n\n")