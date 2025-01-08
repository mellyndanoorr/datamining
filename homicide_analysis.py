import pickle 
import streamlit as st

model = pickle.load(open('Homicide_analysis.sav', 'rb'))

st.title('Homicide Analysis')


# Input fitur yang dibutuhkan
count = st.number_input(' Jumlah Kasus Pembunuhan', min_value=0, value=0, step=1)
year = st.number_input(' Tahun Kejadian', min_value=2000, max_value=2025, value=2020, step=1)


# Variabel untuk prediksi
predict = ''

# Tombol prediksi
if st.button('Prediksi Tingkat pembunuhan'):
    # Lakukan prediksi
    predict = model.predict([[count, year]])
    st.write('Estimasi Tingkat pembuhan:', round(predict[0], 2))



#LANGKAH : 
#1. pip install streamlit 
#2. python homicide_analysis.py
#3. streamlit run homicide_analysis.py ( menjalankan aplikasi nya )
