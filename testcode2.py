def add_numbers(a, b):
    return a + b


def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = add_numbers(num1, num2)
    print("The result is:", result)