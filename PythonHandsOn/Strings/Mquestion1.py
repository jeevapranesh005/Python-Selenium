tuple1 = ('Manjeet', 'Nikhil', 'Akshat')
tuple2 = (' Singh', ' Meherwal', ' Garg')

result = tuple(a + b for a, b in zip(tuple1, tuple2))

print("The concatenated tuple:", result)