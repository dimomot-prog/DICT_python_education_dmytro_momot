from math import remainder

bot_name = "Dima"
birth_year = "2026"

print (f"Hello! My name is {bot_name}.")
print(f"Please,remind me your name.")

your_name = input()

print("What a great name you have, {your_name}!")
print("let me guess your age")
print ("Enter remainders of dividing you age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

age = (remainder3 * 70 + remainder5 * 21 +remainder7 * 15) % 105

print("Your age is {age}; that a good time to start programming!")
print("Now i will prove to you that i can count to any number you want .")

count_to = int(input())

for i in range(count_to + 1 ):
    print ("f{i}!")

print("Completed,have a nice day!")

print("Let's test your programming knowledge")
print("Why do we use methods?")
print("1. To repeat a statement multiple subroutines.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of program.")
print("4. To interrupt the execution of program.")

  while True:
      answer =input()
      if answer == "2":
          break
      else:
          print("Please,try again.")

      print("Congratulations,have a nice day!")