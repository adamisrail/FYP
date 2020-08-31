import numpy as np
import pandas as pd

path = r"D:\Dropbox\Dropbox\P1 Research\Pyhton Codes\Test data and models\2020-03-15_Flow.csv"
dataset = pd.read_csv(path)
np.array(dataset)
Xrow = dataset.iloc[[0], :].values
print(Xrow)
print(Xrow[0, 1])

pd.DataFrame(Xrow)
print(Xrow)