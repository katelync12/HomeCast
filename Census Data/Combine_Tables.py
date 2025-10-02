import pandas as pd
# import openpyxl

# df = pd.read_excel('income_data.xlsx', sheet_name='Sheet1')

# df_less = df[['Median Household Income', 'City', 'Year', 'Total Households']]

# def expand_to_quarters(row_1, row_2):
#     median_1 = int(row_1['Median Household Income'])
#     median_2 = int(row_2['Median Household Income'])

#     if median_1 == 0 or median_2 == 0:
#         return pd.DataFrame()  # Avoid division by zero

#     slope = (median_2 - median_1) / 4
#     quarter_incomes = [int(median_1 + slope * (i + 1)) for i in range(4)]
    
#     quarters = [f"{i+1}" for i in range(4)]
    
#     data = {
#         'Median Household Income': quarter_incomes,
#         'City': [row_1['City']] * 4,
#         'Year': [f"{row_1['Year']}"] * 4,
#         'Quarter': quarters
#     }
    
#     return pd.DataFrame(data)
# df_new = []
# for i in range(len(df_less) - 1):
#     expanded = expand_to_quarters(df_less.iloc[i], df_less.iloc[i + 1])
#     if (df_less.iloc[i]['City'] != df_less.iloc[i + 1]['City']):
#         continue  # Skip if not the same city
#     if not expanded.empty:
#         df_new.append(expanded)
# df_new = pd.concat(df_new, ignore_index=True)
# df_new = df_new.sort_values(by=['City', 'Year', 'Quarter']).reset_index(drop=True)
# #df_new.to_excel('expanded_income_data.xlsx', index=False)

# data = {
#     'Median Household Income': [38909, 26301, 28327, 40328, 45600, 38293, 37625, 41207, 36616, 36687],
#     'City': ['New York', 'Chicago', 'Phoenix', 'Houston', 'Los Angeles', 'New York', 'Chicago', 'Phoenix', 'Houston', 'Los Angeles'],
#     'Year': ['1990', '1990', '1990', '1990', '1990', '2000', '2000', '2000', '2000', '2000'],
# }

# df = pd.DataFrame(data)

# df['Date'] = pd.to_datetime(df['Year']) + pd.offsets.QuarterEnd(1)

# # Step 3: Set up new full date range (1990Q1 to 2009Q4)
# quarters = pd.date_range(start='1990-03-31', end='2009-12-31', freq='Q')

# # Step 4: Create a multi-index of all City-Quarter combinations
# cities = df['City'].unique()
# multi_index = pd.MultiIndex.from_product([cities, quarters], names=['City', 'Date'])

# # Step 5: Reindex the original DataFrame
# df = df.set_index(['City', 'Date'])
# df = df.reindex(multi_index)

# # Step 6: Interpolate missing values by linear method
# df['Median Household Income'] = df['Median Household Income'].interpolate(method='linear')

# # Optional: Reset index to flatten the DataFrame
# df = df.reset_index()

# # Display final result
# df.to_excel('interpolated_income_data.xlsx', index=False)



quarter_age = pd.read_excel('less_age_data.xlsx', sheet_name='Sheet1')

def expand_to_quarters_age(row_1, row_2):
    median_1 = int(row_1['Total Population'])
    median_2 = int(row_2['Total Population'])

    if median_1 == 0 or median_2 == 0:
        return pd.DataFrame()  # Avoid division by zero

    slope = (median_2 - median_1) / 4
    quarter_incomes = [int(median_1 + slope * (i + 1)) for i in range(4)]
    
    quarters = [f"{i+1}" for i in range(4)]
    
    data = {
        'Total Population': quarter_incomes,
        'City': [row_1['City']] * 4,
        'Year': [f"{row_1['Year']}"] * 4,
        'Quarter': quarters
    }
    
    return pd.DataFrame(data)
df_new_age = []
quarter_age = quarter_age.sort_values(by=['City', 'Year']).reset_index(drop=True)
for i in range(len(quarter_age) - 1):
    if (quarter_age.iloc[i]['City'] != quarter_age.iloc[i + 1]['City']):
        continue  # Skip if not the same city
    expanded = expand_to_quarters_age(quarter_age.iloc[i], quarter_age.iloc[i + 1])
    if not expanded.empty:
        df_new_age.append(expanded)

df_new_age = pd.concat(df_new_age, ignore_index=True)
df_new_age = df_new_age.sort_values(by=['City', 'Year', 'Quarter']).reset_index(drop=True)
df_new_age.to_excel('expanded_age_data.xlsx', index=False)


df_income_combined = pd.read_excel('interpolated_income_data.xlsx', sheet_name='Sheet1')
df_income_combined_2 = pd.read_excel('expanded_income_data.xlsx', sheet_name='Sheet1')

combined_income = pd.concat([df_income_combined, df_income_combined_2]).drop_duplicates().reset_index(drop=True)
combined_income = combined_income.drop(columns=['Date'])

total_age = pd.read_excel('expanded_age_data.xlsx', sheet_name='Sheet1')

final_combined = pd.merge(combined_income, total_age, on=['City', 'Year', 'Quarter'], how='inner')
final_combined = final_combined.sort_values(by=['City', 'Year', 'Quarter']).reset_index(drop=True)
final_combined.to_excel('final_combined_data.xlsx', index=False)
