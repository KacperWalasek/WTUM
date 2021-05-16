def sort_entries(entries):
    length = len(entries)
    sorted_entries = []
    for i in range(0, 10):
        empty_tab = []
        sorted_entries.append(empty_tab)
    for i in range(0, length):
        sorted_entries[int(entries[i].label)].append(entries[i])
    return sorted_entries
