# Insertion Sort Part 1 - Time O(N), Auxiliary Space O(1)
def insertionSort1(n, arr):
    v = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > v:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    arr[i + 1] = v
    print(*arr)

if __name__ == "__main__":
    insertionSort1(5, [2, 4, 6, 8, 3])