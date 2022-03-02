
def binary_search(input_array, value):
    if len(input_array) > 1:
        median = input_array[len(input_array)//2]
    else:
        median = input_array[0]
    if value < median:
        new_arr = input_array[:median]
        binary_search(new_arr, value)

    elif value > median:
        new_arr = input_array[median:]
        binary_search(new_arr, value)

    elif value == median:
        return 'value in array'
    else:
        return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
