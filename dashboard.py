import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("main_data.csv")
df['dteday'] = pd.to_datetime(df['dteday'])
df['day_type'] = df['holiday'].apply(lambda x: 'Holiday' if x == 1 else 'Working Day')

sns.set(style="whitegrid")
st.title("Bike Sharing Dashboard 🚴")
st.markdown("### Welcome to the Bike Sharing Dashboard! Discover fascinating insights into bike rental trends through the following visualizations.")

st.subheader("Proporsi Penyewaan Sepeda Berdasarkan Jenis Hari")
rentals_by_day_type = df.groupby('day_type').agg({'count': 'sum'}).reset_index()

fig1, ax1 = plt.subplots(figsize=(8, 8))
ax1.pie(rentals_by_day_type['count'], labels=rentals_by_day_type['day_type'], 
        autopct='%1.1f%%', startangle=140, colors=['#1E90FF', '#FFA500'])
st.pyplot(fig1)

st.markdown("### Data Penyewaan Berdasarkan Jenis Hari")
st.dataframe(rentals_by_day_type)

st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(
    x='weather_situation',
    y='count',
    data=df,
    ax=ax2,
    palette='Blues_d'
)
ax2.set_xlabel('Kondisi Cuaca', fontsize=12)
ax2.set_ylabel('Jumlah Pengguna Sepeda', fontsize=12)
st.pyplot(fig2)

st.markdown("### Data Penyewaan Berdasarkan Kondisi Cuaca")
weather_rentals = df.groupby('weather_situation').agg({'count': 'sum'}).reset_index()
st.dataframe(weather_rentals)

st.subheader("Tren Penggunaan Sepeda Bulanan (2012)")
df_2012 = df[df['dteday'].dt.year == 2012]
monthly_rentals = df_2012.groupby(df_2012['dteday'].dt.month)['count'].sum().reset_index()
monthly_rentals.columns = ['month', 'total_count']

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_rentals['month'] = monthly_rentals['month'].apply(lambda x: month_names[x - 1])

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.lineplot(data=monthly_rentals, x='month', y='total_count', marker='o', ax=ax3, color='blue')
ax3.set_xlabel('Bulan', fontsize=12)
ax3.set_ylabel('Total Penyewaan Sepeda', fontsize=12)
plt.xticks(rotation=45)
st.pyplot(fig3)

st.markdown("### Data Penyewaan Bulanan")
st.dataframe(monthly_rentals)

st.markdown("### Sumber Data")
st.write("Data ini diambil dari Bike Sharing Dataset.")