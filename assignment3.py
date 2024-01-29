#Write a Python program to store first year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using
#Selection Sort and display top 5 scores

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def scores(arr, n):
    print("\nTop 5 Scores:")
    for i in range(n - 1, n - 6, -1):
        print(f"{n - i}. {arr[i]:.2f}%")

def main():
    num = int(input("Enter the number of students: "))
    percentages = [float(input(f"Enter the percentage of student {i + 1}: ")) for i in range(num)]
    selection_sort(percentages)
    scores(percentages, num)

main()