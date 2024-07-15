import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="Explore",
        options=["Introduction", "EDA", "Consumer Price Index", "GDP"],
        menu_icon="cast"
    )

if selected == "Introduction":
    st.title('Quick View of Price Surge in Nigeria Economy Using Data Science')

    st.subheader('Challenge Background')
    st.write("""
    The Nigerian economy has undergone a fast surge in prices and value, ranging from daily commodities 
    to services and products available in the markets. This has changed the economy from state to state in 
    terms of living conditions, as such we intend to look directly at major pillars like incomes, 
    expenditures, and savings capabilities of citizens.
    """)

    st.subheader('The Problem')
    st.write("""
    Create a quick view dashboard that will provide in-depth information on price surge and its effects 
    on the economy using Data Science.
    """)

    st.subheader('Goal of the Project')
    st.write("""
    Present a graphical view of selected items based on basic living needs from food items, cost of 
    transportation, taxation, wages, healthcare, and essential commodities and their rise in prices, 
    also compare the value of Naira and Dollar against these prices.
    """)

    st.subheader('Scope and Approach')
    st.write("""
    This project will focus on:
    - Collecting and analyzing relevant datasets that capture price variations across different sectors.
    - Conducting exploratory data analysis (EDA) to identify patterns and correlations.
    - Implementing data visualization techniques to present findings effectively.
    - Developing predictive models to forecast future price trends and economic indicators.
    - Incorporating interactive elements into the dashboard to enhance user engagement and understanding.
    - Providing actionable insights to stakeholders, policymakers, and the general public.
    """)

elif selected == "EDA":
    st.header("Exploratory Data Analysis")
    # Continue with content for EDA

elif selected == "Consumer Price Index":
    st.header("Consumer Price Index")
    # Continue with content for Consumer Price Index

elif selected == "GDP":
    st.header("GDP Analysis")
    # Continue with content for GDP
