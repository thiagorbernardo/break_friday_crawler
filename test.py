
from country_list import countries_for_language

print(countries_for_language('pt_br'))

# for country in countries_for_language('pt_br'):
#     print(country)


import random

number_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
print("Original list:", number_list)

random.shuffle(number_list)
print("List after first shuffle:", number_list)

random.shuffle(number_list)
print("List after second shuffle:", number_list)