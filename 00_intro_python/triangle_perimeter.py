def main():
    side1 : float = float(input("What is the length of side 1? "))
    side2 : float = float(input("What is the length of side 2? "))
    side3 : float = float(input("What is the length of side 3? "))
    total : float = side1 + side2 + side3
    print (f"the perimeter of the triangle is {total}")

if __name__ == '__main__':
    main()    