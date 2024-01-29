def calculate_average(marks):
    total_marks = sum(marks)
    average = total_marks / len(marks)
    return average

def find_highest_lowest(marks):
    highest_score = max(marks)
    lowest_score = min(marks)
    return highest_score, lowest_score

def count_absent_students(marks):
    absent_students = marks.count(0)  # Assuming 0 represents an absent mark
    return absent_students

def mark_with_highest_frequency(marks):
    frequency_dict = {}
    for mark in marks:
        if mark in frequency_dict:
            frequency_dict[mark] += 1
        else:
            frequency_dict[mark] = 1

    max_frequency = max(frequency_dict.values())
    most_frequent_marks = [mark for mark, frequency in frequency_dict.items() if frequency == max_frequency]

    return most_frequent_marks

marks = []
n=int(input("enter number of students:"))
for i in range(n):
    mark=int(input("enter marks:"))
    marks.append(mark)

average_score = calculate_average(marks)
highest_score, lowest_score = find_highest_lowest(marks)
absent_students_count = count_absent_students(marks)
most_frequent_marks = mark_with_highest_frequency(marks)
def main():
    print(f"Average Score: {average_score}")
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")
    print(f"Number of Absent Students: {absent_students_count}")
    print(f"Mark(s) with Highest Frequency: {most_frequent_marks}")
main()