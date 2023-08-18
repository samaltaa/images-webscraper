from selenium import webdriver
import requests
import io
from PIL import Image

PATH = '/Users/alexsanchez/Downloads/chromedriver_mac64/chromedriver'

wd = webdriver.Chrome(PATH)

image_url = 'https://media.istockphoto.com/id/1288538088/photo/portrait-young-confident-smart-asian-businessman-look-at-camera-and-smile.webp?b=1&s=170667a&w=0&k=20&c=EcjlfC0hE33usx5Ys_ftE1iC0TlgKG1pSqclpOULGLk='

#functions 
def download_image(download_path, url, file_name):
    image_content = requests.get(url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file)
    file_path = download_path + file_name

    with open(file_path, "wb") as f:
        image.save(f, "JPEG")

    print("Success")

#leave file path parameter empty to store the image locally
download_image("", image_url, "test.jpg")