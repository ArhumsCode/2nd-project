
from cs50 import get_float

money = get_float("How much money did you pay with? ")

purchase = get_float("What was the cost of the item? ")



while(money < 0 or purchase < 0 or purchase>money):
    print("Sorry couldn't understand! Try again!")
    money = get_float("How much money did you pay with? ")
    purchase = get_float("What was the cost of the item?")

if(money and purchase > 0):
    print(f"Change due: $ {float(money-purchase)} ")


