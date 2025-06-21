import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 Excel Dashboard - Day/Week/Year View")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    
    if 'Date' not in df.columns:
        st.warning("Please make sure your Excel file has a 'Date' column.")
    else:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df.dropna(subset=['Date'], inplace=True)

        # Time-based grouping
        df['Day'] = df['Date'].dt.date
        df['Week'] = df['Date'].dt.to_period("W").astype(str)
        df['Year'] = df['Date'].dt.year

        # User selects column to analyze
        columns_to_show = df.select_dtypes(include='number').columns.tolist()
        value_column = st.selectbox("Select value column to visualize", columns_to_show)

        # Time selection
        time_view = st.radio("Select Time View", ["Day", "Week", "Year"])

        if time_view == "Day":
            group_col = "Day"
        elif time_view == "Week":
            group_col = "Week"
        else:
            group_col = "Year"

        grouped = df.groupby(group_col)[value_column].sum().reset_index()

        st.subheader(f"{time_view} Matrix")
        st.dataframe(grouped)

        # Bar chart
        fig_bar = px.bar(grouped, x=group_col, y=value_column, title=f"{time_view} Bar Chart")
        st.plotly_chart(fig_bar, use_container_width=True)

        # Pie chart (top 5 only to avoid clutter)
        top5 = grouped.sort_values(by=value_column, ascending=False).head(5)
        fig_pie = px.pie(top5, names=group_col, values=value_column, title=f"Top 5 - {time_view} View")
        st.plotly_chart(fig_pie, use_container_width=True)