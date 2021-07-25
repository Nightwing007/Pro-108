import pandas as pd
import csv
import plotly.figure_factory as pf
filePath = input("Enter File Path here : ")
f = pd.read_csv(filePath)
data = input("Enter the type of data : ")
df = f[data].tolist()
fig = pf.create_distplot([df],["Sales"],show_hist = False)
fig.show()
