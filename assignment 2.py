
age_list = [24, 25, 26, 27, 28]

name_list = ["Athul", "Beena", "Dhamu", "Divya", "Pachu"]

print("Age List:", age_list)
print("Name List:", name_list)


name_list.append("Yazhini")

age_list.insert(2, 30)

name_list.remove("Yazhini")

age_list.pop()

age_list.extend([29, 30, 26])

age_list.sort(reverse=True)

max_age = max(age_list)
min_age = min(age_list)
sum_of_ages = sum(age_list)

print("Updated Name List:", name_list)
print("Sorted Age List (Descending):", age_list)
print("Max Age:", max_age)
print("Min Age:", min_age)
print("Sum of Ages:", sum_of_ages)



name_list = ["Athul", "Beena", "Dhamu", "Divya", "Pachu"]

print("First element:", name_list[0])
print("Last element:", name_list[-1])
print("Elements from index 2 to 4:", name_list[2:5])
print("Reversed name_list:", name_list[::-1])


student_marks = {
    "Athul": 85,
    "Beena": 92,
    "Dhamu": 78,
    "Divya": 88,
    "Pachu": 90
}    

print("Mark of Binu:", student_marks["Beena"])

student_marks["Janani"] = 80

student_marks["Dhamu"] = 82

print("Updated student_marks:", student_marks)


student_marks = {
    "Athul": 85,
    "Beena": 92,
    "Dhamu": 82,
    "Divya": 88,
    "Pachu": 90,
    "Janani": 80
}
print("Keys (Student Names):", student_marks.keys())
print("Values (Marks):", student_marks.values())
print("Key-Value Pairs:", student_marks.items())

my_set = set(['a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'])
print("a. Output of my_set:", my_set)

try:
    my_set[4] = 's'
except TypeError as e:
    print("b. Error when modifying element:", e)
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

union_set = set1.union(set2)          
intersection_set = set1.intersection(set2)  

print("d. Union of set1 and set2:", union_set)
print("   Intersection of set1 and set2:", intersection_set)


score = float(input("Enter your score (0 to 10): "))
if score > 7:
    print("Above Average: Excellent performance! Keep up the great work.")
elif 4 <= score <= 7:
    print("Average: Good effort! Keep practicing, there's room for improvement.")
else:
    print("Below Average: Need to improve your performance, consistent practice will lead to better results.")

