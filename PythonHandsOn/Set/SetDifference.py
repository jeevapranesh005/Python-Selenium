def set_difference(set1, set2):
    return set1.difference(set2)

set1 = {1, 2, 3, 4}
set2 = {2, 3}

result = set_difference(set1, set2)
print(result)

set1 = {'a', 'b', 'c'}
set2 = {'b', 'c', 'd'}

result = set_difference(set1, set2)
print(result)