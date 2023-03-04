import pandas as pd
import plotly.express as px

data = pd.read_csv('gclass.csv')

# grad races
races = data[data['Student Status']=='Undergraduate']
races = races['Race'].value_counts()


races = pd.DataFrame(data=races)
races = races.rename(columns={'Race':'Count'})

fig = px.pie(races, values= 'Count', names=races.index, title='Global Classrooms Undergraduates')
fig.show()