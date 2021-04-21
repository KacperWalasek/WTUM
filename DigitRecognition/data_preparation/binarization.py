from data_classes import Entity


def binarize(entity):
    new_pixels = []
    for row in entity.pixels:
        new_row = []
        for pixel in row:
            new_pixel = 255 if int(pixel) > 100 else 0
            new_row.append(new_pixel)
        new_pixels.append(new_row)
    return Entity(entity.label, new_pixels)
