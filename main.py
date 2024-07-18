# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot = pd.DataFrame()
one_hot['robot'] = (data['whoAmI'] == 'robot').astype(int)
one_hot['human'] = (data['whoAmI'] == 'human').astype(int)

# Метод astype() в pandas используется для преобразования столбцов
# в другой тип данных. В данном случае мы преобразовываем логические значения
# (True/False) в целочисленные значения (1/0).

one_hot.to_csv('csv.csv')
print(one_hot.head(20))