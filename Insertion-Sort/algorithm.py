def insertionSort(arr, n):
    for i in range(1, n):
        j = i

        while j >= 1 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
        
    
if __name__ == "__main__":
    n = int(input("Enter arr size: "))
    arr = list(map(int, input("Enter arr elements: ").split()))

    insertionSort(arr,n)
    print(arr)
