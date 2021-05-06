import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
data = pd.read_csv("phq_all_final.csv")
data["dates"] = pd.to_datetime(data["date"], format="%Y-%m-%dT%H:%M:%S")
patient_id = int(input("Enter patient ID:"))
records = data[data["patient_id"] == patient_id][["dates", "score"]].to_numpy()
plt.plot(records[:,0], records[:,1],'b-o')
plt.plot([records[0, 0], records[-1, 0]], [10, 10], 'r-', label="Threshold")
plt.yticks(list(range(0,21,5)))
fig = plt.gcf()
fig.set_figwidth(15)
fig.set_figheight(10)
ax = plt.gca()
plt.legend()
plt.show()