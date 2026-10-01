# Binary Search - Time O(log N), Auxiliary Space O(1)
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

if __name__ == "__main__":
    data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print("Index of 23:", binary_search(data, 23))
    print("Index of 7:", binary_search(data, 7))