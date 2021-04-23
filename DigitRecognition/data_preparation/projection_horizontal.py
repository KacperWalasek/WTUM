from data_classes import Entity


def projection_horizontal(entity):
    horizontal = []
    for row in entity.pixels:
        ctr = 0
        for col in row:
            if col == 0:
                ctr += 1
        horizontal.append(ctr)

    return horizontal
