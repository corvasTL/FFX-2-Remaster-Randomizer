from PIL import Image,ImageEnhance, ImagePalette, ImageOps, ImageChops
from PIL import ImageFont
from PIL import ImageDraw
import random
import numpy
import os


def transform_rgba_channels(image, red_factor=1, green_factor=1, blue_factor=1, alpha_factor=1):
    """
    Transforms the RGBA channels of an image.

    Args:
        image (PIL.Image.Image): The image to transform.
        red_factor (float): Factor to multiply the red channel by.
        green_factor (float): Factor to multiply the green channel by.
        blue_factor (float): Factor to multiply the blue channel by.
        alpha_factor (float): Factor to multiply the alpha channel by.

    Returns:
        PIL.Image.Image: The transformed image.
    """

    # Convert image to RGBA if it isn't already
    #image = image.convert("RGBA")

    # Get pixel data as a numpy array
    pixels = image.load()
    width, height = image.size

    # Apply transformations to each pixel
    for x in range(width):
        for y in range(height):
            r, g, b, a = pixels[x, y]
            pixels[x, y] = (
                int(r * red_factor),
                int(g * green_factor),
                int(b * blue_factor),
                int(a * alpha_factor),
            )

    return image

negative = Image.open("C:\\Git\\c001_negative.dds")
img = Image.open("C:\\Git\\c001.dds").convert("RGBA")
img2 = Image.open("C:\\Git\\c001_subtract3.dds").convert("L")

# Define colors for mapping
black_rand = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
white_rand = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
mid_rand = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Define mapping positions
blackpoint = 75
whitepoint = 230
midpoint = 127

colorized = ImageOps.colorize(img2, black_rand, white_rand, mid_rand, blackpoint, whitepoint, midpoint)
colorized_conv = colorized.convert("RGBA")
edited = ImageChops.subtract_modulo(colorized_conv, negative)
edited.show()
r = random.uniform(0, 1)
g = random.uniform(0, 1)
b = random.uniform(0, 1)
a = 1 #random.uniform(0, 2)
transformed_image = transform_rgba_channels(edited, r, g, b, 1)
transformed_image.show()

img.paste(transformed_image, (0, 0), transformed_image)
img.show()
img.save("C:\Git\c001_color.dds")
