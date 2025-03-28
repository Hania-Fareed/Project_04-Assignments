import random

num_side = 6

def roll_dice():
    dice1 : int = random.randint(1, num_side)
    dice2 : int = random.randint(1, num_side)
    total : int = dice1 + dice2
    print ("Total of two dice: " , total)

def main():
    roll_dice()
    roll_dice()
    roll_dice()

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()