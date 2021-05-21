from data_classes import Entity


def transition_horizontal(entity):
    tr_horizontal = []
    for row in entity.pixels:
        ctr = 0
        color = 0
        for col in row:
            if col != color:
                color = col
                ctr += 1
        tr_horizontal.append(ctr)

    return tr_horizontal
