import math

def main():
    side1 : float = float(input("Enter the base: "))
    side2 : float = float(input("Enter the perpendicular: "))
    side3 : float = math.sqrt(side1 ** 2 + side2 ** 2)

    print(f"The length of hypotenuse is: {side3}")

if __name__ == '__main__':
    main()    