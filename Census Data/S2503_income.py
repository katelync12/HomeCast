
import requests
import pandas as pd
import openpyxl

# 2016 and before it uses percentages not estimates

places = [
    {"name": "Chicago", "code": "1600000US1714000"},
    {"name": "Houston", "code": "1600000US4835000"},
    {"name": "Los Angeles", "code": "1600000US0644000"},
    {"name": "New York", "code": "1600000US3651000"},
    {"name": "Phoenix", "code": "1600000US0455000"},
]

dfs = []
for place in places:
    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2021, 2022, 2023]
    rename_dict = {
        'S2503_C01_001E': 'Total Households',
        'S2503_C01_002E': 'Less than $5,000',
        'S2503_C01_003E': '$5,000 to $9,999',
        'S2503_C01_004E': '$10,000 to $14,999',
        'S2503_C01_005E': '$15,000 to $19,999',
        'S2503_C01_006E': '$20,000 to $24,999',  
        'S2503_C01_007E': '$25,000 to $34,999',
        'S2503_C01_008E': '$35,000 to $49,999',
        'S2503_C01_009E': '$50,000 to $74,999',
        'S2503_C01_010E': '$75,000 to $99,999',
        'S2503_C01_011E': '$100,000 to $149,999',
        'S2503_C01_012E': '$150,000 +',
        'S2503_C01_013E': 'Median Household Income',
    }
    for year in years:
        url = f"https://api.census.gov/data/{year}/acs/acs1/subject?get=group(S2503)&ucgid={place['code']}&key=183f61b90d9d1c762883d948079890009c6d3d34"
        response = requests.get(url)
        print(response)
        data = response.json()
        df = pd.DataFrame(data[1:], columns=data[0])
        city_df_race = df[['S2503_C01_001E','S2503_C01_002E', 'S2503_C01_003E', 'S2503_C01_004E', 'S2503_C01_005E', 'S2503_C01_006E', 'S2503_C01_007E', 'S2503_C01_008E', 'S2503_C01_009E', 'S2503_C01_010E', 'S2503_C01_011E', 'S2503_C01_012E', 'S2503_C01_013E', ]]
        city_df_race = city_df_race.rename(columns=rename_dict)
        city_df_race['Year'] = year
        city_df_race['City'] = place['name']
        dfs.append(city_df_race)

    # 2020 Configuration
    url = f"https://api.census.gov/data/2020/acs/acs5/subject?get=group(S2503)&ucgid={place['code']}&key=183f61b90d9d1c762883d948079890009c6d3d34"
    response = requests.get(url)
    data = response.json()
    print(response)
    df = pd.DataFrame(data[1:], columns=data[0])
    city_df_race = df[['S2503_C01_001E','S2503_C01_002E', 'S2503_C01_003E', 'S2503_C01_004E', 'S2503_C01_005E', 'S2503_C01_006E', 'S2503_C01_007E', 'S2503_C01_008E', 'S2503_C01_009E', 'S2503_C01_010E', 'S2503_C01_011E', 'S2503_C01_012E', 'S2503_C01_013E', ]]
    city_df_race = city_df_race.rename(columns=rename_dict)
    city_df_race['Year'] = 2020
    city_df_race['City'] = place['name']
    if year in [2010, 2011, 2012, 2013, 2014, 2015, 2016]:
        for key, value in rename_dict.items():
            if key != 'S2503_C01_001E' and key != 'S2503_C01_013E':
                city_df_race[value] = (city_df_race['Total Households'].astype(int) * (city_df_race[value].astype(float) / 100)).astype(int)
    dfs.append(city_df_race)

final_df = pd.concat(dfs, ignore_index=True)
final_df.to_excel('income_data.xlsx', index=False)