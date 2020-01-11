# import requests
# import pandas as pd
# import json
# import pprint
# import matplotlib as plt
# import numpy as np

def get_rest_countries():
    r = requests.get("https://restcountries.eu/rest/v2/all")
    raw_data = r.json()

    def extract_block(field_name, d):
        try:
            return d[field_name][0]["name"]
        except:
            pass

    def get_lat_lon(int, d):
        try:
            return d['latlng'][int]
        except:
            pass

    return pd.DataFrame([{
        "Country": d["name"],
        "Alpha3 Code": d['alpha3Code'],
        "Capital": d['capital'],
        "Region": d['region'],
        "Sub-Region": d['subregion'],
        "Population": d['population'],
        "Latitutde": get_lat_lon(0,d),
        "Longitude": get_lat_lon(1,d),
        "Area": d['area'],
        "Timezone": d['timezones'][0],
        "borders": d['borders'],
        "Currencies": extract_block('currencies', d),
        "Regional Bloc": extract_block('regionalBlocs', d)
        } for d in raw_data])

def get_cia_data():
    with open('factbook.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    data_list = []
    data_list = []
    for country_name in data["countries"].keys():
        country_data = data["countries"][country_name]["data"]

        try:
            name = country_data["name"]
        except:
            name = np.nan

        try:
            government_type = country_data["government"]["government_type"]
        except:
            government_type = np.nan

        try:
            population = country_data["people"]["population"]["total"]
        except:
            population = np.nan

        try:
            internet_users = country_data["communications"]["internet"]["users"]["total"]
        except:
            internet_users = np.nan   

        try:
            internet_users_percent = country_data["communications"]["internet"]["users"]["percent_of_population"]
        except:
            internet_users_percent = np.nan     

        try:
            internet_users_rank = country_data["communications"]["internet"]["users"]["global_rank"]
        except:
            internet_users_rank = np.nan     

        try:
            telephones_fixed = country_data["communications"]["telephones"]["fixed_lines"]["total_subscriptions"]
        except:
            telephones_fixed = np.nan    

        try:
            telephones_fixed_rank = country_data["communications"]["telephones"]["fixed_lines"]["global_rank"]
        except:
            telephones_fixed_rank = np.nan 

        try:
            telephones_mobile = country_data["communications"]["telephones"]["mobile_cellular"]["total_subscriptions"]
        except:
            telephones_mobile = np.nan    

        try:
            telephones_mobile_rank = country_data["communications"]["telephones"]["mobile_cellular"]["global_rank"]
        except:
            telephones_mobile_rank = np.nan 

        try:
            median_age = country_data["people"]["median_age"]["total"]["value"]
        except:
            median_age = np.nan

        try:
            gdp_purchasing = ((country_data["economy"]['gdp']["purchasing_power_parity"]["annual_values"])[0])["value"]
        except:
            gdp_purchasing = np.nan

        try:
            gdp_rank = country_data["economy"]['gdp']["purchasing_power_parity"]["global_rank"]
        except:
            gdp_rank = np.nan

        try:
            education_expen = country_data["people"]["education_expenditures"]["percent_of_gdp"]
        except:
            education_expen = np.nan

        try:
            education_rank = country_data["people"]["education_expenditures"]["global_rank"]
        except:
            education_rank = np.nan

        data_list.append({
            "Country": name,
            "Government Type": government_type,
            "Population": population,
            "Internet Users": internet_users,
            "Internet % of Population": internet_users_percent,
            "Internet Global Rank": internet_users_rank,
            "Telephones Fixed Lines": telephones_fixed,
            "Telephones Fixed Lines Global Rank": telephones_fixed_rank,
            "Telephone Mobile Cellular": telephones_mobile,
            "Telephone Mobile Cellular Global Rank": telephones_mobile_rank,
            "Median_age": median_age,
            "GDP - Purchasing power parity": gdp_purchasing,
            "GDP - Global Rank": gdp_rank,
            "Education Expenditures": education_expen,
            "Education Expeditures - Global Rank": education_rank,


        })
        
    return pd.DataFrame(data_list)
