from data_classes import Entity


def projection_vertical(entity):
    vertical = []
    for col in entity.pixels:
        ctr = 0
        for row in col:
            if row == 0:
                ctr += 1
        vertical.append(ctr)

    return vertical
