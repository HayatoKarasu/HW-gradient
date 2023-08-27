from matplotlib import pyplot as plt

plt.text(0.01, 0.9, "1) Градиент - это вектор, который указывает", fontsize=14)
plt.text(0.01, 0.8, "направление роста функуии. Направление", fontsize=14)
plt.text(0.01, 0.7, "убывания функции указывает обратный", fontsize=14)
plt.text(0.01, 0.6, "градиент или градиент со знаком минус.", fontsize=14)
plt.text(0.01, 0.5, "Примеры градиентов встречаются в дизайне:", fontsize=14)
plt.text(0.01, 0.4, "плавный переход от одного цвета к другому.", fontsize=14)
plt.text(0.01, 0.3, "А так же в машинном обучении, в методе", fontsize=14)
plt.text(0.01, 0.2, "градиентный спуск.", fontsize=14)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, "2) Решите пример:", fontsize=15)
form = r"$z = 3x^3+2y^2-12$"
plt.text(0.01, 0.8, form, fontsize=15)
plt.text(0.01, 0.7, "Вычислить градиент в точке (4, -2)", fontsize=15)
form = r"$\frac{∂z}{∂x} = (3x^3+2y^2-12)'_x = 18x$"
plt.text(0.01, 0.6, form, fontsize=15)
form = r"$\frac{∂z}{∂y} = (3x^3+2y^2-12)'_y = 4y$"
plt.text(0.01, 0.5, form, fontsize=15)
form = r"$grad_ z = (18x; 4y)$"
plt.text(0.01, 0.4, form, fontsize=15)
form = r"$grad|_m z = 18*4+4*(-2)=(72;-8)$"
plt.text(0.01, 0.3, form, fontsize=15)
form = r"$|grad_ z| = \sqrt{(\frac{∂z}{∂x})^2 + (\frac{∂z}{∂y})^2} = \sqrt{72^2+(-8)^2} = $"
plt.text(0.01, 0.2, form, fontsize=15)
form = r"$= \sqrt{5248} ≈ 72,44$"
plt.text(0.01, 0.1, form, fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, "Вывод:", fontsize=15)
plt.text(0.01, 0.8, "Если движение происходит в направлении", fontsize=14)
plt.text(0.01, 0.7, "градиента функции (72;-8), то получаем", fontsize=14)
plt.text(0.01, 0.6, "скорость максимального изменения функции", fontsize=14)
plt.text(0.01, 0.5, "72,44 в точке (4;-2)", fontsize=14)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()