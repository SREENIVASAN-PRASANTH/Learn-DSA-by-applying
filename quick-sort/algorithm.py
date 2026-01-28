def partition(arr, low, high):
    i = low
    j = high

    while i < j:
        while arr[i] <= arr[low] and i <= high -1:
            i += 1
        
        while arr[j] > arr[low] and j >= 1:
            j = j - 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low],arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr, low, high):
    if low < high:
        j = partition(arr, low, high)
        quick_sort(arr, low, j-1)
        quick_sort(arr, j+1, high)


if __name__ == "__main__":
    arr = list(map(int, input("Enter arr (eg. 1 5 3 12 1):").split()))
    print("Before sorting:", arr)
    quick_sort(arr, 0, len(arr)-1)
    print("After sorting:", arr)

