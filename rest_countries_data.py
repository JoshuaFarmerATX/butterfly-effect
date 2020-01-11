import requests
import pandas as pd
import json
import pprint
import matplotlib as plt

def get_rest_countries():
    r = requests.get("https://restcountries.eu/rest/v2/all")
    raw_data = r.json()

    def extract_block(field_name, d):
        try:
            return d[field_name][0]["name"]
        except:
            pass


    return pd.DataFrame([{
        "Country": d["name"],
        "Alpha3 Code": d['alpha3Code'],
        "Capital": d['capital'],
        "Region": d['region'],
        "Sub-Region": d['subregion'],
        "Population": d['population'],
        "Lat and Lon": d['latlng'],
        "Area": d['area'],
        "Timezone": d['timezones'][0],
        "borders": d['borders'],
        "Currencies": extract_block('currencies', d),
        "Regional Bloc": extract_block('regionalBlocs', d)
        } for d in raw_data])

df = get_rest_countries()
print(df.head())
print(len(df['Country']))