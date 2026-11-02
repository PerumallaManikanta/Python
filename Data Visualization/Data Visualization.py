

from turtle import pd

import matplotlib.pyplot as plt
import seaborn as sns
# Load the 'taxis' dataset
df = sns.load_dataset("taxis")

print(df)

print(df.info())

print(df.columns)

print(df.describe())

#2) Handling Missing Values

#➢ Impute missing values using appropriate strategies based on the column type (e.g.,
#using mean, median, or mode for numerical columns, and mode for categorical
#columns).
#➢ For columns that are critical and cannot be reasonably imputed, remove rows with
#missing values to maintain data integrity.

#➢ Check for missing values in the dataset and identify columns with missing data.

print((df.isnull().sum() / len(df)) * 100)

# Separate numerical and categorical columns

import numpy as np

num_cols = df.select_dtypes(include=np.number).columns

cat_cols = df.select_dtypes(include="object").columns

# Fill numerical missing values using median

for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill categorical missing values using mode
for col in cat_cols:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])

# Remove rows where critical timestamps are missing

df = df.dropna(subset=["pickup"])

# Verify missing values

print(df.isnull().sum())



# 3.1 Line Chart – Fare Over Time

# Sort data by pickup timestamp
line_data = df.sort_values("pickup").copy()

# Calculate hourly average fare
hourly_fare = (
    line_data.set_index("pickup")["fare"]
    .resample("h")
    .mean()
    .dropna()
)

# Create line chart
plt.figure(figsize=(12, 5))

plt.plot(hourly_fare.index, hourly_fare.values)

plt.title("Average Fare Over Time")
plt.xlabel("Pickup Timestamp")
plt.ylabel("Average Fare")

plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()


# 3.2 Bar Chart – Total Fare by Pickup Borough

# Group by pickup borough
borough_fare = df.groupby(
    "pickup_borough", observed=True
)["fare"].sum()

# Create bar chart
borough_fare.plot(
    kind="bar",
    figsize=(9, 5),
    title="Total Fare by Pickup Borough"
)

plt.xlabel("Pickup Borough")
plt.ylabel("Total Fare")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 3.3 Pie Chart – Payment Method Distribution

# Count payment methods
payment_counts = df["payment"].value_counts()

# Create pie chart
plt.figure(figsize=(7, 7))

plt.pie(
    payment_counts,
    labels=payment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Distribution of Trips by Payment Method")
plt.show()


# 3.4 Histogram – Distance Distribution

plt.figure(figsize=(9, 5))

plt.hist(
    df["distance"].dropna(),
    bins=30,
    edgecolor="black"
)

plt.title("Distribution of Taxi Trip Distance")
plt.xlabel("Distance")
plt.ylabel("Frequency")

plt.grid(axis="y")
plt.show()

# 3.5 Box Plot – Tip Distribution by Pickup Borough

plt.figure(figsize=(10, 5))

df.boxplot(
    column="tip",
    by="pickup_borough",
    figsize=(10, 5)
)

plt.title("Tip Distribution by Pickup Borough")
plt.suptitle("")
plt.xlabel("Pickup Borough")
plt.ylabel("Tip Amount")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 4. Visualizations Using Seaborn

# 4.1 Count Plot – Trips by Pickup Borough

plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    x="pickup_borough"
)

plt.title("Number of Trips by Pickup Borough")
plt.xlabel("Pickup Borough")
plt.ylabel("Number of Trips")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4.2 Scatter Plot – Distance vs Fare

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="distance",
    y="fare",
    hue="pickup_borough",
    alpha=0.6
)

plt.title("Relationship Between Distance and Fare")
plt.xlabel("Distance")
plt.ylabel("Fare")

plt.legend(title="Pickup Borough")
plt.show()

# 4.3 Heatmap – Correlation Between Numerical Variables

# Select numerical columns
corr_data = df[
    ["distance", "fare", "tip", "tolls", "total"]
]

# Calculate correlation
correlation = corr_data.corr()

# Create heatmap
plt.figure(figsize=(9, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Heatmap")
plt.show()


# 4.4 Pair Plot – Pairwise Relationships

# Select top 5 pickup zones for readability
top_zones = df["pickup_zone"].value_counts().head(5).index

pair_data = df[
    df["pickup_zone"].isin(top_zones)
][["distance", "fare", "tip", "total", "pickup_zone"]].dropna()

# Create pair plot
sns.pairplot(
    pair_data,
    hue="pickup_zone",
    diag_kind="hist"
)

plt.show()

# 4.5 Violin Plot – Fare by Payment Method

plt.figure(figsize=(9, 5))

sns.violinplot(
    data=df,
    x="payment",
    y="fare"
)

plt.title("Fare Distribution by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Fare")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()