import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu

# Load data
file_path = 'dataset/1960_onwards.csv'
data = pd.read_csv(file_path)

# Define plotting functions
def plot_gdp(data):
    fig, ax = plt.subplots()
    ax.plot(data['Year'], data['GDP (constant LCU)'], label='GDP (constant LCU)')
    ax.plot(data['Year'], data['GDP (current LCU)'], label='GDP (current LCU)')
    plt.title('GDP Over Time')
    plt.xlabel('Year')
    plt.ylabel('GDP')
    plt.legend()
    st.pyplot(fig)

def plot_population(data):
    fig, ax = plt.subplots()
    ax.plot(data['Year'], data['Population, total'], label='Total Population')
    ax.plot(data['Year'], data['Population, female'], label='Female Population')
    ax.plot(data['Year'], data['Population, male'], label='Male Population')
    plt.title('Population Dynamics')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend()
    st.pyplot(fig)   

def plot_petrol_prices(data):
    fig, ax = plt.subplots()
    ax.plot(data['Year'], data['Petrol Price (Naira)'])
    plt.title('Petrol Prices Over Time')
    plt.xlabel('Year')
    plt.ylabel('Price in Naira')
    st.pyplot(fig)

def plot_inflation(data):
    fig, ax = plt.subplots()
    ax.plot(data['Year'], data['Inflation, consumer prices (annual %)'], label='Consumer Price Inflation')
    ax.plot(data['Year'], data['Inflation, GDP deflator (annual %)'], label='GDP Deflator Inflation')
    plt.title('Inflation Trends')
    plt.xlabel('Year')
    plt.ylabel('Inflation Rate (%)')
    plt.legend()
    st.pyplot(fig)

def plot_financial_indicators(data):
    fig, ax = plt.subplots()
    ax.plot(data['Year'], data['Money Supply M2'], label='Money Supply M2')
    ax.plot(data['Year'], data['CBN Bills'], label='CBN Bills')
    plt.title('Financial and Monetary Indicators')
    plt.xlabel('Year')
    plt.ylabel('Values')
    plt.legend()
    st.pyplot(fig)

def plot_credit(data):
    fig, ax = plt.subplots()
    ax.plot(data['Year'], data['GDP growth (annual %)'], label='GDP Growth Rate')
    plt.title('Credit to Private Sector')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate (%)')
    plt.legend()
    st.pyplot(fig)

def plot_oil_sector(data):
    fig, ax = plt.subplots()
    ax.plot(data['Year'], data['Crude oil price'], label='Crude Oil Price')
    plt.title('Oil Sector Insights')
    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.legend()
    st.pyplot(fig)

def plot_debt_unemployment(data):
    fig, ax = plt.subplots()
    ax.plot(data['Year'], data['Unemployment, total (% of total labor force) (modeled ILO estimate)'], label='Unemployment Rate')
    plt.title('Debt and Unemployment')
    plt.xlabel('Year')
    plt.ylabel('Unemployment Rate (%)')
    plt.legend()
    st.pyplot(fig)

# Streamlit app structure
with st.sidebar:
    selected = option_menu(
        menu_title="Explore",
        options=["Introduction", "EDA", "Visualizations", "Consumer Price Index", "GDP"],
        menu_icon="cast"
    )

if selected == "Introduction":
    st.title('Quick View of Price Surge in Nigeria Economy Using Data Science')
    st.image("media/surge-price.jpg", caption="Economic Overview", use_column_width=True)
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
    st.subheader('GDP Insights')
    st.write("""
    GDP in Constant and Current LCU
    - Correlation: The GDP in constant and current Local Currency Units (LCU) shows a very high correlation (0.994), indicating consistency in GDP measurements over time.
    - Trend: A significant upward trend in GDP highlights sustained economic growth in Nigeria over the years.
    """)
    plot_gdp(data)

    st.subheader('Population Dynamics')
    st.write("""
    Total, Female, and Male Populations
    - Correlation: Strong correlations exist between the total, female, and male populations, indicating consistent growth across all demographic segments.
    - Trend: Steady population growth from 1960 onwards, with annual growth rates around 2% for both male and female populations.
    """)
    plot_population(data)

    st.subheader('Petrol Prices and GDP')
    st.write("""
    - Correlation: Petrol prices in Naira show a positive correlation with GDP in US dollars (0.229) and per capita GDP (0.286), suggesting a relationship between energy prices and economic performance.
    - Trend: Petrol prices have seen a steady increase, particularly from the late 1990s onwards, correlating with global oil price changes and domestic policy adjustments.
    """)
    plot_petrol_prices(data)

    st.subheader('Inflation Trends')
    st.write("""
    - 1981: Extremely high inflation rates following the global oil price collapse.
    - 1988-1989: High consumer price inflation, reflecting economic instability.
    - 1992-1995: Persistent high inflation due to structural adjustment programs and economic reforms.
    """)
    plot_inflation(data)

    st.subheader('Financial and Monetary Indicators')
    st.write("""
    - Total Reserves: A significant increase in total reserves over the years, indicating improved accumulation of foreign exchange and gold reserves.
    - Narrow Money and Money Supply (M3): Both metrics show noticeable upward trends, reflecting increased monetary circulation.
    """)
    plot_financial_indicators(data)

    st.subheader('Credit to Private Sector')
    st.write("""
    - Credit Growth: Steady increase in credit extended to the private sector, indicating growth in private sector activities and investments.
    """)
    plot_credit(data)

    st.subheader('Download the Entire Report:')

    with open("media/eda_report.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    
    st.download_button(
        label="Download Full Report",
        data=PDFbyte,
        file_name="EDA_Full_Report.pdf",
        mime="application/pdf"
    )

elif selected == "Visualizations":
    st.header("Visualizations and Insights")
    # Continue with content for Consumer Price Index

elif selected == "Consumer Price Index":
    st.header("Consumer Price Index")
    # Continue with content for Consumer Price Index

elif selected == "GDP":
    st.header("GDP Analysis")
    # Continue with content for GDP

