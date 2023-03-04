import pandas as pd
import re
import plotly.express as px

whole_wkbk = pd.read_excel('Data_OIA.xlsx',sheet_name=None)


# print(whole_wkbk['Summer 2022']['Major '])  #
wkbk_names = whole_wkbk.keys()



summer22 = whole_wkbk['Summer 2022']
white_courses = summer22[summer22['Race']=='White']['Course']

# fig = px.histogram(white_courses)
# fig.show()

total = []




