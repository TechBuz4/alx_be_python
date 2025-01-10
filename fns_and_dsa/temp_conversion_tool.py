#Illustrate the concept of variable scope by creating a script that converts temperatures
# between Celsius and Fahrenheit, using global variables to store conversion factors.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR =  9/5

def convert_to_celsius(fahrenheit):
""" Convert to celsius"""
    return ((fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR)
def convert_to_fahrenheit(celsius):
""" covert to fahrenheit"""
    return ((celsius * CELSIUS_TO_FAHRENHEIT_FACTOR ) + 32)

print("Temperature Calculator")
temp = int(input("Enter the temperature to convert:"))
choice = input("Is this temperature in Celsius or Fahrenheit? (C/F):")
if choice.lower() == 'c':
    result = convert_to_celsius(temp)
    print(f"The temperature is {result} in Celsius.")
elif choice.lower() == 'f':
    result = convert_to_fahrenheit(temp)
    print(f"The tempearture is {result} in Fahrenheit")
else: 
    print("The temperature is unknown")

     
