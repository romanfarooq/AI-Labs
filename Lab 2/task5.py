def find_duplicates(numbers):
    # Create an empty list to store the duplicates
    duplicates = []

    # Loop through the list of numbers and count the occurrences of each number
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    # Loop through the dictionary of counts and add any numbers with a count greater than 1 to the duplicates list
    for number, count in counts.items():
        if count > 1:
            duplicates.append(number)

    # Return the duplicates list
    return duplicates

res = find_duplicates([56,13,3,56,100,3,34])

print(res)