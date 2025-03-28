Days_In_Year = 365
Hours_In_Days = 24
Minutes_In_Hour = 60
Seconds_Per_Minute = 60

def main():
    Seconds_In_Year = Days_In_Year * Hours_In_Days * Minutes_In_Hour * Seconds_Per_Minute
    print(f"There are {Seconds_In_Year} seconds in a year!")

if __name__ == '__main__':
    main()
