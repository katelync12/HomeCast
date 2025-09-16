import pandas as pd
import matplotlib.pyplot as plt

age_df = pd.read_excel('age_data.xlsx')
education_df = pd.read_excel('education_data.xlsx')
race_df = pd.read_excel('race_data.xlsx')
income_df = pd.read_excel('income_data.xlsx')

age_df = age_df.sort_values(by=['City', 'Year'])
education_df = education_df.sort_values(by=['City', 'Year'])
race_df = race_df.sort_values(by=['City', 'Year'])
income_df = income_df.sort_values(by=['City', 'Year'])

age_df_normalized = age_df.copy()
age_columns = [col for col in age_df.columns if col not in ['City', 'Year', 'Total Population']]
for col in age_columns:
    age_df_normalized[col] = age_df[col] / age_df['Total Population']

education_df_normalized = education_df.copy()
education_columns = [col for col in education_df.columns if col not in ['City', 'Year', 'Population 25+']]
for col in education_columns:   
    education_df_normalized[col] = education_df[col] / education_df['Population 25+']

income_df_normalized = income_df.copy()
income_columns = [col for col in income_df.columns if col not in ['City', 'Year', 'Total Households', 'Median Household Income']]
for col in income_columns:
    income_df_normalized[col] = income_df[col] / income_df['Total Households']

race_df_normalized = race_df.copy()
race_columns = [col for col in race_df.columns if col not in ['City', 'Year', 'Total Population']]
for col in race_columns:
    race_df_normalized[col] = race_df[col] / race_df['Total Population']

plt.figure(figsize=(12, 6))

for city in race_df['City'].unique():
    city_data = race_df_normalized[race_df_normalized['City'] == city]
    plt.plot(city_data['Year'], city_data['Total Population'], marker='o', label=city)

plt.title('Bachelor\'s Degree Holders Over Time by City')
plt.xlabel('Year')
plt.ylabel('Proportion of Population')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
plt.tight_layout()
plt.savefig('population_distribution_all_cities.png')
plt.close()