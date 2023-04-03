# 1. Create a list a which contains the first three odd positive integers and a list b which contains the first three even positive integers.
a = [1, 3, 5]
b = [2, 4, 6]

# 2. Create a new list c which combines the numbers from both lists (order is unimportant).
c = a + b

# 3. Create a new list d which is a sorted copy of c, leaving c unchanged.
d = sorted(c)

# 4. Reverse d in-place.
d.reverse()

# 5. Set the fourth element of c to 42.
c[3] = 42

# 6. Append 10 to the end of d.
d.append(10)

# 7. Append 7, 8 and 9 to the end of c.
c += [7, 8, 9]

# 8. Print the first three elements of c.
print(c[:3])

# 9. Print the last element of d without using its length.
print(d[-1])

# 10. Print the length of d.
print(len(d))