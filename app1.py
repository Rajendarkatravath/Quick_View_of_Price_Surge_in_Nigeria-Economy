import streamlit as st
from PIL import Image

# Set the page configuration
st.set_page_config(
    page_title="Quick View of Price Surge in the Nigerian Economy Using Data Science",
    page_icon="💰",
    layout="wide",
)

# Load the image
image_path = "imag1.jpg"
image = Image.open(image_path)

# Define the options for the sidebar
options = ["Introduction", "EDA", "Consumer Price Index", "GDP"]

# Create the sidebar with the options
st.sidebar.title("Navigation")
selected_option = st.sidebar.selectbox("Explore the page", options)

# Custom CSS for better styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stSidebar {
        background-color: #f0f2f6;
    }
    .stTitle, .stHeader {
        color: #343a40;
    }
    .stMarkdown {
        color: #343a40;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Introduction Page
if selected_option == "Introduction":
    st.title("Quick View of Price Surge in the Nigerian Economy Using Data Science")
    st.image(image, caption="Economic Price Surge", use_column_width=True)

    # Introduction section
    st.header("Introduction")
    st.markdown("""
    <div style='text-align: justify; font-size: 18px;'>
    The Nigerian economy has experienced a significant surge in prices and value, affecting everything 
    from daily commodities to various services and products in the market. This change has had varied 
    impacts on living conditions across different states. Our analysis will focus on key factors such 
    as incomes, expenditures, and savings capabilities of citizens.
    </div>
    """, unsafe_allow_html=True)

    # Challenge Background section
    st.header("Challenge Background")
    st.markdown("<h2 style='text-align: justify; font-size: 20px;'>The Problem:</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: justify; font-size: 18px;'>
    Develop a quick-view dashboard that provides comprehensive insights into the price surge 
    and its implications for the economy, leveraging Data Science techniques.
    </div>
    """, unsafe_allow_html=True)
    
    # Goal of the Project section
    st.header("Goal of the Project")
    st.markdown("""
    <div style='text-align: justify; font-size: 18px;'>
    The aim is to present a graphical view of selected items related to basic living needs, 
    including food items, transportation costs, taxation, wages, healthcare, and essential 
    commodities. We will also compare the value of the Naira and the Dollar against these prices 
    and analyze how these prices vary over time.
    </div>
    """, unsafe_allow_html=True)

# EDA Page
elif selected_option == "EDA":
    st.title("Exploratory Data Analysis")
    st.markdown("""
    <div style='text-align: justify; font-size: 18px;'>
    Sure! Here’s the revised introduction with an emoji:

Exploratory Data Analysis (EDA) is the process of analyzing datasets to summarize their main characteristics, often using visual methods. In economics, 
EDA focuses on examining GDP, CPI, and prices 📈 to uncover patterns and trends, providing insights into economic health and inflation dynamics while identifying anomalies and generating hypotheses for further analysis.
    </div>
    """, unsafe_allow_html=True)
    

# Consumer Price Index Page
elif selected_option == "Consumer Price Index":
    st.title("Consumer Price Index")
    st.write("""
    The Consumer Price Index (CPI) measures the average change over time in the prices paid by urban consumers for a market basket of consumer goods and services. It is a key indicator of inflation and purchasing trends in the economy.
    """)

# GDP Page
elif selected_option == "GDP":
    st.title("Gross Domestic Product")
    st.write("""
    Gross Domestic Product (GDP) is the total market value of all finished goods and services produced within a country's borders in a specific time period. It is a comprehensive measure of a nation's overall economic activity.
    """)
