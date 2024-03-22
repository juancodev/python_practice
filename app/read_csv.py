import csv

#delimiter me indica como vamos a separar los datos

# fileCSV = csv.DictReader(file,delimiter=',') => convertir a dict los datos

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data


if __name__ == '__main__':
  result = read_csv('./csv/data.csv')
  print(result)
