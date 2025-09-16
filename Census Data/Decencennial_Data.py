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

#Age Section
url = "https://api.census.gov/data/2000/dec/sf4profile?get=group(DP1)&ucgid=1600000US1714000"

years = [2000]

rename_dict = {
    'DP1_C0': 'Total Population',
    'DP1_C6': 'Under 5 years',
    'DP1_C8': '5 to 9 years', 
    'DP1_C10': '10 to 14 years',
    'DP1_C12': '15 to 19 years',
    'DP1_C14': '20 to 24 years',
    'DP1_C16': '25 to 34 years',
    'DP1_C18': '35 to 44 years',
    'DP1_C20': '45 to 54 years',
    'DP1_C22': '55 to 59 years',
    'DP1_C24': '60 to 64 years',
    'DP1_C26': '65 to 74 years',
    'DP1_C28': '75 to 84 years',
    'DP1_C30': '85 years and over',
    'DP1_C32': 'Median Age',
}

dfs = []
for place in places:
    url = f"https://api.census.gov/data/2000/dec/sf4profile?get=group(DP1)&ucgid={place['code']}&key=183f61b90d9d1c762883d948079890009c6d3d34"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data[1:], columns=data[0])
    specific_columns = df[['DP1_C0', 'DP1_C6', 'DP1_C8', 'DP1_C10', 'DP1_C12', 'DP1_C14', 'DP1_C16', 'DP1_C18', 'DP1_C20', 'DP1_C22', 'DP1_C24', 'DP1_C26', 'DP1_C28', 'DP1_C30', 'DP1_C32']]
    specific_columns = specific_columns.head(1)
    specific_columns['Year'] = 2020
    specific_columns['City'] = place['name']
    specific_columns = specific_columns.rename(columns=rename_dict)
    dfs.append(specific_columns)

renamme_dict_edu = {
    'DP2_C12': 'Total 25+ Population',
    'DP2_C14': 'Less than 9th Grade',
    'DP2_C16': '9-12th Grade, No Diploma',
    'DP2_C18': 'High School Graduate',
    'DP2_C20': 'Some College, No Degree',
    'DP2_C22': "Associate's Degree",
    'DP2_C24': "Bachelor's Degree",
    'DP2_C26': "Graduate or Professional Degree",
}
for place in places:
    url = f"https://api.census.gov/data/2000/dec/sf4profile?get=group(DP2)&ucgid={place['code']}&key=183f61b90d9d1c762883d948079890009c6d3d34"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data[1:], columns=data[0])
    specific_columns = df[['DP2_C12', 'DP2_C14', 'DP2_C16', 'DP2_C18', 'DP2_C20', 'DP2_C22', 'DP2_C24', 'DP2_C26']]
    specific_columns = specific_columns.head(1)
    specific_columns['Year'] = 2020
    specific_columns['City'] = place['name']
    dfs.append(specific_columns)

url = "https://api.census.gov/data/2000/dec/sf4profile?get=group(DP3)&ucgid=1600000US1714000"

income_rename_dict = {
    'DP3_C90': 'Total Households',
    'DP3_C92': 'Less than $10,000',
    'DP3_C94': '$10,000 to $14,999',
    'DP3_C96': '$15,000 to $24,999',
    'DP3_C98': '$25,000 to $34,999',
    'DP3_C100': '$35,000 to $49,999',
    'DP3_C102': '$50,000 to $74,999',
    'DP3_C104': '$75,000 to $99,999',
    'DP3_C106': '$100,000 to $149,999',
    'DP3_C108': '$150,000 to $199,999',
    'DP3_C110': '$200,000 or more',
    'DP3_C112': 'Median Household Income',
}
for place in places:
    url = f"https://api.census.gov/data/2000/dec/sf4profile?get=group(DP3)&ucgid={place['code']}&key=183f61b90d9d1c762883d948079890009c6d3d34"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data[1:], columns=data[0])
    specific_columns = df[['DP3_C90', 'DP3_C92', 'DP3_C94', 'DP3_C96', 'DP3_C98', 'DP3_C100', 'DP3_C102', 'DP3_C104', 'DP3_C106', 'DP3_C108', 'DP3_C110', 'DP3_C112']]
    specific_columns = specific_columns.head(1)
    specific_columns['Year'] = 2020
    specific_columns['City'] = place['name']
    specific_columns = specific_columns.rename(columns=income_rename_dict)
    dfs.append(specific_columns)


race_rename_dict = {
    'H010001': 'Total Population',
    'H010003': 'White Alone',
    'H010004': 'Black or African American Alone',
    'H010005': 'American Indian and Alaska Native Alone',
    'H010006': 'Asian Alone',
    'H010007': 'Native Hawaiian and Other Pacific Islander Alone',
    'H010008': 'Some Other Race Alone',
    'H010010': 'Hispanic or Latino',
}
for place in places:
    url = f"https://api.census.gov/data/2000/dec/sf3?get=group(H010)&ucgid={place['code']}&key=183f61b90d9d1c762883d948079890009c6d3d34"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data[1:], columns=data[0])
    specific_columns = df[['H010001', 'H010003', 'H010004', 'H010005', 'H010006', 'H010007', 'H010008', 'H010010']]
    specific_columns = specific_columns.head(1)
    specific_columns['Year'] = 2020
    specific_columns['City'] = place['name']
    specific_columns = specific_columns.rename(columns=race_rename_dict)
    dfs.append(specific_columns)

final_df = pd.concat(dfs, ignore_index=True)
final_df.to_excel('2000_data.xlsx', index=False)