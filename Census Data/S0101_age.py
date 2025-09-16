import requests
import pandas as pd
import openpyxl

# 2016 and before it does the same percentage thing\
# TODO: Please rerun this to get median age into table

places = [
    {"name": "Chicago", "code": "1600000US1714000"},
    {"name": "Houston", "code": "1600000US4835000"},
    {"name": "Los Angeles", "code": "1600000US0644000"},
    {"name": "New York", "code": "1600000US3651000"},
    {"name": "Phoenix", "code": "1600000US0455000"},
]

dfs = []
for place in places:
    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    rename_dict = {
        'S0101_C01_001E': 'Total Population',
        'S0101_C01_002E': 'Under 5 years',
        'S0101_C01_003E': '5 to 9 years',
        'S0101_C01_004E': '10 to 14 years',
        'S0101_C01_005E': '15 to 19 years',
        'S0101_C01_006E': '20 to 24 years',
        'S0101_C01_007E': '25 to 29 years',
        'S0101_C01_008E': '30 to 34 years',
        'S0101_C01_009E': '35 to 39 years',
        'S0101_C01_010E': '40 to 44 years',
        'S0101_C01_011E': '45 to 49 years',
        'S0101_C01_012E': '50 to 54 years',
        'S0101_C01_013E': '55 to 59 years',
        'S0101_C01_014E': '60 to 64 years',
        'S0101_C01_015E': '65 to 69 years',
        'S0101_C01_016E': '70 to 74 years',
        'S0101_C01_017E': '75 to 79 years',
        'S0101_C01_018E': '80 to 84 years',
        'S0101_C01_019E': '85 years and over',
    }
    for year in years:
        if year == 2020:
            url = f"https://api.census.gov/data/2020/acs/acs5/subject?get=group(S0101)&ucgid={place['code']}&key=183f61b90d9d1c762883d948079890009c6d3d34"
        else:
            url = f"https://api.census.gov/data/{year}/acs/acs1/subject?get=group(S0101)&ucgid={place['code']}&key=183f61b90d9d1c762883d948079890009c6d3d34"
        response = requests.get(url)
        data = response.json()
        print(response)
        df = pd.DataFrame(data[1:], columns=data[0])
        city_df_race = df[['S0101_C01_001E', 'S0101_C01_002E', 'S0101_C01_003E', 'S0101_C01_004E', 'S0101_C01_005E', 'S0101_C01_006E', 'S0101_C01_007E', 'S0101_C01_008E', 'S0101_C01_009E', 'S0101_C01_010E', 'S0101_C01_011E', 'S0101_C01_012E', 'S0101_C01_013E', 'S0101_C01_014E', 'S0101_C01_015E', 'S0101_C01_016E', 'S0101_C01_017E', 'S0101_C01_018E', 'S0101_C01_019E', 'S0101_C01_030E', 'S0101_C01_032E']]
        if year in [2010, 2011, 2012, 2013, 2014, 2015, 2016]:
            city_df_race['Median Age'] = city_df_race['S0101_C01_030E']
        else:
            city_df_race['Median Age'] = city_df_race['S0101_C01_032E']
        city_df_race = city_df_race.rename(columns=rename_dict)
        city_df_race['Year'] = year
        city_df_race['City'] = place['name']
        if year in [2010, 2011, 2012, 2013, 2014, 2015, 2016]:
            for key, value in rename_dict.items():
                if key != 'S0101_C01_001E' and key != 'S0101_C01_030E':
                    city_df_race[value] = (city_df_race['Total Population'].astype(int) * (city_df_race[value].astype(float) / 100)).astype(int)
        city_df_race.drop(columns=['S0101_C01_030E', 'S0101_C01_032E'], inplace=True, errors='ignore')
        dfs.append(city_df_race)

final_df = pd.concat(dfs, ignore_index=True)
print(final_df)
final_df.to_excel('age_data.xlsx', index=False)