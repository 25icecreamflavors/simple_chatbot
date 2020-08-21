import random

import numpy as np
from PIL import Image, ImageDraw


def generate_matrix():
    """ Function that generates 7x7 matrix symmetric 
    with respect to the middle column.
    Returns 2d numpy array with integers and number of colours.
    """
    i = np.random.randint(2, 4)
    matrix = np.zeros((7, 7))
    matrix[1:-1, 1] = matrix[1:-1, 5] = np.random.randint(0, i, (1, 5))
    matrix[1:-1, 2] = matrix[1:-1, 4] = np.random.randint(0, i, (1, 5))
    matrix[1:-1, 3] = np.random.randint(0, i, (1, 5))
    return matrix, i


def fill_colour(image, matrix, colours):
    """ Function that takes image (ImageDraw object), 2d array of integers
    that mean colour number, list of colours. Then it draws squares on the
    image with given colours.
    """
    if image is not None and matrix is not None and colours is not None:
        for i in range(1, len(matrix) - 1):
            for j in range(1, len(matrix[i]) - 1):
                image.rectangle(
                    (j * 74, i * 74, (j + 1) * 74, (i + 1) * 74),
                    fill=colours[int(matrix[i, j]) - 1],
                )


def main():
    colours_palette = [
        ["#f6f4e6", "#fddb3a", "#52575d", "#41444b"],
        ["#557571", "#d49a89", "#f7d1ba", "#f4f4f4"],
        ["#776d8a", "#f3e6e3", "#dbe3e5", "#d3c09a"],
        ["#4b5d67", "#322f3d", "#59405c", "#87556f"],
        ["#ebecf1", "#206a5d", "#1f4068", "#1b1c25"],
    ]
    avatar = Image.new("RGB", (518, 518), "#d8d3cd")
    canvas = ImageDraw.Draw(avatar)
    matrix, number_of_colours = generate_matrix()
    colours = np.random.choice(
        colours_palette[random.randint(0, len(colours_palette) - 1)],
        number_of_colours,
        replace=False,
    )
    fill_colour(canvas, matrix, colours)
    avatar.save("avatar.png")


if __name__ == "__main__":
    main()
