#함수

def factorial(number):
    count = number - 1
    while count > 1:
        number = number * count
        count = count - 1
    return number

print(factorial(21))
print(factorial(13))
print(factorial(8))
