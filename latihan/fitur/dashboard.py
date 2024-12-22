import streamlit as st

st.title("Halaman Dashboard")

# fungsi untuk menghitung dan menyimpan total nabung
def total():
    total_nabung = sum(t['jumlah'] for t in st.session_state ['jumlah'] if t['Tipe'] == 'Menabung')

    return f'Total Nabung Anda {total_nabung}'

st.write(total())