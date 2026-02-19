import time
import config
import json

def load_countries():
    with open('countries.json', 'r', encoding = 'utf-8') as file:
        return json.load(file)
    
def build_lookup(countries_data):
    lookup = {}

    for country in countries_data:
        accepted_country_name = country["name"]

        # Official Country Name
        lookup[accepted_country_name.lower()] = accepted_country_name

        # Country Alias
        for alias in country["aliases"]:
            lookup[alias.lower()] = accepted_country_name

    return lookup

countries_data = load_countries()
print(build_lookup(countries_data))