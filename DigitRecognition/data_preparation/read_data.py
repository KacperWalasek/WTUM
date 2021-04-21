import csv
from data_classes import Entity


def read_data(src):
    with open(src, newline='') as file:
        reader = csv.reader(file, delimiter=',')
        entities = []

        for row in reader:
            if row[0] == 'label':
                continue
            pixels = []
            i = 0
            for i in range(0, 28):
                bitmap_row = row[(1+i*28):(1+i*28+28)]
                pixels.append(bitmap_row)
            entities.append(Entity(row[0], pixels))
        return entities
