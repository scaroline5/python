from data import resources, MENU


def print_report():
    """Prints the current status of available Water, Milk, Coffee and Money in the Coffee Machine"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print("\n* * * * Current Status on Resources * * * * ")
    print(f"\nWater: {water}ml"
          f"\nMilk: {milk}ml"
          f"\nCoffee: {coffee}g"
          f"\nMoney: ${money}")
    print("\n* * * * * * End of Report * * * * * * \n")


def check_resources(list_of_ingredients):
    """Receives the list of ingredients to prepare the drink chosen by the customer
    and compare against the available ingredients to identify if it's possible to make the drink """
    for item in list_of_ingredients:
        if resources[item] < list_of_ingredients[item]:
            print(f"Sorry, there isn't enough {item}. Try another drink or come back another time.")
            return False
        else:
            return True


def process_coins(drink_price):
    """Receives the number of coins inserted by the user and calculates to check if it's enough to pay for the drink"""
    print("Please, insert coins.")
    total_coins = int(input("How many quarters? ")) * 0.25
    total_coins += int(input("How many dimes? ")) * 0.10
    total_coins += int(input("How many nickels? ")) * 0.05
    total_coins += int(input("How many pennies? ")) * 0.01
    return total_coins


def is_transaction_successful(received_money, drink_price):
    global money
    if received_money < drink_price:
        print("Sorry, that's not enough money for this drink. Money refunded.")
        return False
    else:
        change = received_money - drink_price
        if change > 0:
            print("Here is ${:0.2f} dollars in change.".format(change))
        money += drink_price
        return True


def make_coffee(drink_name, list_of_ingredients):
    """Prepares and deliver the drink bought by the customer"""
    print("Your drink is being prepared.")
    for item in list_of_ingredients:
        resources[item] = resources[item] - list_of_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


money = 0

# TODO Turn off the Coffee Machine by entering “ off ” to the prompt.
on = True

while on:

    # TODO Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    options = ["1", "2", "3", "off", "report"]
    valid_option = False
    while not valid_option:
        menu_option = input("\nWhat would you like? "
                            "\n1. Espresso ($ 1.50)"
                            "\n2. Latte ($ 2.50)"
                            "\n3. Cappuccino ($ 3.00)\n").lower()
        if menu_option in options:
            valid_option = True
            if menu_option == "off":
                on = False
            elif menu_option == "report":
                # TODO Print report with current ingredient and money status.
                print_report()
            else:
                if menu_option == "1":
                    drink = 'espresso'
                elif menu_option == "2":
                    drink = 'latte'
                else:
                    drink = 'cappuccino'

                # TODO Check if resources are sufficient
                if check_resources(MENU[drink]['ingredients']):
                    # TODO Process coins
                    total_inserted = process_coins(MENU[drink]['cost'])
                    # TODO Check if the transaction was successful
                    if is_transaction_successful(total_inserted, MENU[drink]['cost']):
                        # TODO Make coffee
                        make_coffee(drink, MENU[drink]['ingredients'])
        else:
            print("Invalid option chosen. Try again.")
