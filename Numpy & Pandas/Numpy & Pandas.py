## 1. Create a 1D NumPy Array:

import numpy as np

temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])

## 2. Inspection and Properties: 

# shape of array

print(temperatures_w1.shape)

# Data type of array

print(temperatures_w1.dtype)

# Number of elements in the array

print(f"Number of elements in the array :{len(temperatures_w1)}")


## 3. Array Operations:

temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])

Fahrenheit = (temperatures_w1 * 9/5) + 32

print(Fahrenheit)

## 4. Array Slicing and Indexing:

# Extract the temperatures for the first three days of the week.

print(temperatures_w1[0:3])

# Extract the temperatures for the weekend (last two days).

print(temperatures_w1[-2:])

# Extract the temperatures for the middle three days of the week.

print(temperatures_w1[2:5])

## 5. Create a 2D Array:

temperatures_w1 = np.array([[22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9]])

temperatures_w2 = np.array([[19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]])

## 6. Inspect and Slice the 2D Array:

# shape of 2D array
print(temperatures_w1.shape)
print(temperatures_w2.shape)

# Data types of 2D array

print(temperatures_w1.dtype)
print(temperatures_w2.dtype)

# slice

print(temperatures_w1[-2:])
print(temperatures_w2[-2:])


## Pandas 

# Creating Pandas Series:

import pandas as pd

# 1. Creating Pandas Series:
marks = {
    'marks':[95,92,89,85,80],
    'Custom_Indices': ['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5']
}

series = pd.Series(marks)

print(series)

# 2. Indexing and Slicing:

series = pd.Series([95,92,89,85,80] , index = ['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5'])

print(f"First Rank :{series['Rank1']}")

# loc 

print(series.loc['Rank1':'Rank3'])

# iloc

print(series.iloc[0:3])

#Boolean

print(series[series>90])



# Modify the mark of the student with the 1st rank to 100.
import pandas as pd

# Step 1: Create a Pandas Series with custom indices
marks = pd.Series(
    [95, 92, 89, 85, 80],
    index=['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5']
)

print("Original Marks Series:")
print(marks)

# Step 2: Modify the mark of the 1st rank to 100
marks['Rank1'] = 100

print("\nAfter Modifying Rank1:")
print(marks)

# Step 3: Remove the entry corresponding to the last rank
marks = marks.drop('Rank5')

print("\nAfter Removing Rank5:")
print(marks)

# Step 4: Compute CGPA by dividing each mark by 10
cgpa = marks / 10

print("\nCGPA Series:")
print(cgpa)


# Pandas DataFrame:

# 1. Creating Pandas DataFrame:

transactions = {
    'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'ProductCategory': ['Electronics', 'Clothing', 'Electronics', 'Furniture','Clothing', 'Electronics', 'Furniture', 'Clothing', 'Furniture', 'Electronics'],
    'Region': ['North', 'South', 'North', 'East', 'West', 'North', 'East', 'West','South', 'North'],
    'Amount': [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
}

df = pd.DataFrame(transactions)

# Modify the amount for transaction 102.
df.loc[df['TransactionID'] == 102, 'Amount'] = 165
print(df.loc[df['TransactionID'] == 102])

print(df)

# 2. Data Exploration:

print(df.head()) # head

print(df.tail()) # tail

print(df.shape) # shape

print(df.columns)  # columns

print(df.dtypes)   # Data types

# display ProductCategory and Amount

# ProductCategory
print(df['ProductCategory'])

# Amount

print(df['Amount'])

# Retrieve the last 3 columns of the DataFrame using iloc or loc.

df = df.loc[0:,['ProductCategory','Region','Amount']]

print(df)

df = df.iloc[0:,0:3]

print(df)

# Filter rows where the 'Region' is 'North' and 'Amount' is greater than 200.

FR = df[df['Region'] =='North'] 

print(FR)

print(FR['Amount']>200)

# Find the value counts for the 'ProductCategory' column.

print(df.value_counts(),['ProductCategory'])

# Find the unique values in the 'Region' column.

print(df['Region'].unique)

# Group by 'Region' and find the mean amount for each region.

transactions_grp = df.groupby('Region')['Amount'].mean()

print(transactions_grp)

# Modify the 'Amount' for the transaction with TransactionID 102 to 165.

import pandas as pd

# Step 1: Create a Pandas DataFrame
transactions = pd.DataFrame({
    'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'ProductCategory': [
        'Electronics', 'Clothing', 'Electronics', 'Furniture',
        'Clothing', 'Electronics', 'Furniture', 'Clothing',
        'Furniture', 'Electronics'
    ],
    'Region': [
        'North', 'South', 'North', 'East', 'West',
        'North', 'East', 'West', 'South', 'North'
    ],
    'Amount': [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
})

print("Original DataFrame:")
print(transactions)

# Step 2: Modify Amount for TransactionID 102 to 165
transactions.loc[transactions['TransactionID'] == 102, 'Amount'] = 165

print("\nAfter Modifying Amount:")
print(transactions)

# Step 3: Add Discount column (10% of Amount)
transactions['Discount'] = transactions['Amount'] * 0.10

print("\nAfter Adding Discount:")
print(transactions)

# Step 4: Remove the row with TransactionID 109
transactions = transactions.drop(
    transactions[transactions['TransactionID'] == 109].index
)

print("\nAfter Removing TransactionID 109:")
print(transactions)

# Step 5: Delete the Discount column
transactions = transactions.drop(columns=['Discount'])

print("\nFinal DataFrame:")
print(transactions)








