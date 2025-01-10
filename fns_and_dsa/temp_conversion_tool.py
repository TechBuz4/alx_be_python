#Illustrate the concept of variable scope by creating a script that converts temperatures
# between Celsius and Fahrenheit, using global variables to store conversion factors.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =  9/5

def convert_to_celsius(fahrenheit):
""" Convert to celsius"""
    return (FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32))
def convert_to_fahrenheit(celsius):
""" covert to fahrenheit"""
    return ((CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32)

print("Temperature Calculator")
temp = int(input("Enter your temperature"))
choice = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
if choice.lower() == 'c':
    result = convert_to_celsius(temp)
    print(f"The temperature is {result} in Celsius.")
elif choice.lower() == 'f':
    result = convert_to_fahrenheit(temp)
    print(f"The tempearture is {result} in Fahrenheit")
else: 
    print("The temperature is unknown")

     
