def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    midpoint = len(unsorted_list) / 2
    list1 = unsorted_list[:midpoint]
    list2 = unsorted_list[midpoint:]
    list1 = merge_sort(list1)
    list2 = merge_sort(list2)
    return merge(list1, list2)

def merge(list1, list2):
    list1_index = 0
    list2_index = 0
    merged_list = []
    while list1_index < len(list1) and list2_index < len(list2):
        if list1[list1_index] < list2[list2_index]:
            merged_list.append(list1[list1_index])
            list1_index += 1
        else:
            merged_list.append(list2[list2_index])
            list2_index += 1
    merged_list += list1[list1_index:]
    merged_list += list2[list2_index:]
    return merged_list

if __name__ == "__main__":
    arr = [2, 7, 1, 3, 0, 8, 21, 7]
    sorted = merge_sort(arr)
    print(sorted)