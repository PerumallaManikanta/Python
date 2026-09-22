#1. List Creation:
# Create a list named age_list with five integer elements. For eg., [24, 25, 26, 27, 28]

Age_list = [24, 25, 26, 27, 28]
print(Age_list)

# Create a list named name_list with five string elements.

name_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(name_list)

# 2. List Operations / Modifications:

# Append the string "Yazhini" to name_list.
name_list.append("Yazhini")
print(name_list)

# Insert the element 30 at index 2 in age_list.
Age_list.insert(2, 30)
print(Age_list)

# Remove the string "Yazhini" from name_list.

name_list.remove("Yazhini")
print(name_list)

# Pop the last element from age_list.

popped_age = Age_list.pop()
print(popped_age)
print(Age_list)


# Extend the age_list with additional ages [29, 30, 26].

Age_list = [24, 25, 30, 26, 27]
Age_list.extend([29, 30, 26])
print(Age_list)


# Sort age_list in descending order.

Age_list.sort(reverse=True)
print(Age_list)


# Find Max age, Min age and sum of all ages from age_list.

print(max(Age_list))
print(min(Age_list))
print(sum(Age_list))

#  Accessing List Elements:

# Print the first element of name_list.
print(name_list[0])

# Print the last element of name_list.
print(name_list[-1])

# Print the elements from index 2 to index 4 in name_list.
print(name_list[2:4])

# Print the elements of name_list in reverse order.
print(name_list[::-1])

# Dictionary (Creation, Modification and Access):

# Create a dictionary named student_marks that maps the names of five
# students to their marks (use scale of from 0 to 100).
student_marks ={"Alice": 85, "Bob": 90, "Charlie": 78, "David": 92, "Eve": 88}


# Access and print the mark of a specific student, of your choice.
print((student_marks["Alice"]))


# Add a new student "Janani" with a mark of 80 to the student_marks dictionary.
student_marks["Janani"] = 80
print(student_marks)


# Update the mark of any one older student to 82.
student_marks["Alice"] = 82
print(student_marks)



# Use the keys(), values(), and items() methods to print all keys, values, and
#key-value pairs in the student_marks dictionary.
print(student_marks, list(student_marks.keys()))
print(student_marks, list(student_marks.values()))
print(student_marks, list(student_marks. items()))

# Sets (Operations):

#Create a set called my_set with following values:
# ['a','e','i','o','u','a','a','i']
#Analyse the output and provide explanation for the same.
my_set = {'a','e','i','o','u','a','a','i'}
print(my_set)


#5(b). Attempt to change my_set[4]
# Attempt to change an element at index 4
# my_set[4] = 's'

#5(c). Create set1 and set2
# Create the first set
set1 = {1, 3, 5, 7, 9}
# Create the second set
set2 = {2, 3, 5, 8, 10}

# Print both sets
print("Set 1:", set1)
print("Set 2:", set2)

#5(d). Compute union and intersection
# Find the union of set1 and set2
union_set = set1.union(set2)
# Find the intersection of set1 and set2
intersection_set = set1.intersection(set2)
# Print the results
print("Union:", union_set)
print("Intersection:", intersection_set)




#7. Operators & Conditional Statements 
# Ask the user to enter a score
score = float(input("Enter your score (0 to 10): "))
# Check whether the score is within the valid range
if score < 0 or score > 10:
    print("Invalid score. Please enter a score between 0 and 10.")

# Check whether the score is greater than 7
elif score > 7:
    print("Above Average: Excellent work! Keep up the great performance.")

# Check whether the score is between 4 and 7
elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")

# If the score is less than 4
else:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")
