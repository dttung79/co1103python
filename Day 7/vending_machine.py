def print_menu():
    print("1. Water ($0.5)")
    print("2. Soda ($1.0)")
    print("3. Coffee ($1.5)")

def choose_drink():
    choice = int(input("Enter the option: "))
    price = 0.5 if choice == 1 else 1.0 if choice == 2 else 1.5 if choice == 3 else 0
    
    if price == 0:
        print("Invalid option")
    else:
        print("Price: $", price)
    
    return price

def pay(price):
    paying = True
    while paying:
        money = float(input("Enter money: "))
        change = money - price
        if change < 0:
            print("Not enough money")
            price = price - money
        else:
            print("Change: $", change)
            paying = False

### Main program starts here
while True:
    print_menu()
    price = choose_drink()
    if price > 0:
        pay(price)