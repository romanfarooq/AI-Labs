# print("Hello, world!")

# def my_function():
#     print("Hello, world!")

# my_function()

# def add_numbers(a, b):
#     c = a + b
#     return c

# print(add_numbers(3, 2))

# a = 2

# b = [1, 2, 3,
#      4, 5, 6]

# # this is legal, but we shouldn't do
# c = 1; d = 5

# print(a, b, c, d)

# print(type(7))

# temp = 17 / 3

# temp = 17 // 3

# temp = 17 % 3

# temp = 5 * 3 + 2

# print(temp)

# tax = 12.5 / 100
# price = 100.50
# res = price * tax

# print(res)

# newPrice = price + res

# print(newPrice)

# print(round(newPrice, 2))

# word = 3 * 'un' + 'iun'

# print(word)

# print(word[0:2])

# print(word[2:5])

# with open('myfile.txt', 'w') as myfile:
#     print("Hello!", file=myfile)

# with open('myfile.txt', 'w') as myfile:
#     myfile.write("Hello!")

# with open('myfile.txt', 'r') as myfile:
#     data = myfile.read()
#     print(data)

# # This is a global variable
# a = 0

# if a == 0:
#     # This is still a global variable
#     b = 1

# def my_function(c):
#     # This is a local variable
#     d = 3
#     print(c)
#     print(d)

# my_function(7)

# print(a)
# print(b)

# # c and d doesn't exit anymore -- these statments will give us error
# print(c)
# print(d)

# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print("Negative change to zero")
# elif x == 0:
#     print("Zero")
# elif x == 1:
#     print("single")
# else:
#     print("More")

# for i in range(1, 9):
#     print(i)

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))

# for i in range(5, 10):
#     print(i)

# for i in range(0, 10, 3):
#     print(i)
    
# for i in range(-10, -100, -30):
#     print(i)
    
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#     print()

# fib(2000)

# fib(100)


# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)

# ask_ok('Do you really want to quit?')

# ask_ok('OK to overwrite the file?', 2)

# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# def make_greeting(title, name, surname, formal=True):
#     if formal:
#         return "Hello, %s %s!" % (title, surname)
#     return "Hello, %s!" % name

# print(make_greeting("Mr", "John", "Smith"))
# print(make_greeting("Mr", "John", "Smith", False))

# a = lambda: 3

# # is same as

# def a():
#     return 3

# b = lambda x, y: x + y

# # is same as

# def b(x, y):
#     return x + y
