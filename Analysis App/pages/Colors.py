import streamlit as st
import plotly.express as px


df = st.session_state['df']

col1, col2, col3 = st.columns([1,2,1])

def get_distribution_of_colors_in_dataset(df):
    color_v_c = df['color'].value_counts()
    no_of_colors = st.slider(label = 'No of colors', min_value = 2, max_value=color_v_c.shape[0])
    fig1 = px.bar(color_v_c[:no_of_colors])
    fig1.update_layout(
        title = f'Distribution of colors in this Dataset',
    )
    fig1

# def get_avg_price_for_each_color(df):
st.table(df[['price', 'color']].groupby('price')).agg({'mean'})

color_sidebar_options = ['','Avg_Price_Per_Color']
color_options = st.sidebar.selectbox(label = 'Select Visualizations', options=color_sidebar_options)
# with col2:
    # get_distribution_of_colors_in_dataset(df)
    # get_avg_price_for_each_color(df)