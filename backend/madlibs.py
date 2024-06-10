from datetime import datetime
import json


cur_time = str(datetime.now())
firstName = input("Enter a name: ")
age = input(f"How old is {firstName}: ")
location = input("Enter a location: ")
activity1 = input("Enter an activity: ")
activity2 = input("Enter another activity: ")
activity3 = input("Again, enter another activity: ")
adjective = input("Enter an adjective: ")
number = input("Please input a number: ")
number1 = input("Please input another number: ")
tvShow = input("Please input a TV Show: ")
aspectTvShow = input(f"What's a particular aspect of {tvShow}: ")
favoriteSnack = input(f"What's {firstName}'s favorite snack: ")
religion = input(f"What's {firstName}'s religion *Any religion or agnostic is fine*: ")
favoriteDrink = input(f"What's {firstName}'s favorite drink: ")
favoriteStatement = input(f"What's {firstName}'s favorite way to start a conversation: ")


madlib = f"This is {firstName}.{firstName} is {age} and from {location}. On a regular day you can find {activity1}. But also {firstName} likes to {activity2}. One word to describe {firstName}’s personality would be {adjective}. {firstName} has {number} companions with {number1} children. {tvShow} is {firstName}’s favorite show and likes it because of {aspectTvShow}. {favoriteSnack} is {firstName}’s favorite snack. {firstName} is a practicing {religion} but loves to {activity3}. If you’re interest in a chat, please contact {firstName} to have a WOOF/MEOW and a {favoriteDrink}. If you want to start a conversation, {firstName} will respond by saying, {favoriteStatement}" 
with open(f"{firstName}"+cur_time.txt, "w") as file:
    file.write(madlib)

# need to append item to madlib