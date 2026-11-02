# 📊 Python Data Visualization – NYC Taxi Dataset

## 📌 Project Overview
This project focuses on exploring and visualizing the NYC Taxi dataset using Python. It demonstrates data cleaning, missing value treatment, exploratory data analysis, and different visualization techniques using Matplotlib, Pandas, and Seaborn.

## 🎯 Objectives
- Load and explore the NYC Taxi dataset.
- Identify and handle missing values.
- Analyze taxi fares, trip distances, tips, and payment methods.
- Understand relationships between numerical variables.
- Create meaningful visualizations to identify patterns and trends.

## 🛠️ Technologies & Libraries
- **Python** – Data analysis and visualization.
- **Pandas** – Data manipulation and analysis.
- **Matplotlib** – Data visualization.
- **Seaborn** – Statistical data visualization.

## 📂 Dataset
**Dataset:** Taxis Dataset

**Source:** Seaborn built-in dataset.

```python
import seaborn as sns

df = sns.load_dataset("taxis")
```

## 🔍 Data Cleaning
- Checked missing values across dataset columns.
- Identified numerical and categorical columns with missing data.
- Applied appropriate imputation techniques:
  - Mean
  - Median
  - Mode
- Removed rows where missing values could not be reasonably imputed.

## 📈 Data Visualization

### 1. Matplotlib & Pandas Visualizations

| Visualization | Analysis |
|---|---|
| 📉 Line Chart | Fare trends over pickup time |
| 📊 Bar Chart | Total fare by pickup borough |
| 🥧 Pie Chart | Trip distribution by payment method |
| 📶 Histogram | Distribution of trip distances |
| 📦 Box Plot | Tip distribution across pickup boroughs |

### 2. Seaborn Visualizations

| Visualization | Analysis |
|---|---|
| 📊 Count Plot | Number of trips by pickup borough |
| 🔵 Scatter Plot | Relationship between distance and fare |
| 🌡️ Heatmap | Correlation between numerical variables |
| 🔗 Pair Plot | Pairwise relationships between numerical variables |
| 🎻 Violin Plot | Fare distribution by payment method |

## 📊 Key Analytical Areas
- Taxi fare distribution over time.
- Borough-wise fare comparisons.
- Payment method preferences.
- Trip distance patterns.
- Relationship between distance and fare.
- Correlation between fare, tip, tolls, and total amount.

## 💡 Skills Demonstrated
- Data Cleaning & Preprocessing
- Missing Value Treatment
- Exploratory Data Analysis (EDA)
- Data Visualization
- Statistical Analysis
- Python Data Analysis Libraries
- Data Interpretation

## 👨‍💻 Author
**P. Manikanta**

📍 Hyderabad, India

🔗 [LinkedIn](https://www.linkedin.com/in/manikantaa1999)

💻 [GitHub](https://github.com/PerumallaManikanta)

---
⭐ *Exploring data, discovering patterns, and transforming information into meaningful visual insights using Python.*