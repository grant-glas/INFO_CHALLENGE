import pandas as pd
import plotly.express as px

wkbk = pd.read_excel('Data_OIA.xlsx', sheet_name=None)

for sheet in wkbk:
# race per semester
# makes 7 pie charts
    semester = wkbk[sheet]
    rf = semester['Race'].value_counts()

    rf = pd.DataFrame(data=rf)
    rf = rf.rename(columns={'Race':'Count'})

    fig = px.pie(rf, values= 'Count', names=rf.index, title=f'Global Classrooms Race {sheet}')
    fig.show()
# 




