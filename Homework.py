'''
#Создать объект pandas Series из листа, объекта NumPy, и словаря
'''
#Из листа
import pandas as pd
my_list = [1, 2, 3, 4, 5]
series_from_list = pd.Series(my_list)
print(series_from_list)
#Из объекта NumPy
import numpy as np
import pandas as pd
my_array = np.array([1, 2, 3, 4, 5])
series_from_array = pd.Series(my_array)
print(series_from_array)
#Из словаря
import pandas as pd
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
series_from_dict = pd.Series(my_dict)
print(series_from_dict)



'''
#Получить не пересекающиеся элементы в двух объектах Series
'''
import pandas as pd
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([4, 5, 6, 7, 8])
not_common_series1 = series1[~series1.isin(series2)]
not_common_series2 = series2[~series2.isin(series1)]
print("Не пересекающиеся элементы в series1:", not_common_series1)
print("Не пересекающиеся элементы в series2:", not_common_series2)



'''
#Узнать частоту уникальных элементов объекта Series (гистограмма)
'''


import pandas as pd
import matplotlib.pyplot as plt
series = pd.Series([1, 2, 3, 3, 4, 4, 5, 5, 5])
value_counts = series.value_counts()
value_counts.plot.bar()
plt.xlabel('Уникальные элементы')
plt.ylabel('Частота')
plt.title('Гистограмма частоты уникальных элементов')
plt.show()




'''
#Объединить два объекта Series вертикально и горизонтально
'''

#Вертикальное объединение 
import pandas as pd
series1 = pd.Series([1, 2, 3])
vertical_concat = pd.concat([series1, series2], axis=0)
print(vertical_concat)

#Горизонтальное объединение
import pandas as pd
series1 = pd.Series([1, 2, 3])
series2 = pd.Series([4, 5, 6])
horizontal_concat = pd.concat([series1, series2], axis=1)
print(horizontal_concat)




'''
#Найти разность между объектом Series и смещением объекта Series на n
'''

import pandas as pd
series = pd.Series([1, 2, 3, 4, 5])
n = 2
shifted_series = series.shift(n)
difference = series - shifted_series
print(difference)
