import pandas as pd

df = pd.read_excel("iris_dataset.xlsx")
print(df.head())
print(df.info())
sepal_length = df['sepal_length']
print(sepal_length)