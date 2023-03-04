import pandas as pd
import plotly.express as px

data = pd.read_csv('gclass.csv')
umddata = pd.read_csv('UMD.csv')



races = data['Race'].value_counts()

races = pd.DataFrame(data=races)
races = races.rename(columns={'Race':'Count'})

fig = px.pie(races, values= 'Count', names=races.index, title='Global Classrooms Races')
fig.show()


umddata['Total'] = umddata['2020'] + umddata['2021'] + umddata['2022']
umddata = umddata[0:9]
print(umddata)

fig2 = px.pie(umddata,values='Total', names='Race', title='UMD Race Percentages')
fig2.show()



