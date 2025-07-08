def find_unique_elements(lst):
    output = []
    for i in lst:
        if i not in output:
            output.append(i)
    return output

print(find_unique_elements([4,6,73]))