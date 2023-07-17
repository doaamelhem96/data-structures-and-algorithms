def compare_numbers(a, b):
    if a == b:
        return 0
    if a < b:
        return -1
    if a > b:
        return 1

def compare_strings(a, b):
    a_lower = a.lower()
    b_lower = b.lower()
    if a_lower < b_lower:
        return -1
    elif a_lower > b_lower:
        return 1
    return 0

