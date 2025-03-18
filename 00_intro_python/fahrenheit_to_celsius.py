def main():
    temperature: float = float(input("Enter temperature in Fahrenheit: "))  # Convert input to float
    degrees_celsius = (temperature - 32) * 5.0 / 9.0  # Formula for converting degrees
    print(f"Temperature: {temperature}F = {degrees_celsius:.2f}C")  #  Output to 2 decimal places

if __name__ == '__main__':
    main()