# 🐍 Python Data Analysis with NumPy and Pandas

A practical Python project demonstrating foundational data analysis techniques using **NumPy** and **Pandas**. The project explores numerical calculations, array indexing, Series operations, DataFrame exploration, filtering, aggregation, and data manipulation.

## 📌 Project Overview

This project covers three practical areas of data analysis:

- 🌡️ **NumPy Temperature Analysis** — Work with daily temperature readings across two weeks, convert Celsius to Fahrenheit, calculate summary statistics, and practice array indexing and slicing.
- 🎓 **Pandas Series Analysis** — Work with student marks and custom rank labels, access values by position and label, filter records, update values, remove an entry, and calculate CGPA using the specified formula.
- 🛒 **Pandas DataFrame Analysis** — Explore retail transactions, inspect data structure, select and filter records, summarize categories and regions, update a transaction amount, calculate a discount, and remove specified data.

## 🎯 Project Objectives

- Create and inspect one-dimensional and two-dimensional NumPy arrays.
- Perform numerical calculations and descriptive statistics.
- Practice array indexing and slicing.
- Create Pandas Series with custom indices.
- Use label-based indexing, position-based indexing, and Boolean filtering.
- Inspect DataFrame dimensions, columns, data types, and records.
- Filter rows, count category values, identify unique values, and group data for aggregation.
- Update values and add or remove DataFrame rows and columns.

## 🧰 Tools & Technologies

- 🐍 Python
- 🔢 NumPy
- 🧮 Pandas
- 💻 Jupyter Notebook or Visual Studio Code

## 📂 Data Overview

### 🌡️ 1. Temperature Data

Daily average temperatures are provided for two weeks, with seven readings per week.

| Week | Temperatures (°C) |
|---|---|
| Week 1 | 22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9 |
| Week 2 | 19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1 |

This data is used to practice array properties, Celsius-to-Fahrenheit conversion, maximum and minimum values, mean calculation, and slicing.

### 🎓 2. Student Marks

A Pandas Series stores marks with custom rank labels.

| Rank | Mark |
|---|---:|
| Rank1 | 95 |
| Rank2 | 92 |
| Rank3 | 89 |
| Rank4 | 85 |
| Rank5 | 80 |

The Series demonstrates label-based and position-based access, Boolean filtering, value updates, entry removal, and mark-to-CGPA conversion by dividing each mark by 10.

### 🛒 3. Retail Transactions

The transactions DataFrame contains 10 records and four initial columns.

| Column | Description |
|---|---|
| `TransactionID` | Identifier for each transaction |
| `ProductCategory` | Product category, such as Electronics, Clothing, or Furniture |
| `Region` | Region associated with the transaction |
| `Amount` | Transaction amount |

This data supports DataFrame exploration, filtering, category counts, unique-value checks, regional average calculations, and data manipulation.

## 🔍 Analysis & Operations

### 🔢 NumPy

- Create one-dimensional and two-dimensional arrays.
- Inspect array shape, data type, and number of elements.
- Convert Celsius to Fahrenheit using `F = (C × 9/5) + 32`.
- Calculate maximum, minimum, and mean temperatures.
- Extract the first three days, last two days, and middle three days using slicing.
- Select weekly temperatures and weekend readings from a two-dimensional array.

### 🎓 Pandas Series

- Create a Series with custom rank labels.
- Retrieve values using integer positions, `.loc`, and `.iloc`.
- Filter marks greater than 90 using a Boolean mask.
- Update the mark associated with `Rank1`.
- Remove the `Rank5` entry.
- Calculate CGPA by dividing each mark by 10.

### 🛒 Pandas DataFrame

- Inspect records using `.head()` and `.tail()`.
- Review `.shape`, `.columns`, `.dtypes`, and `.info()`.
- Select specific columns and retrieve columns by position.
- Filter transactions by region and amount.
- Count product categories and identify unique regions.
- Group transactions by region and calculate mean transaction amounts.
- Update the amount for transaction `102`.
- Calculate a 10% discount in a `Discount` column.
- Remove transaction `109` and delete the `Discount` column.

## 💡 Skills Demonstrated

- Python fundamentals for data analysis
- NumPy array creation, properties, calculations, and slicing
- Pandas Series and DataFrame operations
- Data inspection and exploratory data analysis
- Boolean indexing and conditional filtering
- Grouping and aggregation
- Data transformation and manipulation
- Analytical thinking and problem-solving

## ⚙️ Getting Started

### 1️⃣ Install the libraries

```bash
pip install numpy pandas
```

### 2️⃣ Import the libraries

```python
import numpy as np
import pandas as pd
```

### 3️⃣ Run the analysis

Open the Python script or Jupyter Notebook in **Visual Studio Code** or **Jupyter Notebook** and run the code. The examples use the temperature, student marks, and retail transaction data documented above.

## 🗂️ Suggested Project Structure

```text
python-data-analysis-numpy-pandas/
├── README.md
└── python_data_analysis.ipynb
```

*The notebook filename is a suggested example. Keep the filename that matches your actual repository.*

## 📈 Expected Outcomes

This project demonstrates how NumPy supports numerical computation and how Pandas helps organize, explore, filter, summarize, and transform structured data. These techniques provide a foundation for larger data analysis and reporting projects.

## 👤 Author

**P. Manikanta**

- 🔗 LinkedIn: [linkedin.com/in/manikantaa1999](https://linkedin.com/in/manikantaa1999)
- 💻 GitHub: [github.com/PerumallaManikanta](https://github.com/PerumallaManikanta)

---

✨ *Exploring data and building practical Python data analysis skills with NumPy and Pandas.*
