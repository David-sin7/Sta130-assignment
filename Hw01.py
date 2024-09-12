#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Prelecture question 1 
import pandas as pd
url = "https://gist.githubusercontent.com/ycui1/dd33483219aeec871b9137a1e7925235/raw/6ae3e4e51b4807313068244dd315eb5e0a989827/pandas_missing_values_dataset.csv"
df = pd.read_csv(url)
df.isna().sum()



# In[12]:


#Prelecture qusetion 1 1)
rows, columns = df.shape
print(f'The dataset has {rows} rows and {columns} columns.')

#Prelecture qusetion 1 2)
#Observation is data or answers collected from a specific substance or scene.
#variables are some specific attributes or responses from the subjects in certain conditions. 


# In[29]:


#Prelecture qusetion 2
data = pd.read_csv('https://gist.githubusercontent.com/ycui1/dd33483219aeec871b9137a1e7925235/raw/6ae3e4e51b4807313068244dd315eb5e0a989827/pandas_missing_values_dataset.csv')

summary = data.describe()
print("Statistical Summary:\n", summary)

value_counts_q2 = data['q2'].value_counts()
print("\nValue Counts for column 'q2':\n", value_counts_q2)

value_counts_q4 = data['q4'].value_counts()
print("\nValue Counts for column 'q4':\n", value_counts_q4)


# Prelecture qusetion 3
# df.shape will give the size of the dataset including the missing value
# df.describe() will tell us how many columns contain numerical data.

# Prelecture qusetion 4
# a） An attribute stores some kind of value or information about the object,
# A method is a function that you can call to perform operations or calculations

# #post-lecture question 6
# Definition: 
# Count:
# The number of non-missing (non-NaN) values in the column. It represents how many valid entries are available for each variable.
# 
# Mean:
# The average of the values in the column, calculated by summing all non-missing values and dividing by the count of those values
# 
# Std (Standard Deviation):
# A measure of the spread or dispersion of the values in the column. It shows how much the values deviate, on average, from the mean. A higher standard deviation indicates more variability.
# 
# Min:
# The minimum or smallest value in the column.
# 
# 25% (First Quartile):
# This is the value below which 25% of the data falls. It’s also called the first quartile (Q1). It gives a sense of the lower part of the data distribution.
# 
# 50% (Median or Second Quartile):
# The median value, also called the second quartile (Q2). This is the middle value that separates the lower half and the upper half of the data. In other words, 50% of the data lies below this value.
# 
# 75% (Third Quartile):
# This is the value below which 75% of the data falls, also called the third quartile (Q3). It gives a sense of the upper part of the data distribution.
# 
# Max:
# The maximum or largest value in the column.
# 
# Why These Statistics Only Apply to Numeric Variables:
# These summary statistics—mean, standard deviation, and percentiles—are only meaningful for numeric data. They require mathematical operations (like summing or calculating deviations), which don’t make sense for categorical or string variables. This is why df.describe() by default only analyzes numeric columns.
# 
# How df.describe() Handles Missing Data:
# Missing values (NaNs) are ignored when calculating statistics. This means that df.describe() computes statistics only on the non-missing (valid) values in the column.(For example, if a column has 10 rows but 2 of them are missing, the count will be 8, and the mean, standard deviation, etc., will be calculated based on those 8 valid values.)
# Count will reflect the number of non-missing values for each variable, not the total number of rows in the dataset. This is important when there are missing values, as it indicates how many data points were actually used to compute the statistics.
# 
# Implications for Handling Missing Data:
# df.describe() handles missing values implicitly by excluding them from the calculations. It can still provide meaningful summaries, which suggests that missing data doesn't always need to be removed before using certain methods.However, not all methods in data analysis handle missing data the same way. For example, certain machine learning models or statistical tests may fail or produce inaccurate results if missing values are not explicitly addressed (e.g., by removing them or filling them in through imputation).

# post-lecture question 7:
# 1) In a medical dataset where each row represents a patient, if only a few patients have missing data for certain variables, you might choose to eliminate those specific rows using df.dropna(), ensuring that the remaining dataset stays complete.
# 
# 2) In a customer survey dataset with a column for optional comments where 80% of the data is missing, you could choose to remove that comments column entirely using del df['col'] since it doesn’t add much to your analysis, preserving the more valuable customer demographic data.
# 
# 3) Deleting the column with many missing values before using df.dropna() can be important. By removing the column first, you decrease the overall number of missing data points, meaning fewer rows will be dropped by df.dropna(). If you don’t remove the column beforehand, df.dropna() could delete rows unnecessarily, causing you to lose data that is still useful in other parts of the dataset.
# 
# 4) 
# before 
# Before:
# 
# Name	Email	Phone	Age	Feedback
# John	john@example.com	123-456-7890	28	NaN
# Alice	alice@example.com	NaN	35	Great service
# Bob	bob@example.com	987-654-3210	NaN	NaN
# Carol	carol@example.com	NaN	22	Good experience
# 
# 
# after: 
# John	john@example.com	123-456-7890	28
# 
# Further Guidance: 
# Making a Copy of Data:
# Before making any modifications to your dataset, it's a good practice to create a backup copy. This ensures you can always "undo" or revert changes by reloading the original copy if something doesn't work as expected.
# Undoing Changes:
# If changes made to the dataset are not what you expected, you can restore the original dataset using the backup copy (df_saved). This is why creating a copy is so important before making modifications.
# Checking the State of Data:
# You need to ensure that the state of the dataset (df) aligns with what your code expects. If you previously ran code that modified the dataset and didn’t save a copy, the structure may no longer match the assumptions of the current code.
# Before executing new code, always double-check the structure of your dataframe using df.info() or df.head() to verify that it looks as expected.
# Handling Errors:
# If you encounter Python errors, you can copy and paste the error message here, and I can assist in troubleshooting it.
# It’s also important to make sure the objects (dataframes, lists, etc.) in your environment haven’t been unexpectedly changed or deleted, which could lead to errors like NameError or KeyError.

# In[ ]:


#Code for 7.4:
    import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob', 'Carol'],
    'Email': ['john@example.com', 'alice@example.com', 'bob@example.com', 'carol@example.com'],
    'Phone': ['123-456-7890', None, '987-654-3210', None],
    'Age': [28, 35, None, 22],
    'Feedback': [None, 'Great service', None, 'Good experience']
}


df = pd.DataFrame(data)

before_report = df.copy()


del df['Feedback']


df_cleaned = df.dropna()


after_report = df_cleaned.copy()

import ace_tools as tools; tools.display_dataframe_to_user(name="Before Data Cleanup", dataframe=before_report)
tools.display_dataframe_to_user(name="After Data Cleanup", dataframe=after_report)


# Question 8: 
# 1. It groups the data by unique values in col1 and describe col2 in each group including using Count, Mean, Standard deviation, Min, 25%, 50%, and 75% percentiles, Max
# example: 
# pclass	survived	name	sex	age	sibsp	parch	ticket	fare	cabin	embarked	boat	body	home.dest
# 1	1	Lurette, Miss. Elise	female	58	0	0	PC 17569	146.5208	B80	C			
# 1	1	Madill, Miss. Georgette Alexandra	female	15	0	1	24160	211.3375	B5	S	2		St Louis, MO
# 2	1	Faunthorpe, Mrs. Lizzie (Elizabeth Anne Wilkinson)	female	29	1	0	2926	26.0000		S	16		
# 2	0	Fillbrook, Mr. Joseph Charles	male	18	0	0	C.A. 15185	10.5000		S			Cornwall / Houghton, MI
# if I used it as an example, the code will be df.groupby("pclass")["fare"].describe(). then the code will group them using pclass and using the data in age to make anaylze. and the answer output will be 
# 
#         count      mean         std        min        25%        50%        75%        max
# pclass                                                                                    
# 1       3.0      189.7320    37.306      146.5208    178.9292    211.3375   211.3375   211.3375
# 2       2.0       18.2500    10.964      10.5000     14.3750     18.2500    22.1250    26.0000
# 
# 
# 

# Question 8: 
# 2 df.describe will analyze each row indepently for each non-missing value. df.groupby("col1")["col2"].describe() is using col1 to seperate them into different group and then using the value of col2 to analyze.
# 3.Compared to Google Search, ChatGPT is better at analyzing and explaining code, as well as providing possible advice and suggestions. Google Search relies on users' or companies' past responses. So i believe chatgpt is better than the google search.

# Question 9:
# Yeah, really hard to understand in first time

# #summary 
# #Here’s a summary of the key points covered in this session:
# 
# #Dataset Summarization:
# 
# #We reviewed how to use df.describe() for summarizing numeric columns and df['column'].value_counts() for counting unique values in specific columns.
# #You learned how df.describe() provides statistics like count, mean, and standard deviation for numeric columns, and how df['column'].value_counts() is useful for counting occurrences in categorical columns.
# 
# #Differences Between df.shape and df.describe():
# #df.shape reports the total number of rows and columns in the dataset, regardless of missing values or data types.
# #df.describe() provides statistics only for numeric columns by default, and the count reflects only non-missing values.
# 
# #Understanding Attributes and Methods:
# #Attributes (like df.shape) store a specific value or information about the DataFrame without performing any calculations.
# #Methods (like df.describe()) are functions that perform operations or calculations when called with parentheses ().
# 
# #Handling Missing Values:
# #You learned that the "count" reported by df.describe() reflects only non-missing values, which may lead to discrepancies between the total rows in df.shape and the count in df.describe() when missing data is present.
# 
# #Clarification of Attributes and Methods:
# #Attributes store values directly related to an object (e.g., DataFrame dimensions), while methods perform operations on the object (e.g., calculating statistics or transforming data).
# #ChatGpt link : https://chatgpt.com/share/a67aa256-124c-46e2-a8e8-ce48aaf06c6c

# Chatgpt Summary before Question 7:
# Understanding Attributes vs. Methods in Pandas:
# 
# Attributes (like df.shape) store properties about the DataFrame, such as its size, and do not require parentheses ().
# Methods (like df.describe()) are functions that perform calculations or operations on the DataFrame, requiring parentheses to execute.
# Using df.describe() and df['column'].value_counts():
# 
# df.describe() provides summary statistics for numeric columns, such as count, mean, standard deviation, min, max, and percentiles (25%, 50%, and 75%).
# df['column'].value_counts() counts the occurrences of unique values in a column, particularly useful for categorical data.
# Discrepancies Between df.shape and df.describe():
# 
# df.shape reports the total number of rows and columns in the dataset, including missing values.
# df.describe() only calculates summary statistics for non-missing values and applies only to numeric columns unless otherwise specified.
# The "count" in df.describe() represents the number of non-missing values, which can be less than the total number of rows due to missing data.
# Handling Missing Data in df.describe():
# 
# df.describe() automatically handles missing data by excluding NaN values from its calculations. This means it still provides summary statistics even if there are missing values in the column.
# Not all methods handle missing data as gracefully as df.describe() does, so sometimes it is necessary to explicitly remove or impute missing values.
# Definitions of Summary Statistics:
# 
# Count: Number of non-missing values in the column.
# Mean: Average of non-missing values.
# Std: Standard deviation, showing the spread of the data.
# Min: Smallest value.
# 25%, 50%, 75%: Percentiles representing the distribution of the data.
# Max: Largest value.
# Working with Non-Numeric Data:
# 
# The statistics provided by df.describe() only apply to numeric data by default, as mean, standard deviation, and percentiles cannot be calculated for categorical or non-numeric data. You can, however, include non-numeric data by using df.describe(include=['object']).
# Code Examples Shared:
# Loading and Summarizing the Dataset:
# 
# python
# import pandas as pd
# 
# 
# data = pd.read_csv('path_to_your_file.csv')
# 
# 
# print("Shape of the dataset (rows, columns):", data.shape)
# 
# print("\nSummary of numeric columns:\n", data.describe())
# Using value_counts() for Categorical and Numeric Columns:
# 
# 
# 
# print("\nValue counts for column 'q2':\n", data['q2'].value_counts())
# 
# print("\nValue counts for column 'q4':\n", data['q4'].value_counts())
# Coding Results Summary:
# Shape of the Dataset:
# he dataset (rows, columns): (number of rows, number of columns)
# Summary of Numeric Columns:
# 
# python
# Summary of numeric columns:
#     subject_id       q1        q4
# count    20.0         15        18
# mean    1010.5        5.5       6.2
# std       5.91        1.8       3.2
# min     1001          3.0       1.0
# 25%     1005.75       4.0       4.0
# 50%     1010.5        5.0       5.0
# 75%     1015.25       7.0       8.0
# max     1020          9.0      12.0
# Value Counts for q2 and q4:
# 
# python
# Value counts for column 'q2':
# Agree             5
# Disagree          5
# Strongly Agree    3
# Neutral           2
# python
# 
# Value counts for column 'q4':
# 5     3
# 8     3
# 7     2
# 4     1
# 12    1
# 
# #chatgpt link: https://chatgpt.com/share/a67aa256-124c-46e2-a8e8-ce48aaf06c6c

# In[ ]:


Chatgpt link: https://chatgpt.com/share/6411f63f-8b57-4836-8606-d7d010ab125d
              https://chatgpt.com/share/a67aa256-124c-46e2-a8e8-ce48aaf06c6c
                

