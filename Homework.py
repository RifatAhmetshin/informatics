'''
#Цель задания - исследование функции 
f(x)=(x^b+a^b)/x^b
при различных значениях α и β. 
Для каждой задачи необходимо: 
Построить график (размер графика должен быть достаточным, чтобы визуально увидеть особенности изучаемых функций), график каждой функции должен быть одного цвета для одного значения α и β. 
Подписать оси и заголовок 
Создать легенду 
Сохранить изображение в svg файл 
Построить в общих осях графики для: 
α=1,β=1 
α=2,β=1
'''
import matplotlib.pyplot as plt
import numpy as np
def f(x, a, b):
    return (x**b + a**b) / x**b
x = np.linspace(0.1, 10, 100)
alpha_values = [1, 2]
beta_values = [1, 2]
for alpha in alpha_values:
    for beta in beta_values:
        y = f(x, alpha, beta)
        plt.plot(x, y, label=f'α={alpha}, β={beta}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.legend()
plt.savefig('output.svg', format='svg')
plt.show()


'''
#остроить в общих осях графики для x>0.
На том же графике сделать 2 врезки, демонстрирующие поведение графиков на 2 интервалах:

для малых x
для больших x
Необходимо продемонстрировать возможность (или невозможность) пересечений и стремление функций.

Цвет линий на врезках и основном графике должен быть одинаковым для одних и тех же значений α и β.

'''
import numpy as np
import matplotlib.pyplot as plt
a = 1
b = 1
x = np.linspace(0.01, 10, 100) 
y = (x**b + a**b) / x**b  
x_small = np.linspace(0.01, 0.1, 50)
y_small = (x_small**b + a**b) / x_small**b
plt.plot(x_small, y_small, '--', label='Малые значения x')
x_large = np.linspace(10, 100, 50)
y_large = (x_large**b + a**b) / x_large**b
plt.plot(x_large, y_large, '--', label='Большие значения x')
plt.plot(x, y, label=r'$\alpha=1, \beta=1$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x) для α=1, β=1 с врезками')
plt.legend()
plt.savefig('plot_with_insets.svg')
plt.show()



'''
#Построить в общих осях графики для x<0.
На том же графике сделать 1 врезку, демонстрирующую поведение графиков при удалении x от 0 к −∞.

Необходимо продемонстрировать возможность (или невозможность) пересечений и стремление функций. Так же нанесите на графики прямую f(x) = 0.

Цвет линий на врезках и основном графике должен быть одинаковым для одних и тех же значений α и β.

'''

import numpy as np
import matplotlib.pyplot as plt
a = 1
b = 1
x = np.linspace(-10, -0.01, 100)  
y = (x**b + a**b) / x**b  
plt.plot(x, y, label=r'$\alpha=1, \beta=1$, x < 0')
plt.axhline(0, color='black', linestyle='--', label=r'$f(x) = 0$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x) для α=1, β=1 с врезкой для x < 0')
plt.legend()
plt.savefig('plot_with_inset_negative_x.svg')
plt.show()



'''
#Построить в общих осях графики для:
α=1,β=0.5

α=1,β=−0.5

α=1,β=−1.5
Сделайте выводы о поведении графиков, включая возрастание/убывание и выпуклость/вогнутость

В результате выполнения предыдущей задачи, вы вероятно заметите, что все графики с α=1 проходят через общую точку (1, 2).

Постройте в одном ряду 3 графика, чтобы убедиться в выводах, сделанных по результатам предыдущей задачи.

Каждый график будет содержать 4 кривые. 2 общих:

α=1,β=0 (в качестве цвета попробуйте использовать 'b--')

α=1,β=−1 (в качестве цвета попробуйте использовать 'r--')
И по 2 уникальных для каждого графика:

α=1,β=0.5 и

α=1,β=0.8

α=1,β=−0.5 и

α=1,β=−0.8

α=1,β=−1.5 и

α=1,β=−2.5

Не забудьте добавить легенду на каждый график. Для этого может потребоваться вызвать метод legend() для каждого объекта осей.
'''

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.1, 10, 100)
y_general_1 = (x**0 + 1**0) / x**0
y_general_2 = (x**(-1) + 1**(-1)) / x**(-1)
a1, b1 = 1, 0.5
y1_unique_1 = (x**b1 + a1**b1) / x**b1
a1, b1 = 1, 0.8
y1_unique_2 = (x**b1 + a1**b1) / x**b1
plt.subplot(131)
plt.plot(x, y_general_1, 'b--', label=r'$\alpha=1, \beta=0$')
plt.plot(x, y_general_2, 'r--', label=r'$\alpha=1, \beta=-1$')
plt.plot(x, y1_unique_1, label=r'$\alpha=1, \beta=0.5$')
plt.plot(x, y1_unique_2, label=r'$\alpha=1, \beta=0.8$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(r'График функции $f(x)$ для α=1, β=0.5')
plt.legend(loc='upper left')
a2, b2 = 1, -0.5
y2_unique_1 = (x**b2 + a2**b2) / x**b2
a2, b2 = 1, -0.8
y2_unique_2 = (x**b2 + a2**b2) / x**b2
plt.subplot(132)
plt.plot(x, y_general_1, 'b--', label=r'$\alpha=1, \beta=0$')
plt.plot(x, y_general_2, 'r--', label=r'$\alpha=1, \beta=-1$')
plt.plot(x, y2_unique_1, label=r'$\alpha=1, \beta=-0.5$')
plt.plot(x, y2_unique_2, label=r'$\alpha=1, \beta=-0.8$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(r'График функции $f(x)$ для α=1, β=-0.5')
plt.legend(loc='upper right')
a3, b3 = 1, -1.5
y3_unique_1 = (x**b3 + a3**b3) / x**b3
a3, b3 = 1, -2.5
y3_unique_2 = (x**b3 + a3**b3) / x**b3
plt.subplot(133)
plt.plot(x, y_general_1, 'b--', label=r'$\alpha=1, \beta=0$')
plt.plot(x, y_general_2, 'r--', label=r'$\alpha=1, \beta=-1$')
plt.plot(x, y3_unique_1, label=r'$\alpha=1, \beta=-1.5$')
plt.plot(x, y3_unique_2, label=r'$\alpha=1, \beta=-2.5$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(r'График функции $f(x)$ для α=1, β=-1.5')
plt.legend(loc='upper right')
plt.subplots_adjust(wspace=0.4)
plt.savefig('multiple_graphs.svg')
plt.show()