def set_intersection_count(sets):
    common = set.intersection(*sets)
    return len(common)

sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
print(set_intersection_count(sets))

sets = [{'a', 'b'}, {'b', 'c'}, {'c', 'd'}]
print(set_intersection_count(sets))