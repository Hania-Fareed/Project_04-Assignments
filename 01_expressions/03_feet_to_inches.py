Inches_per_foot : int = 12

def main():
    feet : float = float(input("Enter number in feet: "))
    inches : float = feet * Inches_per_foot
    print(f"That is {inches} inches!")

if __name__ == '__main__':
    main()    