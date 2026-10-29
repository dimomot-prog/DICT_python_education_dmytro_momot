import random

num_friends = int(input("Enter the number of friends joining (including you): "))

if num_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(num_friends):
        name = input(">")
        friends[name] = 0

    total_amount = float(input("Enter the total amount: "))
    lucky_option = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')

    lucky_one = None
    if lucky_option.strip().lower() == "yes":
        lucky_one = random.choice(list(friends.keys()))
        print("{lucky_one} is the lucky one!")
    else:
        print("No one is going to be lucky")

    if lucky_one:
        split_amount = round(total_amount / num_friends - 1), 2
        for friend in friends:
            if friend == lucky_one:
                friends[friend] = 0
            else:
                friends[friend] = split_amount
    else:
        split_amount = round(total_amount / num_friends), 2
        for friend in friends:
            friends[friend] = split_amount
    print()
    print(friends)



