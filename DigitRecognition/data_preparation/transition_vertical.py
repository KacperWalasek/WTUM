from data_classes import Entity


def transition_vertical(entity):
    tr_vertical = []
    for col in entity.pixels:
        ctr = 0
        color = 255
        for row in col:
            if row != color:
                color = row
                ctr += 1
        tr_vertical.append(ctr)

    return tr_vertical
