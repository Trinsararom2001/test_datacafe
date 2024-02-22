# import library
import pandas as pd #data manipulate
import streamlit as st #web abb (Dashboard (DB))
import numpy as np # function (math,arrays)
import matplotlib.pyplot as plt # visualized
import seaborn as sns # visualized
import plotly.express as px # ***visualized
import plotly.graph_objects as go
import datetime #time


#layout
st.set_page_config(
    page_title="Dashboard Food retail",
    page_icon=":bar_chart:",
    layout = 'wide',
)
# Add custom CSS to center-align the title
st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Center-aligned title
st.markdown("<h1 class='title'>Dashboard For Food retails</h1>", unsafe_allow_html=True)

path_mean = r'C:\Users\kan43\Downloads\data test from data cafe-20240221T180350Z-001\data test from data cafe\Data Cafe Test Before Interview\df_mean'
path_sum = r'C:\Users\kan43\Downloads\data test from data cafe-20240221T180350Z-001\data test from data cafe\Data Cafe Test Before Interview\df_sum'

df_mean = pd.read_csv(path_mean)
df_sum = pd.read_csv(path_sum)


# Convert date strings to datetime objects
df_mean['date'] = pd.to_datetime(df_mean['date'])
df_sum['date'] = pd.to_datetime(df_sum['date'])

# Sidebar for filtering options
st.sidebar.header("Dashboard For Food retails")
st.sidebar.header("Filter Commodity")

# Default to selecting all commodities
default_commodity_options = df_mean['commodity'].unique()
commodity_options = st.sidebar.multiselect("Select Commodity", default_commodity_options, default=default_commodity_options)

# Date range filter
start_date_default = df_mean['date'].min()
end_date_default = df_mean['date'].max()

start_date = st.sidebar.date_input("Start Date", min_value=df_mean['date'].min().date(), max_value=df_mean['date'].max().date(), value=start_date_default.date())
end_date = st.sidebar.date_input("End Date", min_value=df_mean['date'].min().date(), max_value=df_mean['date'].max().date(), value=end_date_default.date())


tab1, tab2 = st.tabs(["Mean", "Sum"])

with tab1:

    # Filter data based on commodity and date range
    filtered_data = df_mean[(df_mean['commodity'].isin(commodity_options)) & 
                        (df_mean['date'] >= pd.to_datetime(start_date)) & 
                        (df_mean['date'] <= pd.to_datetime(end_date))]

    # Dollar Sales by date
    sales_figure = px.line(filtered_data, x='date', y='dollar_sales', color='commodity'
                                        , title='Average Dollar Sales by date')
    sales_figure.update_layout(legend=dict(
        orientation="h",
        yanchor="top",
        y=1.15,
        xanchor="left",
        x=0.01
    ))

    # Average Dollar Sales by Commodity
    avg_sales_by_commodity = filtered_data.groupby('commodity')['dollar_sales'].mean().reset_index()
    avg_sales_figure = px.bar(avg_sales_by_commodity, x='commodity', y='dollar_sales',color='commodity', title='Average Dollar Sales by Commodity')
    avg_sales_figure.update_layout(legend=dict(
        orientation="h",
        yanchor="top",
        y=1.05,
        xanchor="left",
        x=0.01
    ))

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(sales_figure ,use_container_width = True)
    with col2:
        st.plotly_chart(avg_sales_figure ,use_container_width = True)

    # Create a scatter plot using Plotly Express
    fig1 = px.scatter(filtered_data, x='dollar_sales', y='units', color='commodity', title='Scatter Plot Dollar Sales vs Units')

    # Customize layout
    fig1.update_layout(xaxis_title='Dollar Sales',
                    yaxis_title='Units')
    fig1.update_layout(legend=dict(
        orientation="h",
        yanchor="top",
        y=1.05,
        xanchor="left",
        x=0.01
    ))

    # Display the plot in Streamlit
    st.plotly_chart(fig1, use_container_width = True)

with tab2:

    # Filter data based on commodity and date range
    filtered_data = df_sum[(df_sum['commodity'].isin(commodity_options)) & 
                        (df_sum['date'] >= pd.to_datetime(start_date)) & 
                        (df_sum['date'] <= pd.to_datetime(end_date))]

    # Dollar Sales by date
    sales_figure = px.line(filtered_data, x='date', y='dollar_sales', color='commodity'
                                        , title='Sum Dollar Sales by date')
    sales_figure.update_layout(legend=dict(
        orientation="h",
        yanchor="top",
        y=1.15,
        xanchor="left",
        x=0.01
    ))

    # Average Dollar Sales by Commodity
    avg_sales_by_commodity = filtered_data.groupby('commodity')['dollar_sales'].sum().reset_index()
    avg_sales_figure = px.bar(avg_sales_by_commodity, x='commodity', y='dollar_sales',color='commodity', title='Sum Dollar Sales by Commodity')
    avg_sales_figure.update_layout(legend=dict(
        orientation="h",
        yanchor="top",
        y=1.05,
        xanchor="left",
        x=0.01
    ))

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(sales_figure ,use_container_width = True)
    with col2:
        st.plotly_chart(avg_sales_figure ,use_container_width = True)

    # Create a scatter plot using Plotly Express
    fig1 = px.scatter(filtered_data, x='dollar_sales', y='units', color='commodity', title='Scatter Plot Dollar Sales vs Units')

    # Customize layout
    fig1.update_layout(xaxis_title='Dollar Sales',
                    yaxis_title='Units')
    fig1.update_layout(legend=dict(
        orientation="h",
        yanchor="top",
        y=1.05,
        xanchor="left",
        x=0.01
    ))

    # Display the plot in Streamlit
    st.plotly_chart(fig1, use_container_width = True)



