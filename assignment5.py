#Write a Python program to store first year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using quick sort and display top five scores.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def scores(arr, n):
    print("\nTop 5 Scores:")
    for i in range(n - 1, n - 6, -1):
        print(f"{n - i}. {arr[i]:.2f}%")

def main():
    num= int(input("Enter the number of students: "))
    percentages = [float(input(f"Enter the percentage of student {i + 1}: ")) for i in range(num)]
    percentages = quick_sort(percentages)
    scores(percentages, num)

main()
