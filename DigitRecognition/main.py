from read_data import read_data


if __name__ == '__main__':
    entries = read_data('train.csv')
    for ent in entries:
        print(ent.label)
    print(entries[50].pixels)