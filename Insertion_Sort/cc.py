def insert(sorted_list, value):
    i = 0
    while i < len(sorted_list) and value > sorted_list[i]:
        i += 1
    sorted_list.insert(i, value)

def insertion_sort(input_list):
    sorted_list = [input_list[0]]  # Initialize the sorted list with the first element
    for i in range(1, len(input_list)):
        insert(sorted_list, input_list[i])
    return sorted_list
