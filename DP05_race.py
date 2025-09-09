
import requests
import pandas as pd
import openpyxl

places = [
    {"name": "Chicago", "code": "1600000US1714000"},
    {"name": "Houston", "code": "1600000US4835000"},
    {"name": "Los Angeles", "code": "1600000US0644000"},
    {"name": "New York", "code": "1600000US3651000"},
    {"name": "Phoenix", "code": "1600000US0455000"},
]

dfs = []
for place in places:
    # 2023 Configuration
    rename_dict = {
        'DP05_0075E': 'Total Population',
        'DP05_0076E': 'Total Hispanic or Latino',
        'DP05_0082E': 'Total White alone',
        'DP05_0083E': 'Total Black alone',
        'DP05_0084E': 'Total American Indian / Alaskan Native alone',
        'DP05_0085E': 'Total Asian alone',
        'DP05_0086E': 'Total Native Hawaiian and Other Pacific Islander alone',
        'DP05_0087E': 'Total Other alone',
    }
    url = f"https://api.census.gov/data/2023/acs/acs1/profile?get=group(DP05)&ucgid={place['code']}&key=183f61b90d9d1c762883d948079890009c6d3d34"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data[1:], columns=data[0])
    city_df_race = df[['DP05_0075E', 'DP05_0076E', 'DP05_0082E', 'DP05_0083E', 'DP05_0084E', 'DP05_0085E', 'DP05_0086E', 'DP05_0087E']]
    city_df_race = city_df_race.rename(columns=rename_dict)
    city_df_race['Year'] = 2023
    city_df_race['City'] = place['name']
    dfs.append(city_df_race)

    # 2022 Configuration
    rename_dict = {
        'DP05_0072E': 'Total Population',
        'DP05_0073E': 'Total Hispanic or Latino',
        'DP05_0079E': 'Total White alone',
        'DP05_0080E': 'Total Black alone',
        'DP05_0081E': 'Total American Indian / Alaskan Native alone',
        'DP05_0082E': 'Total Asian alone',
        'DP05_0083E': 'Total Native Hawaiian and Other Pacific Islander alone',
        'DP05_0084E': 'Total Other alone',
    }
    url = f"https://api.census.gov/data/2022/acs/acs1/profile?get=group(DP05)&ucgid={place['code']}&key=183f61b90d9d1c762883d948079890009c6d3d34"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data[1:], columns=data[0])
    city_df_race = df[['DP05_0072E', 'DP05_0073E', 'DP05_0079E', 'DP05_0080E', 'DP05_0081E', 'DP05_0082E', 'DP05_0083E', 'DP05_0084E']]
    city_df_race = city_df_race.rename(columns=rename_dict)
    city_df_race['Year'] = 2022
    city_df_race['City'] = place['name']
    dfs.append(city_df_race)

    # 2021 Configuration
    rename_dict = {
        'DP05_0070E': 'Total Population',
        'DP05_0071E': 'Total Hispanic or Latino',
        'DP05_0077E': 'Total White alone',
        'DP05_0078E': 'Total Black alone',
        'DP05_0079E': 'Total American Indian / Alaskan Native alone',
        'DP05_0080E': 'Total Asian alone',
        'DP05_0081E': 'Total Native Hawaiian and Other Pacific Islander alone',
        'DP05_0082E': 'Total Other alone',
    }
    url = f"https://api.census.gov/data/2021/acs/acs1/profile?get=group(DP05)&ucgid={place['code']}&key=183f61b90d9d1c762883d948079890009c6d3d34"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data[1:], columns=data[0])
    city_df_race = df[['DP05_0070E', 'DP05_0071E', 'DP05_0077E', 'DP05_0078E', 'DP05_0079E', 'DP05_0080E', 'DP05_0081E', 'DP05_0082E']]
    city_df_race = city_df_race.rename(columns=rename_dict)
    city_df_race['Year'] = 2021
    city_df_race['City'] = place['name']
    dfs.append(city_df_race)

    # 2020 Configuration
    rename_dict = {
        'DP05_0070E': 'Total Population',
        'DP05_0071E': 'Total Hispanic or Latino',
        'DP05_0077E': 'Total White alone',
        'DP05_0078E': 'Total Black alone',
        'DP05_0079E': 'Total American Indian / Alaskan Native alone',
        'DP05_0080E': 'Total Asian alone',
        'DP05_0081E': 'Total Native Hawaiian and Other Pacific Islander alone',
        'DP05_0082E': 'Total Other alone',
    }
    url = f"https://api.census.gov/data/2020/acs/acs5/profile?get=group(DP05)&ucgid={place['code']}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data[1:], columns=data[0])
    city_df_race = df[['DP05_0070E', 'DP05_0071E', 'DP05_0077E', 'DP05_0078E', 'DP05_0079E', 'DP05_0080E', 'DP05_0081E', 'DP05_0082E']]
    city_df_race = city_df_race.rename(columns=rename_dict)
    city_df_race['Year'] = 2020
    city_df_race['City'] = place['name']
    dfs.append(city_df_race)

    # 2017-2019 Section
    years = [2017, 2018, 2019]
    rename_dict = {
        'DP05_0070E': 'Total Population',
        'DP05_0071E': 'Total Hispanic or Latino',
        'DP05_0077E': 'Total White alone',
        'DP05_0078E': 'Total Black alone',
        'DP05_0079E': 'Total American Indian / Alaskan Native alone',
        'DP05_0080E': 'Total Asian alone',
        'DP05_0081E': 'Total Native Hawaiian and Other Pacific Islander alone',
        'DP05_0082E': 'Total Other alone',
    }
    for year in years:
        url = f"https://api.census.gov/data/{year}/acs/acs1/profile?get=group(DP05)&ucgid={place['code']}&key=183f61b90d9d1c762883d948079890009c6d3d34"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data[1:], columns=data[0])
        city_df_race = df[['DP05_0070E', 'DP05_0071E', 'DP05_0077E', 'DP05_0078E', 'DP05_0079E', 'DP05_0080E', 'DP05_0081E', 'DP05_0082E']]
        city_df_race = city_df_race.rename(columns=rename_dict)
        city_df_race['Year'] = year
        city_df_race['City'] = place['name']
        dfs.append(city_df_race)

    # 2010-2016 Section
    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016]
    rename_dict = {
        'DP05_0065E': 'Total Population',
        'DP05_0066E': 'Total Hispanic or Latino',
        'DP05_0072E': 'Total White alone',
        'DP05_0073E': 'Total Black alone',
        'DP05_0074E': 'Total American Indian / Alaskan Native alone',
        'DP05_0075E': 'Total Asian alone',
        'DP05_0076E': 'Total Native Hawaiian and Other Pacific Islander alone',
        'DP05_0077E': 'Total Other alone',
    }
    for year in years:
        url = f"https://api.census.gov/data/{year}/acs/acs1/profile?get=group(DP05)&ucgid={place['code']}&key=183f61b90d9d1c762883d948079890009c6d3d34"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data[1:], columns=data[0])
        city_df_race = df[['DP05_0065E', 'DP05_0066E', 'DP05_0072E', 'DP05_0073E', 'DP05_0074E', 'DP05_0075E', 'DP05_0076E', 'DP05_0077E']]
        city_df_race = city_df_race.rename(columns=rename_dict)
        city_df_race['Year'] = year
        city_df_race['City'] = place['name']
        dfs.append(city_df_race)

final_df = pd.concat(dfs, ignore_index=True)
final_df.to_excel('race_data.xlsx', index=False)