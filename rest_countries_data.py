import requests
import pandas as pd
import json
import pprint
import matplotlib as plt

r = requests.get("https://restcountries.eu/rest/v2/all")
raw_data = r.json()
# pprint.pprint(raw_data)

# df = pd.DataFrame([{
#     "City": d["name"]
# } for ])

def extract_block(field_name, d):
    try:
        return d[field_name][0]["name"]
    except:
        pass


df = pd.DataFrame([{
    "Country": d["name"],
    "Alpha3 Code": d['alpha3Code'],
    "Capital": d['capital'],
    "Region": d['region'],
    "Sub-Region": d['subregion'],
    "Population": d['population'],
    "Lat and Lon": d['latlng'],
    "Area": d['area'],
    "Timezone": d['timezones'],
    "borders": d['borders'],
    "Currencies": extract_block('currencies', d),
    "Regional Bloc": extract_block('regionalBlocs', d)
    } for d in raw_data])

print(df.head())