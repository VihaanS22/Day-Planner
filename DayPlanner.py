import calendar
import time;

import random

print("")
print("The Day Planner")
print("")
print("Hello There. This is Emily, your virtual assistant. Here, in The Day Planner, you can add 12 tasks for 1 hour each that you wish to do in your day. So step up and shine up your world!.")
print("")
guess = input("Before that, would you like to play a fun math-riddle based game before planning your day? Type yes or no :- ")

print("")

if(guess == "yes"):
        
    number = random.randint(1, 9)
    chances = 0

    print(" ")
    print("❓🧠The Number Guesser - a math riddle based game🎲🧮")

    print(" ")
    print("Welcome to The Number Guesser. Here you will be shown a riddle and solving it will give you a numerical answer. Type that in the space given and pass the test. You have 5 chances to guess the correct number. Good Luck!!!")

    print(" ")
    if number == 1:
        print("✖️ ➕What three numbers, none of which is zero, give the same result whether they’re added or multiplied? Type in the least number in them? ➖ ➗")

    if number == 2:
        print("🍎🍎If there are three apples and you take away two, how many apples do you have?🍏🍏")

    if number == 3:
        print("👧🏼👧🏽👩‍🦰A man describes his daughters, saying, “They are all blonde, but two; all brunette but two; and all redheaded but two.” How many daughters does he have?👧🏼👧🏽👩‍🦰")

    if number == 4:
        print("🐢🐠Leon works at the aquarium. When he tries to put each turtle in its own tank, he has one turtle too many. But if he puts two turtles per tank, he has on tank too many. How many turtles and how many tanks does Leon have? Type in the number of turtles he has🐢🐠")

    if number == 5:
        print("👩‍👧‍👧Mary has four daughters, and each of her daughters has a brother. How many children does Mary have?👩‍👧‍👧")

    if number == 6:
        print("🚴‍♂️🦟Two cyclists began a training run, one starting from Moscow and the other starting from Simferopol. When the riders were 180 miles apart, a fly took an interest. Starting on one cyclists shoulder, the fly flew ahead to meet the other cyclist. After reaching him the fly then turned around and yet back. The restless fly continued to shuttleback and fourth until the pair met; then settled on the nose of one rider. The flys speed was 30 mph. Each cyclist speed was 15 mph. How many miles did the fly travel?🚴🏽‍♂️🦟")

    if number == 7:
        print("🧮🔢I am an odd number. Take away a letter and I become even. What number am I?🔢🧮")

    if number == 8:
        print("⚖️🥔How much is this bag of potatoes?' asked the man. '32lb divided by half its own weight,' said the green grocer. How much did the potatoes weigh?🥔⚖️. Hint : Use square roots.")

    if number == 9:
        print("👨‍👧🔞Charlotte is 13 years old. Her father Montague is 40 years old. How many years old was Charlotte when her father was four times as old as Charlotte?🔞👨‍👧")



    while chances<5:
        print(" ")
        guess = int(input("enter a num 🔢:-"))
        print(" ")
        if guess == number:
            print("🏆Congrats you won🏆")
            break
        

        elif guess<number:
            print("⛔guess was too low⛔")
            print(" ")
        else:
            print("⛔guess was too high⛔")
            print(" ")
        chances +=1


    if not chances < 5:
        print(" ")
        print("🙁Aw man. You were so close! The number was : ", number)

    print(" ")
    print("😃Do you want to play again and discover more math riddles. Type '1' to play again.  If you want to exit, type '2' 😃")
    choice = int(input("🤔What do you choose. Yes or No🤔 :"  ))



    if choice <2:
        print(" ")
        print("💐Welcome back. Press the up arrow key and hit enter to join in again.💐")
        print(" ")

    else:
        print(" ")
        print("👋Goodbye. See you later👋")
        print(" ")

        print("The Day Planner")

        

if(guess == "no"):
    print("Ok...Please continue planning your day!")



name = input("Please enter your name:-")
print("")
print("Hi there" + " " + name + "." + " What would you like your plan to be today?")
print("")

first = input("What would you like to do in the first hour:- ")
second = input("What next? :-")
third = input("Time for the third :- ")
fourth = input("Single number four :- ")
fifth = input("High-Five :-")
sixth = input("Number six :-")
seventh = input("Heaven seven :-")
eighth = input("Let's wait for eight? :-")
ninth = input("Cloud Nine :-?")
tenth = input("10th hour :-")
eleventh = input("Close to 12 :-")
twelfth = input("The moment of truth :-")


print("")
print("Planner of" + " " + name + ", is ready for the 12 hours they starts from!!!")
print("")
print("Task 1 :- " + first)
print("Task 2 :- " + second)
print("Task 3 :- " + third)
print("Task 4 :- " + fourth)
print("Task 5 :- " + fifth)
print("Task 6 :- " + sixth)
print("Task 7 :- " + seventh)
print("Task 8 :- " + eighth)
print("Task 9 :- " + ninth)
print("Task 10 :- " + tenth)
print("Task 11 :- " + eleventh)
print("Task 12 :- " + twelfth)
print("")

plan = input("Do you want to plan any important task or check a calendar and the current time? Type Important Tasks or Calendar. If not just hit enter key! ")

if(plan == "Important Tasks"):


    print("")
    imp = print("Enter any five of your important tasks!")

    one = input("First most important:- ")
    two = input("What next? :-")
    three = input("Third importance:- ")
    four = input("Then?:- ")
    five = input("What finally? :-")

    print("")
    print("Important Task Planner of" + " " + name + ", is ready!!!")
    print("")
    print("Task 1 :- " + one)
    print("Task 2 :- " + two)
    print("Task 3 :- " + three)
    print("Task 4 :- " + four)
    print("Task 5 :- " + five)


elif(plan == "Calendar"):
    print("")
    yy = int(input("Enter year: "))  
    print("")
    mm = int(input("Enter month: "))  
    print("")
    print(calendar.month(yy,mm))  

    print ( time.asctime(time.localtime(time.time())) )

    print(" ")

else:
    exit()



