import utils
import read_csv
import charts

def run():

  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

  country = input("Ingresa el país => ")

  result_total = utils.get_population_by_country(data, country)



  if len(result_total) > 0:
    country = result_total[0]
    keys, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], keys, values)

  # print(result_total)

'''
Otro dato interesante es que pueden renombrar un módulo dentro del código para cuando lo usen usar una abreviación con as

import moduloconnombrelargo as m
'''

# Dualidad para poder ejecutar el script desde diferente archivo o en el mismo archivo

# Se le llama: Entry point

if __name__ == '__main__':
  run()