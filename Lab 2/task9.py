import time

big_list = list(range(100000, 300001))

def search(integer_list, key):
    for i in range(0, len(integer_list)):
        if integer_list[i] == key:
            return i
    return None

def timer(num):
    start = time.time()
    search(big_list, num)
    end = time.time()
    return end - start

print("Time taken to find element at front:", timer(100000))
print("Time taken to find element in middle:", timer(200000))
print("Time taken to find element at back:", timer(300000))
print("Time taken to find element not in list:", timer(3))