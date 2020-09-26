#This Tool Is Made By NandyDark And Its Job Is To Take Screenshot..It Works On Windows OS and MacOS
from PIL import Image, ImageGrab # pip install pillow
import time

def nandytakeScreenshot():
    image = ImageGrab.grab()
    image.show()
    
if _name_=="_main_":
    time.sleep(3)
    nandytakeScreenshot()
