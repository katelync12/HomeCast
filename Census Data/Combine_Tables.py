import pandas as pd
import numpy as np

df_income = pd.read_excel('income_data.xlsx', sheet_name='Sheet1')
df_age_before = pd.read_excel('less_age_data.xlsx', sheet_name='Sheet1')

df_less_income = df_income[['Median Household Income', 'City', 'Year']]

data = {
    'Median Household Income': [38909, 26301, 28327, 40328, 45600, 38293, 37625, 41207, 36616, 36687],
    'City': ['New York', 'Chicago', 'Phoenix', 'Houston', 'Los Angeles', 'New York', 'Chicago', 'Phoenix', 'Houston', 'Los Angeles'],
    'Year': [1990, 1990, 1990, 1990, 1990, 2000, 2000, 2000, 2000, 2000],
}

df_income_before = pd.DataFrame(data)

df_income_combined = pd.concat([df_less_income, df_income_before], axis=0)



df_income_combined = df_income_combined.sort_values(by=['City', 'Year']).reset_index(drop=True)
df_income_combined['Date'] = pd.to_datetime(df_income_combined['Year'], format='%Y') + pd.offsets.QuarterEnd(4)

quarters = pd.date_range(start='1990-03-31', end='2022-12-31', freq='Q')

median_income_quarterly = []

for city, group in df_income_combined.groupby('City'):
    city_df = group.set_index('Date').sort_index()
    city_quarterly = pd.DataFrame(index=quarters)
    city_quarterly = city_quarterly.join(city_df['Median Household Income'], how='left')
    city_quarterly['Median Household Income'] = city_quarterly['Median Household Income'].interpolate(method='linear')
    city_quarterly['Median Household Income'] = city_quarterly['Median Household Income'].ffill().bfill()
    city_quarterly['City'] = city
    median_income_quarterly.append(city_quarterly)

df_income_combined = pd.concat(median_income_quarterly).reset_index().rename(columns={'index': 'Date'})
df_income_combined['Year'] = df_income_combined['Date'].dt.year
df_income_combined['Quarter'] = df_income_combined['Date'].dt.quarter
df_income_combined = df_income_combined[['Median Household Income', 'City', 'Year', 'Quarter']]


# Population Section

age_data_combined = df_age_before.sort_values(by=['City', 'Year']).reset_index(drop=True)
age_data_combined['Date'] = pd.to_datetime(age_data_combined['Year'], format='%Y') + pd.offsets.QuarterEnd(4)
print(age_data_combined)

median_age_quarterly = []
for city, group in age_data_combined.groupby('City'):
    city_df = group.set_index('Date').sort_index()
    city_quarterly = pd.DataFrame(index=quarters)
    city_quarterly = city_quarterly.join(city_df['Total Population'], how='left')
    city_quarterly['Total Population'] = city_quarterly['Total Population'].interpolate(method='linear')
    city_quarterly['Total Population'] = city_quarterly['Total Population'].ffill().bfill()
    city_quarterly['City'] = city
    median_age_quarterly.append(city_quarterly)


df_age_combined = pd.concat(median_age_quarterly).reset_index().rename(columns={'index': 'Date'})
print(df_age_combined)
df_age_combined['Year'] = df_age_combined['Date'].dt.year
df_age_combined['Quarter'] = df_age_combined['Date'].dt.quarter
df_age_combined = df_age_combined[['Total Population', 'City', 'Year', 'Quarter']]

# Merging Section
final_combined = pd.merge(df_income_combined, df_age_combined, on=['City', 'Year', 'Quarter'], how='inner')
final_combined = final_combined.sort_values(by=['City', 'Year', 'Quarter']).reset_index(drop=True)
final_combined.to_excel('final_combined_data.xlsx', index=False)