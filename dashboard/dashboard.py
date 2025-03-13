
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Bike Sharing Data Analysis", layout="wide")

# Title of the Dashboard
st.title("Bike Sharing Data Analysis")

# Cache data loading (Updated to use st.cache_data)
@st.cache_data
def load_data():
    day_df = pd.read_csv("C:\\Users\\Novia Rahmadhani\\OneDrive\\Documents\\Bike-sharing-dataset\\dashboard\\newday.csv")
    return day_df

day_df = load_data()

# Show the first few rows of the data
st.subheader("Dataset Overview")
st.write(day_df.head())

# 1. **Suhu vs Jumlah Penyewaan Sepeda per Hari**
st.subheader("Suhu vs Jumlah Penyewaan Sepeda per Hari")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=day_df, x='temp', y='cnt', color='blue', alpha=0.6)
plt.title('Hubungan antara Suhu dan Jumlah Penyewaan Sepeda per Hari')
plt.xlabel('Suhu (Normalisasi)')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.grid(True)
st.pyplot(plt)

# 2. **Kelembapan vs Jumlah Penyewaan Sepeda per Hari**
st.subheader("Kelembapan vs Jumlah Penyewaan Sepeda per Hari")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=day_df, x='hum', y='cnt', color='red', alpha=0.6)
plt.title('Hubungan antara Kelembapan dan Jumlah Penyewaan Sepeda per Hari')
plt.xlabel('Kelembapan (Normalisasi)')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.grid(True)
st.pyplot(plt)

# 3. **Hari dengan Penyewaan Sepeda Tertinggi**
st.subheader("Hari dengan Penyewaan Sepeda Tertinggi")
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Group by day to find the total rental count for each day
daily_rentals = day_df.groupby('dteday')['cnt'].sum()

# Find the day with the highest rental count
max_rentals_day = daily_rentals.idxmax()  # Get the date of the highest rental
max_rentals_count = daily_rentals.max()   # Get the highest rental count

# Display the result
st.write(f"**Hari dengan penyewaan sepeda tertinggi adalah {max_rentals_day.strftime('%Y-%m-%d')}**.")
st.write(f"Jumlah penyewaan pada hari tersebut adalah {max_rentals_count} sepeda.")

# 4. **Trend Penyewaan Sepeda per Hari**
st.subheader("Tren Penyewaan Sepeda per Hari")
plt.figure(figsize=(12, 6))
daily_rentals.plot(kind='line', color='blue', linewidth=2)

# Highlight the day with the highest rentals
plt.scatter(max_rentals_day, max_rentals_count, color='red', zorder=5)
plt.text(max_rentals_day, max_rentals_count + 100, f'{max_rentals_count}', 
         ha='center', color='red', fontsize=12, fontweight='bold')

# Adding labels and title
plt.title('Total Penyewaan Sepeda per Hari', fontsize=14)
plt.xlabel('Tanggal', fontsize=12)
plt.ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)

st.pyplot(plt)