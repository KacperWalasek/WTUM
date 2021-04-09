from read_data import read_data
from show_picture import show_picture

if __name__ == '__main__':
    entries = read_data('train.csv')
    for ent in entries:
        print(ent.label)
    print(entries[50].pixels)
    show_picture(entries[80], 'picture')
