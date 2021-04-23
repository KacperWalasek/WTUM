def find_max_position(histogram):
    histogram = list(histogram)

    return histogram.index(max(histogram)), max(histogram)
