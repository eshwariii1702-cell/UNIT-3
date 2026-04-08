import celsius_to_fahrenheit as cf
import fahrenheit_to_celsius as fc

choice = input("Convert (C/F): ")

if choice == "C":
    c = float(input("Enter Celsius: "))
    print("Fahrenheit:", cf.convert(c))

elif choice == "F":
    f = float(input("Enter Fahrenheit: "))
    print("Celsius:", fc.convert(f))
