# This script will ask the user about the current weather conditions 
# and provide clothing recommendations based on the input

# asking for user inputs
user_input = input("What's the weather like today? (sunny/rainy/cold):").lower()

# statements to respond based on user inputs
if user_input == "sunny":
  print("Wear a t-shirt and sunglasses.")
elif user_input == "rainy":
  print("Don't forget your umbrella and a raincoat.")
elif user_input == "cold":
  print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
