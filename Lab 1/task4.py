def cube(n):
    return n ** 3

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def count_pattern(pattern, lst):
    count = 0
    for i in range(len(lst) - len(pattern) + 1):
        if lst[i:i+len(pattern)] == pattern:
            count += 1
    return count

def multiplication_table(n):
    for i in range(1, 11):
        print(n, 'x', i, '=', n*i)

def simple_calculator():
    operation = input('Enter an operation (+, -, /, *): ')
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '/':
        print(num1 / num2)
    elif operation == '*':
        print(num1 * num2)
    else:
        print('Invalid operation')

def sort_sentence(sentence):
    words = sentence.split()
    words.sort()
    return ' '.join(words)

class RomanNumeralConverter:
    def __init__(self):
        self.roman_numerals = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def convert(self, number):
        roman_numeral = ''
        for value, numeral in self.roman_numerals.items():
            while number >= value:
                roman_numeral += numeral
                number -= value
        return roman_numeral

def find_pair(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return i, j