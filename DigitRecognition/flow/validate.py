from Utils.compare import compare
from data_preparation.data_extraction import extract_data


def show_result_info(validation_set, result):
    print()
    print('Analiza rezultatu:')
    label_pairs = list(zip(result, list(map(lambda ent: ent.label, validation_set))))
    correct = [None]*10
    for i in range(10):
        correct[i] = [0, 0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(len(label_pairs)):
        ent = label_pairs[i]
        if ent[0] == ent[1]:
            correct[int(ent[0])][0] += 1
        else:
            correct[int(ent[0])][1] += 1
            correct[int(ent[0])][2][int(ent[1])] += 1
    for i in range(len(correct)):
        c = correct[i]
        print('Liczba', i)
        print('Skuteczność:', "{}%".format(int(c[0]/(c[0]+c[1])*100)))
        print('Liczba pomyłek z daną liczbą:')
        for t in enumerate(c[2]):
            print("{0}: {1}".format(t[0], t[1]))
        print()
        

def validate(algorithm, validation_set):
    result = algorithm.predict(list(map(lambda ent: extract_data(ent), validation_set)))
    show_result_info(validation_set, result)
    return compare(validation_set, result)
