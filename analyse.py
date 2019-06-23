import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('tth.csv')


years = df.groupby('Founded Year').size()

for i in range(len(df['Industry'])):
    df['Industry'][i] = str(df['Industry'][i])
    df['Industry'][i] = df['Industry'][i].strip()
    if df['Industry'][i] == 'IOT':
        df['Industry'][i] = 'IoT'
    if df['Industry'][i] == 'Fleet':
        df['Industry'][i] = 'Fleet Management'
    if df['Industry'][i] == 'HealthCare':
        df['Industry'][i] = 'Healthcare'
    if df['Industry'][i] == 'nan':
        df['Industry'][i] = 'Unnamed'

fields = df.groupby('Industry').size()


trace = go.Pie(labels=list(years.index), title='Startups Founded', values=years.values,
               hoverinfo='label+percent', textinfo='value',
               textfont=dict(size=10),
               marker=dict(line=dict(color='#ffffff', width=2)))


pyo.plot([trace], filename='tth_pie_chart.html')

tr = go.Bar(x = list(fields.index), y = fields.values, name = 'Startups Industry',
            marker = dict(color = '#000FFF'))

layout = go.Layout(
    xaxis=dict(title='Industry', titlefont=dict(size=14), tickangle=-35, ticklen=4),
    yaxis=dict(title='No. of Startups', titlefont=dict(size=14)),
    font=dict(size=8)
)

fig = go.Figure(data=[tr], layout=layout)

pyo.plot(fig, filename='tth_bar_chart.html')



