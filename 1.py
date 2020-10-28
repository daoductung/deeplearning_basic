import pandas as pd
import os
import matplotlib.pyplot as plt

PATH_DATASET = os.getcwd() + '\\dataset'

data_linear_load = pd.read_csv(PATH_DATASET + '\\data_linear.csv')

plt.plot(data_linear_load['Diện tích'], data_linear_load['Giá'])
plt.title("Biểu đồ giữa diện tích và giá nhà")
plt.xlabel("Giá nhà")
plt.ylabel("Diện tích")
plt.show()