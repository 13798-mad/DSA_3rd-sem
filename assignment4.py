#Write a Python program to store first year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using
#Bubble sort and display top 5 scores

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def scores(arr, n):
    print("\nTop 5 Scores:")
    for i in range(n - 1, n - 6, -1):
        print(f"{n - i}. {arr[i]:.2f}%")

def main():
    num = int(input("Enter the number of students: "))
    percentages = [float(input(f"Enter the percentage of student {i + 1}: ")) for i in range(num)]
    bubble_sort(percentages)
    scores(percentages, num)

main()
