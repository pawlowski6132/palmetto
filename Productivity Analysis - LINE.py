import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
from plotly.subplots import make_subplots


df = pd.read_csv('palmetto2.csv', index_col = 'Week Ending', parse_dates = True)

# df.head()
df['Productivity'] = df['Tot Vol'] / df['Tot Hr']

y2 = df['12wk_MA'] = df['Productivity'].rolling(window = 12).mean()
 
x = df.index
y = df['Productivity']


trace0 = go.Scatter(x = x,
                    y = y,
                    mode = 'lines+markers',
                    name = 'Productivity'
                    )

trace1 = go.Scatter(x = x,
                    y = y2,
                    mode = 'lines',
                    name = '12 Week Mov Avg',
                    )

data = [trace0, trace1]

layout = go.Layout(title = 'Palmetto Productivity')

fig = go.Figure(data = data, layout = layout)

pyo.plot(fig)