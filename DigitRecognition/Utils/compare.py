def compare(entities, labels):
    count = 0
    for i in range(len(labels)):
        if entities[i].label != labels[i]:
            count += 1
    return 1 - count/len(entities)
