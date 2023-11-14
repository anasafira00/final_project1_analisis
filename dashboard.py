import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Baca dataset
hour_df = pd.read_csv("C:/Users/anasafira/pydicoding/hour.csv")

# Konversi kolom 'dteday' ke tipe data datetime
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Sidebar Streamlit
st.sidebar.title("Dashboard Peminjaman Sepeda")
selected_data = st.sidebar.radio("Pilih Data:", ["Data Jam (Hourly)", "Data Harian (Daily)"])

# Visualisasi data jam atau harian
if selected_data == "Data Jam (Hourly)":
    st.title("Data Jam (Hourly)")
    st.dataframe(hour_df.head())

    # Visualisasi peminjaman per jam
    st.subheader("Grafik Peminjaman Sepeda per Jam")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=hour_df, x='hr', y='cnt', hue='weekday', marker='o')
    st.pyplot()

    # Informasi statistik
    st.subheader("Informasi Statistik")
    st.write("Rata-rata Jumlah Peminjaman Sepeda: ", round(hour_df['cnt'].mean()))
    st.write("Jumlah Peminjaman Sepeda Maksimum: ", hour_df['cnt'].max())
    st.write("Jumlah Peminjaman Sepeda Minimum: ", hour_df['cnt'].min())

else:
    # Data Harian
    day_df = pd.read_csv("C:/Users/anasafira/pydicoding/day.csv")
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])

    st.title("Data Harian (Daily)")
    st.dataframe(day_df.head())

    # Visualisasi peminjaman per hari
    st.subheader("Grafik Peminjaman Sepeda per Hari")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=day_df, x='dteday', y='cnt')
    st.pyplot()

    # Informasi statistik
    st.subheader("Informasi Statistik")
    st.write("Rata-rata Jumlah Peminjaman Sepeda: ", round(day_df['cnt'].mean()))
    st.write("Jumlah Peminjaman Sepeda Maksimum: ", day_df['cnt'].max())
    st.write("Jumlah Peminjaman Sepeda Minimum: ", day_df['cnt'].min())
