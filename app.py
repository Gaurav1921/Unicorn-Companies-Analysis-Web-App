import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load your data
df = pd.read_csv('Unicorn Companies Data (After Preprocessing).csv')

# Set the page title and icon
st.set_page_config(
    page_title="Unicorn Companies Analysis",
    page_icon="🦄",
)

# Main title
st.title("Unicorn Companies Analysis")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Home", "Data Summary", "Country Analysis", "City Analysis", "Industry Analysis"])

if page == "Home":
    st.header("Welcome to the Unicorn Companies Analysis Dashboard")
    st.write("Explore data about unicorn companies around the world.")

elif page == "Data Summary":
    st.header("Data Summary")
    st.subheader("Dataset Preview")
    st.write(df.head())

    # Summary statistics
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # You can add more summary statistics or charts here...

elif page == "Country Analysis":
    st.header("Country Analysis")
    
    # Create a dropdown for selecting a country
    selected_country = st.selectbox("Select a Country", df['Country'].unique())

    # Filter data for the selected country
    country_df = df[df['Country'] == selected_country]

    # Display some information about the selected country
    st.subheader(f"Analysis for {selected_country}")
    st.write(f"Total unicorn companies in {selected_country}: {len(country_df)}")

    # Create a chart (example using Plotly Express)
    # Group the data by 'Year' and count the number of companies for each year
    count_by_year = country_df['Year'].value_counts().reset_index()
    count_by_year.columns = ['Year', 'Count']

    # Create a bar chart
    fig = px.bar(count_by_year, x='Year', y='Count', title=f"Unicorn Companies in {selected_country} Over Time")
    st.plotly_chart(fig)

    # Create another chart (example using Plotly Graph Objects)
    fig2 = go.Figure()
    fig2.add_trace(go.Pie(
        labels=country_df['Industry'].value_counts().index,
        values=country_df['Industry'].value_counts().values,
        title=f"Industry Distribution in {selected_country}",
    ))
    st.plotly_chart(fig2)

    # You can add more country-specific analysis here...

elif page == "City Analysis":
    st.header("City Analysis")
    
    # Create a dropdown for selecting a city
    selected_city = st.selectbox("Select a City", df['City'].unique())

    # Filter data for the selected city
    city_df = df[df['City'] == selected_city]

    # Display some information about the selected city
    st.subheader(f"Analysis for {selected_city}")
    st.write(f"Total unicorn companies in {selected_city}: {len(city_df)}")

    # Create a chart (example using Plotly Express)
    fig1 = px.pie(city_df, names='Industry', title=f"Unicorn Companies in {selected_city} by Industry")
    st.plotly_chart(fig1)

    # Create another chart (example using Plotly Graph Objects)
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=city_df['Year'],
        y=city_df['Valuation ($B)'],
        marker_color='skyblue',
        name="Valuation",
    ))
    fig2.update_layout(title_text=f"Valuation Trends in {selected_city}")
    st.plotly_chart(fig2)

    # You can add more city-specific analysis here...

elif page == "Industry Analysis":
    st.header("Industry Analysis")

    # Create a dropdown for selecting an industry
    selected_industry = st.selectbox("Select an Industry", df['Industry'].unique())

    # Filter data for the selected industry
    industry_df = df[df['Industry'] == selected_industry]

    # Display some information about the selected industry
    st.subheader(f"Analysis for {selected_industry}")
    st.write(f"Total unicorn companies in the {selected_industry} industry: {len(industry_df)}")

    # Create a chart (example using Plotly Express)
    fig1 = px.histogram(industry_df, x='Valuation ($B)',
                        title=f"Distribution of Valuations for {selected_industry} Companies")
    st.plotly_chart(fig1)

    # Create another chart (example using Plotly Graph Objects)
    fig2 = go.Figure()
    fig2.add_trace(go.Box(
        x=industry_df['Year'],
        y=industry_df['Valuation ($B)'],
        name="Valuation",
    ))
    fig2.update_layout(title_text=f"Valuation Distribution Over Time in {selected_industry}")
    st.plotly_chart(fig2)

    # You can add more industry-specific analysis here...
