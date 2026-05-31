def count_unique_elements(input_list):
    return len(set(input_list))

# Test Case 1
input_list = [1, 2, 2, 3, 3, 4]
print(count_unique_elements(input_list))

input_list = ['a', 'b', 'b', 'c']
print(count_unique_elements(input_list))