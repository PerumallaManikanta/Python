feedback_data = {
'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
'Feedback': [
' Very GOOD Service!!!',
'poor support, not happy ',
'GREAT experience! will come again.',
'okay okay...',
' not BAD',
'Excellent care, excellent staff!',
'good food and good ambience!',
'Poor response and poor handling of issue',
'Satisfied. But could be better.',
'Good support... quick service.'
],
'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

print(feedback_data)

# ● Ask the user to enter how many more feedbacks they want to add.
num_new_feedbacks = int(input("How many more feedbacks do you want to add? "))

print(f"Please enter the details for {num_new_feedbacks} new feedbacks:")




n = int(input("How many feedbacks do you want to add? "))

for i in range(n):
    print("\nEnter details for feedback", i + 1)

    name = input("Enter name: ")
    feedback = input("Enter feedback: ")
    rating = int(input("Enter rating (1-5): "))

    s_no = len(feedback_data['S_No']) + 1

    feedback_data['S_No'].append(s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

print("\nFeedbacks added successfully!")

print(i)


#Text Cleaning

for i in range(len(feedback_data['Feedback'])):

    text = feedback_data['Feedback'][i]

    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace("!", "")
    text = text.replace("?", "")

    text = " ".join(text.split())

    text = text.strip()

    text = text.lower()

    feedback_data['Feedback'][i] = text

print("Feedbacks cleaned successfully!")
print(feedback_data['Feedback'])


# 4

def count_word_in_feedbacks(word):
    count = 0

    for feedback in feedback_data['Feedback']:
        words = feedback.split()

        if word.lower() in words:
            count += 1

    return count


print("Good:", count_word_in_feedbacks("good"))
print("Poor:", count_word_in_feedbacks("poor"))
print("Excellent:", count_word_in_feedbacks("excellent"))

print(feedback_data)

print("Average Rating:", sum(feedback_data['Rating']) / len(feedback_data['Rating']))



print("\nFeedback with the longest comment:")
longest_feedback = max(feedback_data['Feedback'], key=lambda x: len(x.split()))
print(longest_feedback)


unique_words = set()
for feedback in feedback_data['Feedback']:
    words = feedback.split()
    unique_words.update(words)

print("\nUnique words used across all feedbacks:")
print(unique_words)


sorted_feedbacks = sorted(zip(feedback_data['S_No'], feedback_data['Name'], feedback_data['Feedback'], feedback_data['Rating']), key=lambda x: x[3], reverse=True)

print("\nFeedbacks sorted by rating (highest to lowest):")
for s_no, name, feedback, rating in sorted_feedbacks:
    print(f"S.No: {s_no}, Name: {name}, Feedback: {feedback}, Rating: {rating}")
