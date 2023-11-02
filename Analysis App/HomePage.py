import streamlit as st
import pandas as pd

csv_file = '../data/cleaned_samsung_mobile_new_data.csv'

st.set_page_config(page_title='Samsung Mobile Visualization', layout = 'wide', page_icon=':bar_chart')

left_col, center_col, right_col = st.columns([1,2,1])

with center_col:
    st.title(':red[Samsung Mobile] :blue[Visualization Analysis]🤖')

@st.cache_data
def get_csv(file_path):
    df = pd.read_csv(file_path, index_col=None)
    df.to_csv()
    return df

df = get_csv(csv_file)

if 'df' not in st.session_state:
    st.session_state['df'] = df

st.table(df.head(13))

