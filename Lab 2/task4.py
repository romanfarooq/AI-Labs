def mean_median_mode(numbers):
    # Calculate the sum of list elements
    total = 0
    for number in numbers:
        total += number

    # Calculate the mean
    mean = total / len(numbers)

    # Calculate the median
    numbers.sort()
    if len(numbers) % 2 == 0:
        median = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
    else:
        median = numbers[len(numbers) // 2]

    # Calculate the mode
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    mode = []
    max_count = 0
    for number, count in counts.items():
        if count > max_count:
            max_count = count
    
    for number, count in counts.items():
        if count == max_count:
            mode.append(number)

    # Display the result
    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)

mean_median_mode([56,13,3,56,100,3,34])