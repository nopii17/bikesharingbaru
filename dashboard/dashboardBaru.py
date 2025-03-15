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
    # Load the dataset from the uploaded files
    day_df = pd.read_csv("dashboard/newday.csv")
    hour_df = pd.read_csv("dashboard/newhour.csv")
    return day_df, hour_df

day_df, hour_df = load_data()

# Convert 'dteday' to datetime for filtering
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Interactivity: Date range filter
st.sidebar.subheader("Filter by Date Range")
start_date = st.sidebar.date_input("Start date", day_df['dteday'].min())
end_date = st.sidebar.date_input("End date", day_df['dteday'].max())

# Filter data based on the selected date range
filtered_day_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & (day_df['dteday'] <= pd.to_datetime(end_date))]

# Show the first few rows of the filtered data
st.subheader("Dataset Overview")
st.write(filtered_day_df.head())

# 1. **Suhu vs Jumlah Penyewaan Sepeda per Hari**
st.subheader("Suhu vs Jumlah Penyewaan Sepeda per Hari")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=filtered_day_df, x='temp', y='cnt', color='blue', alpha=0.6)
plt.title('Hubungan antara Suhu dan Jumlah Penyewaan Sepeda per Hari')
plt.xlabel('Suhu (Normalisasi)')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.grid(True)
st.pyplot(plt)

# 2. **Kelembapan vs Jumlah Penyewaan Sepeda per Hari**
st.subheader("Kelembapan vs Jumlah Penyewaan Sepeda per Hari")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=filtered_day_df, x='hum', y='cnt', color='red', alpha=0.6)
plt.title('Hubungan antara Kelembapan dan Jumlah Penyewaan Sepeda per Hari')
plt.xlabel('Kelembapan (Normalisasi)')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.grid(True)
st.pyplot(plt)

# 3. **Binning based on Weather Conditions**
st.subheader("Binning Berdasarkan Kondisi Cuaca")

# Binning Temperature, Humidity, and Windspeed into Low, Medium, High categories
day_df['temp_bin'] = pd.cut(day_df['temp'], bins=[-float('inf'), 0.3, 0.7, float('inf')], labels=['Rendah', 'Sedang', 'Tinggi'])
day_df['hum_bin'] = pd.cut(day_df['hum'], bins=[-float('inf'), 0.3, 0.7, float('inf')], labels=['Rendah', 'Sedang', 'Tinggi'])
day_df['windspeed_bin'] = pd.cut(day_df['windspeed'], bins=[-float('inf'), 0.3, 0.7, float('inf')], labels=['Rendah', 'Sedang', 'Tinggi'])

# Display the binned data
st.write(day_df[['dteday', 'temp_bin', 'hum_bin', 'windspeed_bin']].head())

# 4. **Hari dengan Penyewaan Sepeda Tertinggi**
st.subheader("Hari dengan Penyewaan Sepeda Tertinggi")

# Group by day to find the total rental count for each day
daily_rentals = filtered_day_df.groupby('dteday')['cnt'].sum()

# Find the day with the highest rental count
max_rentals_day = daily_rentals.idxmax()  # Get the date of the highest rental
max_rentals_count = daily_rentals.max()   # Get the highest rental count

# Display the result
st.write(f"**Hari dengan penyewaan sepeda tertinggi adalah {max_rentals_day.strftime('%Y-%m-%d')}**.")
st.write(f"Jumlah penyewaan pada hari tersebut adalah {max_rentals_count} sepeda.")

# 5. **Trend Penyewaan Sepeda per Hari**
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
