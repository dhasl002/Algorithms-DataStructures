import random
def quick_sort(arr, left, right):
    if left >= right:
        return arr
    pivot = arr[random.randint(left, right)]
    index = partition(arr, left, right, pivot)
    quick_sort(arr, left, index - 1)
    quick_sort(arr, index, right)
    return arr

def partition(arr, left, right, pivot):
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            tmp = arr[left]
            arr[left] = arr[right]
            arr[right] = tmp
            left += 1
            right -= 1
    return left


if __name__ == "__main__":
    arr = [2, 7, 1, 3, 0, 8, 21, 7]
    sorted = quick_sort(arr, 0, len(arr) - 1)
    print(sorted)