import pandas as pd
import plotly.express as px

data = pd.read_csv('gclass.csv')
umddata = pd.read_csv('UMD.csv')

nonres = data[data['Residency']=='Non-resident']

races = nonres['Race'].value_counts()

races = pd.DataFrame(data=races)
races = races.rename(columns={'Race':'Count'})

fig = px.pie(races, values= 'Count', names=races.index, title='Non-Residents in Global Classrooms by Race')
fig.show()