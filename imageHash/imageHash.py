#!/usr/local/bin/python3.4
from PIL import Image as PILImage
import sys
import os
def dhash(path, hash_size = 16):

    image = PILImage.open(path)
    try:
        image = image.convert('L').resize(
            (hash_size + 1, hash_size),
            PILImage.ANTIALIAS,
        )
    except:
        return False

    difference = []
    for row in range(hash_size):
        for col in range(hash_size):
            pixel_left = image.getpixel((col, row))
            pixel_right = image.getpixel((col + 1, row))
            difference.append(pixel_left > pixel_right)

    decimal_value = 0
    hex_string = []
    for index, value in enumerate(difference):
        if value:
            decimal_value += 2**(index % 8)
        if (index % 8) == 7:
            hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
            decimal_value = 0
    return ''.join(hex_string)

def main():

    if sys.argv.__len__() < 2:
        return
    file_path = sys.argv[1]
    if os.path.exists(file_path) is False :
        return
    if sys.argv.__len__() > 2:
        print(dhash(file_path, int(sys.argv[2])))
    else:
        print(dhash(file_path))
main()