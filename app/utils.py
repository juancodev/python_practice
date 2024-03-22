# crear modulos en Python

def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  return population_dict.keys(), population_dict.values()


# modulo para validar si el dato existe en el pais
def get_population_by_country(data: list, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result

def world_population_percentage(labels, data):
  print(labels)
  for el in data:
    print(el)