import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
st.set_page_config(page_title='execetuion data')
st.header('execetion data analaysis')
execl_file='exmaple.xlsx'
sheet_name='Data'
df=pd.read_excel(execl_file,sheet_name=sheet_name,usecols='A',header=0)
df_participants=pd.read_excel(execl_file,sheet_name=sheet_name,usecols='A:B',header=0)
st.dataframe(df)
# st.dataframe(df_participants)
pie_chart=px.pie(df_participants,title='PIE CHART',values='VALUE',names='NAMES')
st.plotly_chart(pie_chart)
