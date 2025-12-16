class InsertionSort:
    def insertion_sort(self, arr):
        n = len(arr)

        for i in range(1, n):
            key = arr[i]
            j = i - 1

            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key


if __name__ == "__main__":
    arr = [9, 5, 1, 4, 3]

    sorter = InsertionSort()
    sorter.insertion_sort(arr)

    print("Sorted array:", arr)
