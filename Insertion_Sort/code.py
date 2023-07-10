def insert(sorted_list, value):
    i = 0
    while value > sorted_list[i]:
        i += 1
    while i < len(sorted_list):
        temp = sorted_list[i]
        sorted_list[i] = value
        value = temp
        i += 1
    sorted_list.append(value)

def insertion_sort(input_list):
    sorted_list = [input_list[0]]
    for i in range(1, len(input_list)):
        insert(sorted_list, input_list[i])
    return sorted_list
