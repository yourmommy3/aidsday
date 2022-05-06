import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("./CPU_benchmark.csv")

#plt.bar(data['price'],data['cpuName'])

#plt.scatter(data['price'],data['cpuName'])

plt.pie(data['cores'])
plt.show()