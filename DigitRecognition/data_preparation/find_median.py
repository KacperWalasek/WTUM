def find_median(histogram):
    histogram = list(histogram)
    histogram.sort()
    length = len(histogram)
    if length % 2 == 0:
        median = histogram[length//2 - 1] + histogram[length // 2]
        median /= 2
    else:
        median = histogram[length // 2]

    return median
