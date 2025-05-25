def binary_serach(arr,num):
    end = len(arr)
    start = 0

    while start < end:
        mid = (start+end)//2

        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            start = mid+1
        else:
            end = mid-1
    return -1

arr = [1,2,3,4,5,3,4,6]
print(binary_serach(arr, 6))