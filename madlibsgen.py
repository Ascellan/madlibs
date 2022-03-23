print(" ")
print(" ")
#Title of the game
game = "Lost in the Apocalypse"

#Printing title and introduction
print(game)
print(" ")
print("Welcome my friend!")
print(" ")

#Taking an input from player, yes/no
question1 = input("It seems like you're feeling adventurous today, am I right?: ")
print(" ")
if question1 == "yes" or question1 == "Yes":
    print("I knew it!")
    print("Try to keep your pants on, pal. \nYou're about to enter the exciting world of Apocalyptic Madness!")
    print("This is where everything is upside down \nand laughter is guaranteed.")
    print(" ")
    print("Now let's throw in some words.")
elif question1 == "no" or question1 == "No":
    print("Too bad! You can always come back later. \nHave a nice day!")
    exit()

#If player answers something else, this is what the program prints.
else:
    print("You are adorable. There's nothing to be afraid of!")
    print(" ")
    print("Now let's throw in some words!")

#Asking for an input from user
print(" ")
input1 = input("Give me a noun in the plural: ")
input2 = input("A noun, please: ")
input3 = input("A noun, please: ")
input4 = input("A noun in the plural: ")
input5 = input("Again, a noun in the plural: ")
input6 = input("A noun in the plural: ")
input7 = input("A noun in the plural: ")
input8 = input("Aaannd the last one, \nbe a doll and give me an adjective!: ")

print(" ")
print("Thank you! Good job!")
print("You've got quite an imagination. \nI'm excited to see what kind of world you've created!")

print(" ")
question3 = input("Are you ready to see what it's like?: ")
if question3 == "yes" or question3 == "Yes":
    print(" ")
    print("Alright, here comes the Madness!")

else:
    print("Now come on, I know you want to!")
    print(" ")
    print("Here comes the Madness, ready or not!")

#placing the values of player's inputs to sentences
sentence1 = f"As I walked along the {input1} \nI realized I was the last of my kind."
sentence2 = f"I was in a {input2} in the middle of the night"
sentence3 = f"Swirls of dust escaped the gravity when the {input3} haunted me \nwith the most tormenting voice."
sentence4 = f"I was a giant amongst the {input4}, \nconsuming their essence to the bone."
sentence5 = f"Hill after hill, mountain after another those fallen {input5} soared the skies \nand painted the space with their gruesome figure."
sentence6 = f"Piece by piece the ingenious strategy of the {input6} revealed itself for me."
sentence7 = f"I was stunned by the presence of {input7}. \nThey looked too {input8}."

#printing the story
print(sentence1 + " ")
print(sentence2 + " ")
print(sentence3 + " ")
print(sentence4 + " ")
print(sentence5 + " ")
print(sentence6 + " ")
print(sentence7)

print(" ")
print("So did you like the story? If you did, (or even better, didn't) just try again any time you like! Bye!")
