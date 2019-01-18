def is_armstrong(number):
    string = str(number)
    lenth = len(string)
    accumulator = 0

    for num in string:
        accumulator += int(num)**lenth

    return accumulator == number

