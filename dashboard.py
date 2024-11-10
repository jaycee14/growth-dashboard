import streamlit as st
import numpy as np
import plotly.express as px
from utils import get_data, prep_data
from report_data import reports

st.title('UK Productivity Hours by Region')    

st.write('Data from https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/labourproductivity/datasets/labourproductivitytables110andr1')

raw_data = get_data()
data_re_org = prep_data(raw_data,'ITL1')

ymin, ymax = data_re_org.Hours.min(),data_re_org.Hours.max() *1.1

fig = px.bar(data_re_org, x="Region", y="Hours", 
             animation_frame="Year",title='All Regions over Time',)

fig.update_layout(yaxis_range=[ymin,ymax])

st.subheader('Interactive Dashboards')

st.plotly_chart(fig, use_container_width=True,)


def gen_regions(df):

    regions = list(df.Region.unique())

    all_entries=[]

    for region in regions:
        all_entries.append(
            {'label':region,
            'method':'update',
             'args':[{
                 'y':[df.loc[df.Region==region,'Hours']],
                 'x':[df.loc[df.Region==region,'Year']]
               }]}
        )

    return all_entries

buttons_list = gen_regions(data_re_org)

fig2 = px.bar(data_re_org.loc[data_re_org.Region=='North East'], x="Year", y="Hours", title='Individual Region Values')

fig2.update_layout(updatemenus=[dict(
    type='dropdown',
    direction='down',
    buttons=list(buttons_list)
)], yaxis_range=[ymin,ymax])

st.plotly_chart(fig2, use_container_width=True)

st.subheader('LLM Generated Commentary')

rep = st.selectbox(
    "Report Selection",
    ('1','2','5','10'),
    index=None
)

if rep is not None:
    st.markdown(reports[rep])
