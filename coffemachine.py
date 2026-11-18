class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550
        self.state = 'action'

    def process_input(self, user_input: str) -> bool:
        if self.state == 'action':
            if user_input == 'buy':
                self.state = 'buy'
                print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            elif user_input == 'fill':
                self.fill_machine()
            elif user_input == 'take':
                self.take_money()
            elif user_input == 'remaining':
                self.print_state()
            elif user_input == 'exit':
                return False

        elif self.state == 'buy':
            if user_input != 'back':
                self.buy_coffee(user_input)
            self.state = 'action'

        return True

    def print_state(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def buy_coffee(self, choice: str):
        recipes = {
            '1': (250, 0, 16, 4),
            '2': (350, 75, 20, 7),
            '3': (200, 100, 12, 6)
        }

        if choice not in recipes:
            return

        req_water, req_milk, req_beans, cost = recipes[choice]

        if self.water < req_water:
            print("Sorry, not enough water!")
        elif self.milk < req_milk:
            print("Sorry, not enough milk!")
        elif self.coffee_beans < req_beans:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= req_water
            self.milk -= req_milk
            self.coffee_beans -= req_beans
            self.cups -= 1
            self.money += cost

    def fill_machine(self):
        print()
        add_water = int(input("Write how many ml of water do you want to add:\n> "))
        add_milk = int(input("Write how many ml of milk do you want to add:\n> "))
        add_beans = int(input("Write how many grams of coffee beans do you want to add:\n> "))
        add_cups = int(input("Write how many disposable cups of coffee do you want to add:\n> "))

        self.water += add_water
        self.milk += add_milk
        self.coffee_beans += add_beans
        self.cups += add_cups

    def take_money(self):
        print(f"\nI gave you {self.money}")
        self.money = 0


def main():
    machine = CoffeeMachine()
    running = True

    while running:
        if machine.state == 'action':
            print("\nWrite action (buy, fill, take, remaining, exit):")
            user_input = input("> ").strip()
            running = machine.process_input(user_input)
        elif machine.state == 'buy':
            user_input = input("> ").strip()
            running = machine.process_input(user_input)


if __name__ == "__main__":
    main()