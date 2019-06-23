import urllib.request
import random


def download_image_url(url):
    name = random.randrange(1, 1000)
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullname)


download_image_url("https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2018/03/italy_and_mediterranean/17402074-1-eng-GB/Italy_and_Mediterranean_node_full_image_2.jpg")
