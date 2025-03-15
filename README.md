# Dashboard Bike Sharing ✨
## New Update!!
...
Dashboard sudah interaktif dapat berubah berdasarkan tanggal
...
## Set Up Environtment - VS Code untuk Dashboard 
...
py -m venv .venv
.venv\Scripts\activate
...
## Run steamlit app

```
streamlit run dashboard.py
```
README ASSIGNMENT by Novia Rahmadhani Purnomo
email : noviarp17@student.ub.ac.id
Cohort ID : mc006d5x2415
Github Project : https://github.com/nopii17/bikesharingbaru 

day.csv --> file dataset awal (belum di cleaning)
hour.csv --> file dataset awal (belum di cleaning)
readme -dataset --> penjelasan rincian mengenai dataset awal
newday.csv --> file dataset setelah di cleaning
newhour.csv --> file dataset setelah di cleaning
Proyek_Analisis_Data --> alur analisis data dari data wrangling hingga visualization (menggunakan impor day.csv dan hour.csv)

setelah file di impor, load data dengan perintah
'''
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')
'''

kemudian jalankan semua kode di file 'Proyek Analisis Data' tersebut

dashboardBaru.py --> python untuk menjalankan streamlit (buka dengan Visual Studio Code)
impor data yang digunakan yaitu file newday.csv dan newhour.csv

pada command prompt run 'streamlit run dashboardBaru.py'

kemudian run file python, apabila sudah benar akan muncul dashboard streamlit di chrome

!! UNTUK MELIHAT DASHBOARD BISA LANGSUNG KE url.txt!!
