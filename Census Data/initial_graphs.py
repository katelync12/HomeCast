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

plt.figure(figsize=(12, 6))

for city in income_df['City'].unique():
    city_data = income_df[income_df['City'] == city]
    plt.plot(city_data['Year'], city_data['Median Household Income'], marker='o', label=city)

plt.title('Median Household Income Over Time by City')
plt.xlabel('Year')
plt.ylabel('Median Household Income')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()
plt.tight_layout()
plt.savefig('income_distribution_all_cities.png')
plt.close()