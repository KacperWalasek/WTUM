def stretch(histogram):
    new_histogram = [0]*28
    beg_offset = 0
    end_offset = 0
    for i in range(len(histogram)):
        if histogram[i] != 28 and histogram[i] != 0:
            beg_offset = i
            break

    for i in range(len(histogram)):
        if histogram[-(i+1)] != 28 and histogram[-(i+1)] != 0:
            end_offset = -i
            break
    hist_len = 28 - beg_offset + end_offset
    for i in range(len(new_histogram)):
        ind = beg_offset + i*hist_len/28
        rest = ind - int(ind)
        snd = 0
        if i != 27:
            snd = rest*histogram[int(ind)+1]
        new_histogram[i] = histogram[int(ind)]*(1-rest) + snd
    # print('a', histogram, new_histogram)
    return new_histogram
