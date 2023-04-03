def calculator(num1, num2, operation='addition', output_format='floating point'):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError('Invalid input: numbers must be integers or floats')
    if operation not in ['addition', 'subtraction', 'multiplication', 'division']:
        raise ValueError('Invalid input: operation must be addition, subtraction, multiplication or division')
    if output_format not in ['integer', 'floating point']:
        raise ValueError('Invalid input: output format must be integer or floating point')
    if operation == 'addition':
        result = num1 + num2
    elif operation == 'subtraction':
        result = num1 - num2
    elif operation == 'multiplication':
        result = num1 * num2
    elif operation == 'division':
        result = num1 / num2
    if output_format == 'integer':
        return round(result)
    else:
        return result
    
res = calculator(13, 34)

print(res)