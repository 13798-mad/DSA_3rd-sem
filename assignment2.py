#In second year computer engineering class, group A student’s play cricket, group B students play badminton and group C students play football.
#Write a Python program using functions to compute following: -
#List of students who play both cricket and badminton
#List of students who play either cricket or badminton but not both
#Number of students who play neither cricket nor badminton
#Number of students who play cricket and football but not badminton.

def students(group_name):
    num = int(input(f"Enter the number of students in group {group_name}: "))
    student_list = [input(f"Enter name of student {i + 1} in group {group_name}: ") for i in range(num)]
    return set(student_list)

def main():
    # Get the list of students for each group
    cricket = students("A")
    badminton = students("B")
    football = students("C")

    # List of students who play both cricket and badminton
    both = cricket.intersection(badminton)
    print("List of students who play both cricket and badminton:", both)

    # List of students who play either cricket or badminton but not both
    either = cricket.symmetric_difference(badminton)
    print("List of students who play either cricket or badminton but not both:", either)

    # Number of students who play neither cricket nor badminton
    neither = football.difference(cricket.union(badminton))
    num_neither = len(neither)
    print("Number of students who play neither cricket nor badminton:", num_neither)

    # Number of students who play cricket and football but not badminton
    cricket_and_football = cricket.intersection(football).difference(badminton)
    num_cricket_and_football = len(cricket_and_football)
    print("Number of students who play cricket and football but not badminton:", num_cricket_and_football)

main()
