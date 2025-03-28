def main():
    num1 : int = int(input("Please enter an integer to be divided: "))
    num2 : int = int(input("Please enter an integer to divide by: "))
    
    sum : int = num1 // num2
    remainder : int = num1 % num2

    print(f"The result of this division is {sum} with a remainder of {remainder}.")

if __name__ == '__main__':
    main()
