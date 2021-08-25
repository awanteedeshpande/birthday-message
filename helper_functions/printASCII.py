import helpers as hp
from PIL import Image
import time
import math
import os


def convert_to_ascii():
    imgFile = "./helper_functions/image.jpg" #replace by your own custom image
    img = Image.open(imgFile)

    # resize the image
    width, height = img.size
    aspect_ratio = height / width
    new_width = math.ceil(hp.terminal_size()/2.4)
    new_height = aspect_ratio * new_width * 0.45
    img = img.resize((new_width, int(new_height)))

    # new size of image
    # print(img.size)

    # convert image to greyscale format
    # https://stackoverflow.com/questions/52307290/what-is-the-difference-between-images-in-p-and-l-mode-in-pil
    img = img.convert('L')
    pixels = img.getdata()

    # replace each pixel with a character from array
    #chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", ".", ")", "(", "^"]
    chars = ["@", "@", "G", ")", "k", "B", "(", ".", "!", ":", ".", ":", ".", ")"]
    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    # split string of chars into multiple strings of length equal to new width and create a list
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)

    for row in ascii_image.split("\n"):
        print(row.center(hp.terminal_size()))
        time.sleep(0.002)