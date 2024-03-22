import matplotlib.pyplot as plt

def generate_bar_chart(name,labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./img/{name}.png')
  plt.close()

def generate_pie_chart(label, value):
  fig, ax = plt.subplots()
  ax.pie(value, labels=label)
  ax.axis('equal')
  plt.savefig('./img/pie.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 20, 200]
  generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)