#3: Introducing to the data
'''
Instructions
Read all-ages.csv into a DataFrame object, and assign it to all_ages.
Read recent-grads.csv into a DataFrame object, and assign it to recent_grads.
Display the first five rows of all_ages and recent_grads.
'''

import pandas as pd

all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
print(all_ages[:5])
print(recent_grads.head(5)

#4: Summarizing Major Categories
'''
Use the Total column to calculate the number of people who fall under each Major_category in each data set.
Store the result as a separate dictionary for each data set.
The key for the dictionary should be the Major_category, and the value should be the total count.
For the counts from all_ages, store the results as a dictionary named aa_cat_counts.
For the counts from recent_grads, store the results as a dictionary named rg_cat_counts.
'''
# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()

def calculate_major_cats(df):
    cats = df['Major_category'].unique()
    counts_dict = dict()
    
    for c in cats:
        major_df = df[df["Major_category"] == c]
        total = major_df["Total"].sum(axis=0)
        counts_dict[c] =total
    return counts_dict

aa_cat_counts = calculate_major_cats(all_ages)
rg_cat_counts = calculate_major_cats(recent_grads)

#5: Low-Wage Job Rates

'''
Use the Low_wage_jobs and Total columns to calculate the proportion of recent college graduates that worked low wage jobs.
Recall that you can use the Series.sum() method to return the sum of the values in a column.
Store the resulting float as low_wage_percent, and display the value with the print() function.
'''
low_wage_percent = recent_grads["Low_wage_jobs"].sum()/recent_grads["Total"].sum()

#6: Comparing Data Sets
'''Use a for loop to iterate over majors.
For each major, use Boolean filtering to find the corresponding row in both DataFrames.
Compare the values for Unemployment_rate to see which DataFrame has a lower value.
Increment rg_lower_count if the value for Unemployment_rate is lower for recent_grads than it is for all_ages.
Display rg_lower_count with the print() function.
'''
# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0
for major in majors:
    recent_grads_row = recent_grads[recent_grads['Major'] == major]
    all_ages_row = all_ages[all_ages["Major"] == major]
    rg_uemp = recent_grads_row["Unemployment_rate"].values[0]
    aa_uemp = all_ages_row["Unemployment_rate"].values[0]
    
    if rg_uemp < aa_uemp:
        rg_lower_count +=1 
    
print(rg_lower_count)
