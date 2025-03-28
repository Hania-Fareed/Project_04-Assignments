import random

dice_num : int = 6
def roll_dice():
    dice1 : int = random.randint(1, dice_num)
    dice2 : int = random.randint(1, dice_num)

    total : int = dice1 + dice2

    print (f"First dice: {dice1}")
    print (f"Second dice: {dice2}")
    print (f"Total of two dice {total}")

if __name__ == '__main__':
    roll_dice()

