import requests
import urllib.request
from PIL import Image
from madlibs import firstName

#f(‘This is {name}. {name} is {age} and from {location}. On a regular day you can find {activity1}. But also {name} likes to {activity2}. One word to describe {name}’s personality would be {adjective}. {name} has {number} companions with {number1} children. {tvShow} is {name}’s favorite show and likes it because of {aspectTvShow}. {favoriteSnack} is {name}’s favorite snack. {name} is a practicing {religion} but loves to {activity3}. If you’re interest in a chat, please contact {name} to have a WOOF/MEOW and a {favoriteDrink}. “{favoriteStatement}”.’)
dog_name= "tony"

#DATA FROM API
website = "https://dog.ceo/api/breeds/image/random"

r = requests.get(website)
data = r.json()
photo = data['message']
print(photo)


# TODO: Need to set photo by user's first name then append to json. 

