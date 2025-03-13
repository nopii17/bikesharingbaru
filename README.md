# Dashboard Bike Sharing ✨

## Run steamlit app

```
streamlit run dashboard.py
```
README ASSIGNMENT by Novia Rahmadhani Purnomo
email : noviarp17@student.ub.ac.id
Cohort ID : mc006d5x2415

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

dashboard.py --> python untuk menjalankan streamlit (buka dengan Visual Studio Code)
impor data yang digunakan yaitu file newday.csv dan newhour.csv (dari lokal)

pada command prompt run 'streamlit run dashboard.py'

local host Ketika saya run :
 Local URL: http://localhost:8501
 Network URL: http://192.168.1.6:8501

kemudian run file python, apabila sudah benar akan muncul dashboard streamlit di chrome
