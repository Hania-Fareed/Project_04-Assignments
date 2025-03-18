def main():
    print("This program is about to convert string into number and adding two numbers")
    num1 : str = input("Enter your first number:")
    num1 : int = int(num1)
    num2 : str = input("Enter your second number:")
    num2 : int = int(num2)
    sum = (num1 + num2)
    print(f"Your final answer is {sum}")

if __name__ == '__main__':
    main()    