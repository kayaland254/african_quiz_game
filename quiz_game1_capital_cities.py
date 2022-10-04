import random

countries = ["zambia", "kenya", "namibia", "ghana", "egypt", "cameroon", "DRC"]
capital_city = ["lusaka", "nairobi", "windhoek", "accra", "cairo", "yaonde", "kinshasa"]

i = len(countries)
country_index = random.choice(range(i))

selected_country = (countries[country_index])
selected_capital_city = (capital_city[country_index])
