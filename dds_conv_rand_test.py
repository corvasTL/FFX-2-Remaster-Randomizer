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

img = Image.open("C:\\Git\\c001_top.dds")
img2 = Image.open("C:\\Git\\c001_bottom.dds")
transformed_image = img2
for i in range(10):
    r = random.uniform(0, 3)
    g = random.uniform(0, 3)
    b = random.uniform(0, 3)
    a = 1 #random.uniform(0, 3)
    transformed_image = transform_rgba_channels(transformed_image, r, g, b, 1 )
    transformed_image.show()

img.paste(new, (0, 0), new)
#img.paste(img2, (0, 0), img2) #WORKING LAYERING
#img.show()
#mask = img2.convert("L")
#mask.show()
#mask_edited = ImageOps.colorize(mask, black_rand, white_rand, mid_rand, blackpoint, whitepoint, midpoint)
#mask_edited_conv = mask_edited.convert("RGBA")
#img3 = ImageChops.add(img, mask_edited_conv) #(img, black_rand, white_rand, mid_rand, blackpoint, whitepoint, midpoint)
img.show
img.save("C:\Git\c001_color.dds")
