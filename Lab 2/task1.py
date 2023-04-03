def selection_sort(items):
    for step in range(len(items)):
        location_of_smallest = step
        for location in range(step, len(items)):
            if items[location] < items[location_of_smallest]:
                location_of_smallest = location
        items[step], items[location_of_smallest] = items[location_of_smallest], items[step]
    return items

res = selection_sort([56,13,56,100,3,34])

print(res)