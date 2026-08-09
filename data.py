import pandas as pd
import matplotlib.pyplot as plt
from Linear_regression import gradient_descent

df = pd.read_csv("study_time_vs_exam_score.csv")

m = 0
b = 0
l = 0.001
epochs = 10000
for i in range(epochs):
    if i % 50 ==0:
        print(i)
    m, b = gradient_descent(m, b, df, l)

plt.scatter(df["study_hours"],df["exam_score"])
x_axis = list(range(1,10))
y_axis = [m*x + b for x in x_axis]
plt.plot(x_axis,y_axis)
plt.show()


