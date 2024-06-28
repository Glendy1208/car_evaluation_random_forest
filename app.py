import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load('rf_model.pkl')

# Function to make predictions
def predict_evaluation(buying, maint, doors, persons, lug_boot, safety):
    data = {
        'buying': [buying],
        'maint': [maint],
        'doors': [doors],
        'persons': [persons],
        'lug_boot': [lug_boot],
        'safety': [safety]
    }
    df = pd.DataFrame(data)
    prediction = model.predict(df)[0]
    return prediction

# Sidebar navigation
st.sidebar.title('Glendy (22-076)')
page = st.sidebar.radio('Navigasi', ['Informasi', 'Inputan',])

# Page content based on selection
if page == 'Informasi':
    st.title('Sistem Penilaian Kelayakan Pembelian Mobil Menggunakan Metode Random Forest')
    st.markdown("""
    Aplikasi ini dibuat untuk membanutu calon pembeli mobil untuk mengevaluasi mobil yang akan dibeli layak atau tidak untuk dibeli 
    """)

    st.subheader('Source Code Aplikasi')
    st.write('https://github.com/Glendy1208/car_evaluation_random_forest')

    st.header('Keterangan Hasil Evaluasi')

    st.subheader('Tidak Layak Dibeli')
    st.markdown("""
    **Deskripsi:**  Mobil tidak direkomendasikan untuk dibeli, didasarkan karena faktor seperti harga yang terlalu tinggi, biaya perawatan yang tinggi, keamanan yang rendah, atau kombinasi dari faktor-faktor tersebut.
    """)
    st.subheader('Cukup Layak Dibeli')
    st.markdown("""
    **Deskripsi:** Mobil cukup direkomendasikan untuk dibeli, memenuhi standar minimum yang diinginkan dalam hal harga, perawatan, kapasitas, ukuran bagasi, dan keamanan.
    """)
    st.subheader('Layak Dibeli')
    st.markdown("""
    **Deskripsi:** Mobil direkomendasikan untuk dibeli, memiliki fitur yang lebih baik dari standar minimum, dengan keseimbangan yang baik antara harga, perawatan, kapasitas, ukuran bagasi, dan keamanan.
    """)
    st.subheader('Sangat Layak Dibeli')
    st.markdown("""
    **Deskripsi:** Mobil sangat direkomendasikan untuk dibeli, melebihi standar dalam hampir semua aspek termasuk harga, perawatan, kapasitas, ukuran bagasi, dan keamanan.
    """)

    st.header('Keterangan Inputan')
    
    st.subheader('Harga Pembelian Mobil')
    st.markdown("""
    **Deskripsi:** Mengindikasikan harga pembelian mobil.
    - vhigh (very high): Harga mobil sangat mahal, Lebih dari Rp 500 juta.
    - high: Harga mobil mahal, berkisar antara Rp 300 juta - Rp 500 juta.
    - med (medium): Harga mobil sedang, berkisar antara Rp 150 juta - Rp 300 juta.
    - low: Harga mobil murah, berkisar antara Rp 50 juta - Rp 150 juta.
    """)

    st.subheader('Biaya Perawatan')
    st.markdown("""
    **Deskripsi:** Mengindikasikan biaya perawatan mobil.
    - vhigh (very high): Biaya perawatan sangat tinggi, Lebih dari Rp 10 juta per tahun.
    - high: Biaya perawatan tinggi, berkisar antara Rp 7 juta - Rp 10 juta per tahun.
    - med (medium): Biaya perawatan sedang, berkisar antara Rp 4 juta - Rp 7 juta per tahun.
    - low: Biaya perawatan rendah, berkisar antara Rp 1 juta - Rp 4 juta per tahun.
    """)

    st.subheader('Jumlah pintu mobil')
    st.markdown("""
    **Deskripsi:** Mengindikasikan jumlah pintu mobil.
    - 2: Mobil dengan 2 pintu.
    - 3: Mobil dengan 3 pintu.
    - 4: Mobil dengan 4 pintu.
    - 5more: Mobil dengan 5 atau lebih pintu.
    """)

    st.subheader('Jumlah maksimal penumpang')
    st.markdown("""
    **Deskripsi:** Mengindikasikan kapasitas tempat duduk mobil.
    - 2: Kapasitas untuk 2 orang.
    - 4: Kapasitas untuk 4 orang.
    - more: Kapasitas untuk lebih dari 4 orang.
    """)

    st.subheader('Ukuran bagasi')
    st.markdown("""
    **Deskripsi:** Mengindikasikan ukuran bagasi mobil.
    - small:
        - **Deskripsi:** Ukuran bagasi kecil, cocok untuk kebutuhan sehari-hari.
        - **Kapasitas:** Sekitar 150 - 300 liter.
        - **Contoh:** Cukup untuk beberapa tas belanja kecil atau satu koper kecil. 
    - med (medium):
        - **Deskripsi:** Ukuran bagasi sedang, cocok untuk kebutuhan keluarga kecil.
        - **Kapasitas:** Sekitar 300 - 500 liter.
        - **Contoh:** Cukup untuk beberapa koper ukuran sedang atau perlengkapan berkemah.
    - big:
        - **Deskripsi:** Ukuran bagasi besar, ideal untuk keluarga besar atau perjalanan panjang.
        - **Kapasitas:** Lebih dari 500 liter.
        - **Contoh:** Cukup untuk beberapa koper besar atau perlengkapan perjalanan panjang.
    """)

    st.subheader('Keselamatan')
    st.markdown("""
    **Deskripsi:** Mengindikasikan tingkat keamanan mobil.
    **Kategori:**
    - Rendah:
        - **Deskripsi:** Tingkat keamanan rendah, dengan fitur keselamatan dasar.
        - Sabuk pengaman standar.
        - Sistem rem standar.
    - Sedang:
        - **Deskripsi:** Tingkat keamanan sedang, dengan tambahan fitur keselamatan.
        - Sabuk pengaman standar.
        - Sistem rem anti-lock (ABS).
        - Airbag untuk pengemudi dan penumpang depan.
        - Kontrol stabilitas elektronik (ESC).
    - Tinggi:
        - **Deskripsi:** Tingkat keamanan tinggi, dengan fitur keselamatan canggih dan lengkap.
        - Sabuk pengaman standar.
        - Sistem rem anti-lock (ABS).
        - Airbag untuk pengemudi, penumpang depan, dan airbag samping.
        - Kontrol stabilitas elektronik (ESC).
        - Sistem peringatan tabrakan depan.
        - Sistem pengereman darurat otomatis.
        - Kamera belakang atau sistem pemantauan blind spot.
    """)

elif page == 'Inputan':
    st.title('Form Inputan')

    # Create dropdowns for user input
    buying = st.selectbox('Harga', options=[0, 1, 2, 3], format_func=lambda x: [' Rp 50 juta - Rp 150 juta', 'Rp 150 juta - Rp 300 juta', 'Rp 300 juta - Rp 500 juta.', '>  Rp 500 juta'][x])
    maint = st.selectbox('Biaya Perawatan Pertahun', options=[0, 1, 2, 3], format_func=lambda x: ['Rp 1 juta - Rp 4 juta', 'Rp 4 juta - Rp 7 juta', 'Rp 7 juta - Rp 10 juta', '> Rp 10 juta '][x])
    doors = st.selectbox('Pintu', options=[0, 1, 2, 3], format_func=lambda x: ['2', '3', '4', '> 5'][x])
    persons = st.selectbox('Jumlah Max Penumpang', options=[0, 1, 2], format_func=lambda x: ['2', '4', '> 4'][x])
    lug_boot = st.selectbox('Ukuran Bagasi', options=[0, 1, 2], format_func=lambda x: ['150 - 300 liter', '300 - 500 liter', '> 500 liter'][x])
    safety = st.selectbox('Tingkat Keselamatan Penumpang', options=[0, 1, 2], format_func=lambda x: ['Rendah', 'Sedang', 'Tinggi'][x])

    # Predict button
    if st.button('Predict'):
        result = predict_evaluation(buying, maint, doors, persons, lug_boot, safety)
        st.write(f'Hasil Evaluasi Mobil : {["Tidak Layak Dibeli", "Masih Layak Dibeli", "Layak Dibeli", "Sangat Layak Dibeli"][result]}')
