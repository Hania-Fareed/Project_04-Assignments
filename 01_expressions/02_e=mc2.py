
C =  299792458

def main():
    user_input : float = float(input("Enter kilos of mass: "))
    e : float = user_input * C**2

    print ("e = m * C**2")
    print(f"m = {user_input:.2f} kg" )
    print (f"C = {C} m/s")
    print(f"{e:.4e} joules of energy!")

if __name__ == '__main__':
    main()