import requests
import pandas as pd
import openpyxl

# 2017 and before it does not have combined data like "High School or Higher" or "Bachelor's Degree or Higher"

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
        'DP02_0059E': 'Population 25+',
        'DP02_0060E': 'Less than 9th Grade',
        'DP02_0061E': '9-12th Grade, No Diploma',
        'DP02_0062E': 'High School Graduate',
        'DP02_0063E': 'Some College, No Degree',
        'DP02_0064E': "Associate's Degree",
        'DP02_0065E': "Bachelor's Degree",
        'DP02_0066E': "Graduate or Professional Degree",
        'DP02_0067E': 'High School or Higher',
        'DP02_0068E': 'Bachelor\'s Degree or Higher',
    }
    rename_dict_2018 = {
        'DP02_0058E': 'Population 25+',
        'DP02_0059E': 'Less than 9th Grade',
        'DP02_0060E': '9-12th Grade, No Diploma',
        'DP02_0061E': 'High School Graduate',
        'DP02_0062E': 'Some College, No Degree',
        'DP02_0063E': "Associate's Degree",
        'DP02_0064E': "Bachelor's Degree",
        'DP02_0065E': "Graduate or Professional Degree",
        'DP02_0066E': 'High School or Higher',
        'DP02_0067E': 'Bachelor\'s Degree or Higher',
    }
    for year in years:
        if year == 2020:
            url = f"https://api.census.gov/data/2020/acs/acs5/profile?get=group(DP02)&ucgid={place['code']}&key=183f61b90d9d1c762883d948079890009c6d3d34"
        else:
            url = f"https://api.census.gov/data/{year}/acs/acs1/profile?get=group(DP02)&ucgid={place['code']}&key=183f61b90d9d1c762883d948079890009c6d3d34"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data[1:], columns=data[0])
        if year in [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]:
            city_df_race = df[['DP02_0058E', 'DP02_0059E', 'DP02_0060E', 'DP02_0061E', 'DP02_0062E', 'DP02_0063E', 'DP02_0064E', 'DP02_0065E', 'DP02_0066E', 'DP02_0067E']]
            city_df_race = city_df_race.rename(columns=rename_dict_2018)
        else:
            city_df_race = df[['DP02_0059E', 'DP02_0060E', 'DP02_0061E', 'DP02_0062E', 'DP02_0063E', 'DP02_0064E', 'DP02_0065E', 'DP02_0066E', 'DP02_0067E', 'DP02_0068E']]
            city_df_race = city_df_race.rename(columns=rename_dict)
        city_df_race['Year'] = year
        city_df_race['City'] = place['name']
        dfs.append(city_df_race)

final_df = pd.concat(dfs, ignore_index=True)
final_df.to_excel('education_data.xlsx', index=False)