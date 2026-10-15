# 📊 Survey Feedback Analyzer

## 📌 Project Overview

The **Survey Feedback Analyzer** is a Python-based tool designed to
organize, clean, and analyze written survey feedback. It uses core
Python concepts to extract useful insights from customer comments and
ratings.

## 🎯 Objectives

-   🗂️ Store feedback details in a dictionary of lists.
-   ✍️ Collect additional feedback from users.
-   🧹 Clean text by removing punctuation, extra spaces, and
    inconsistent capitalization.
-   🔎 Count feedback entries containing specific words.
-   📈 Calculate the average rating and identify the longest comment.
-   🧩 Find unique words used across feedback entries.

## 🛠️ Concepts Used

-   Python dictionaries and lists
-   `input()` and user interaction
-   `for` loops and conditional statements
-   String methods such as `replace()`, `split()`, and `' '.join()`
-   User-defined functions
-   Word counting and duplicate removal
-   `zip()` and `sorted()` for optional rating-based sorting

## ⚙️ Key Features

### 📥 Preloaded Feedback

Starts with 10 feedback records containing a serial number, name,
written feedback, and rating.

### ✍️ Add New Feedback

Allows users to specify how many feedback entries to add. Each entry
includes a name, written comment, and rating from 1 to 5. Serial numbers
continue from 11 onward.

### 🧹 Text Cleaning

Standardizes feedback by: - Removing punctuation such as periods,
commas, exclamation marks, and question marks - Replacing multiple
spaces with a single space - Removing leading and trailing spaces -
Converting text to lowercase

### 🔍 Word-Based Insights

Counts how many feedback entries contain each of these words: - `good` -
`poor` - `excellent`

The `count_word_in_feedbacks(word)` function performs a case-insensitive
match.

### 📊 Summary and Insights

-   Displays the cleaned feedback dictionary
-   Calculates the average rating
-   Finds the feedback with the longest comment by word count
-   Displays the unique words used across all feedback
-   Optionally sorts feedback entries from highest to lowest rating

## ▶️ How to Run

1.  Make sure Python 3 is installed.

2.  Save the program in a Python file, such as
    `survey_feedback_analyzer.py`.

3.  Open a terminal in the file's directory.

4.  Run:

    ``` bash
    python survey_feedback_analyzer.py
    ```

5.  Follow the prompts to add feedback and view the analysis.

## 📂 Data Structure

The feedback is stored in a dictionary of lists with these fields:

  Field        Description
  ------------ ----------------------------------------------
  `S_No`       Unique serial number for each feedback entry
  `Name`       Name of the person providing feedback
  `Feedback`   Written feedback comment
  `Rating`     Rating from 1 to 5

## 💡 Outcome

This project demonstrates how Python can be used to collect, clean, and
analyze textual feedback, summarize ratings, and extract simple insights
from unstructured comments.
