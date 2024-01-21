import requests
import pandas as pd
import time
import streamlit as st
import plotly.express as px
from PIL import Image
def get_all_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response as JSON
        posts_data = response.json()
        return posts_data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

def update_excel_file(posts_data, excel_file_path):
    if posts_data:
        # Normalize the data after the get response
        df = pd.json_normalize(posts_data)
        
        # Append the data to the existing Excel file
        with pd.ExcelWriter(excel_file_path, mode='w', engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='ex1')
        
        print(f"Data updated in Excel file: {excel_file_path}")
        st.set_page_config(page_title='execetuion data')
        st.header('execetion data analaysis')
        #excel file name 
        execl_file='test.xlsx'
        #excel sheet name
        sheet_name='ex1'
        #coloumn to be used make sure you have the name col name as in the exccel file
        df=pd.read_excel(execl_file,sheet_name=sheet_name,usecols='B:C',header=0)
        df_participants=pd.read_excel(execl_file,sheet_name=sheet_name,usecols='B:C',header=0)
        st.dataframe(df)
        #id and title is the col name in the execl file name
        pie_chart=px.pie(df_participants,title='PIE CHART',values='id',names='title')
        st.plotly_chart(pie_chart)

# path of excel or excel file name
excel_file_path = "test.xlsx"

while True:
    # Retrieve all  data
    all_posts_data = get_all_posts()
    
    # calling the update function for updating excel data
    update_excel_file(all_posts_data, excel_file_path)

    # Wait for 10 seconds 
    time.sleep(10)