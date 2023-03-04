import pandas as pd
import plotly.express as px

wkbk = pd.read_excel('Data_OIA.xlsx', sheet_name=None)

for sheet in wkbk:
    semester = wkbk[sheet]
    gf = semester['Gender'].value_counts()

    gf = pd.DataFrame(data=gf)
    gf = gf.rename(columns={'Gender':'Count'})

    fig = px.pie(gf, values= 'Count', names=gf.index, title=f'Global Classrooms Gender {sheet}')
    fig.show()






