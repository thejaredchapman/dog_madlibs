import requests
import urllib.request
from PIL import Image



#DATA FROM API
website = "https://api.thedogapi.com/v1/images/search"
r = requests.get(website)
data = r.json()
url = data[0]['url']

urllib.request.urlretrieve(url, "dog_image.jpg")


