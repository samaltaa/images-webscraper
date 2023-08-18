from selenium import webdriver
import requests
import io
from PIL import Image
import time
import os


PATH ='/Users/alexsanchez/Downloads/chromedriver_mac64/chromedriver'

wd = webdriver.Chrome(PATH)

image_url = ''

#functions 
def get_images_from_google(wd, delay, max_images):
    def scroll_down(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    url = 'https://www.google.com/search?sca_esv=558159101&sxsrf=AB5stBhmr7b5nZg8uazF-khD-vZpNJ68RQ:1692379791901&q=portraits+of+asians&tbm=isch&source=lnms&sa=X&sqi=2&ved=2ahUKEwjVwMiC3uaAAxXmD1kFHcm3DVsQ0pQJegQIDRAB&biw=1019&bih=731&dpr=2#imgrc=cSkwL5wkDdHR8M'
    wd.get(url)


def download_image(download_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open(file_path, "wb") as f:
            image.save(f, "JPEG")

        print("Success")
    except Exception as e:
        print('FAILED -', e)

#leave file path parameter empty to store the image locally
#download_image("", image_url, "test.jpg")

get_images_from_google(wd, 2, 10)