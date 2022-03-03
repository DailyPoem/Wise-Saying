import pandas as pd

data = pd.read_csv('./dataset.csv')
print(data['content'][0][6])
print(data['author'][0])