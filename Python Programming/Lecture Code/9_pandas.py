import pandas as pd
import numpy as np

df = pd.read_excel('address.xlsx')
print(df['이름'])
print(df.to_numpy())

a = np.random.random((5,5))
print(a)
print(a[1:-1, 1:4])