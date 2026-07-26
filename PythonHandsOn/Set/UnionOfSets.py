def union_sets(set1, set2):
    return set1.union(set2)


set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(union_sets(set1, set2))

set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
print(union_sets(set1, set2))
