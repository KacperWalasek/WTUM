def find_min_position(histogram):  # finds minimum NON ZERO value and it's position
    position = 0
    value = len(histogram)
    ctr = 0

    for n in histogram:
        if value > n > 0:
            position = ctr
            value = n
        ctr += 1

    return position, value
