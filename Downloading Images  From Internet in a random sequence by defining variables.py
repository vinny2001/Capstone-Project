# This Revision of the Image Downloader has printed text in the CMD window to display the download progress to the user
import urllib.request
import random
import time
print("""*********************************************************************************************************************
Establishing Internet Connection
""")
time.sleep(2)


def download_image_url(url):
    name = random.randrange(1, 1000)
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullname)


print("""Download has started
""")
time.sleep(2)
download_image_url("https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2018/03/italy_and_mediterranean/17402074-1-eng-GB/Italy_and_Mediterranean_node_full_image_2.jpg")
if download_image_url:
    print("""Done!
    """)
time.sleep(1)
print("""Coded by Vincenzo D'Aria. Enjoy!"
*********************************************************************************************************************
""")
time.sleep(2)
