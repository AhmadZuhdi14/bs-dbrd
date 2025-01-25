import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# helper functions
def get_season_trends(df):
    return df.groupby('season')['cnt_day'].mean()

def get_workingday_comparison(df):
    return df.groupby('workingday')['cnt_day'].mean()

def get_hourly_distribution(df):
    return df.groupby('hr')['cnt_hour'].mean()

def main():
    st.title("Ahmad Zuhdi: Bike Sharing Data Dashboard")

    # Load data
    all_df = pd.read_csv("main_data.csv")

    # Sidebar filters
    st.sidebar.header("Filter Data")
    season_filter = st.sidebar.multiselect(
        "Pilih Musim:", options=[1, 2, 3, 4], default=[1, 2, 3, 4], format_func=lambda x: ["Spring", "Summer", "Fall", "Winter"][x-1]
    )
    workingday_filter = st.sidebar.radio("Hari Kerja atau Libur:", options=[0, 1], format_func=lambda x: "Libur" if x == 0 else "Hari Kerja")

    # Apply filters
    filtered_data = all_df[(all_df['season'].isin(season_filter)) & (all_df['workingday'] == workingday_filter)]

    # Headings
    st.header("Bike Sharing Data Insights")

    # Visualizations
    st.subheader("Tren Penyewaan Sepeda Berdasarkan Musim")
    season_trends = get_season_trends(filtered_data)
    st.bar_chart(season_trends)

    st.subheader("Penyewa sepeda pada Libur atau Hari Kerja")
    workingday_comparison = get_workingday_comparison(filtered_data)
    st.bar_chart(workingday_comparison)

    st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Waktu")
    hourly_distribution = get_hourly_distribution(filtered_data)
    st.line_chart(hourly_distribution)

if __name__ == "__main__":
    main()