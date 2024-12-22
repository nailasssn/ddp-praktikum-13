import streamlit as st


# Side bar direktory
dashboard = st.Page("./fitur/dashboard.py", title="Dashboard")
nabung = st.Page("./fitur/nabung.py", title="Nabung")
penarikan = st.Page("./fitur/penarikan.py", title="Penarikan")

pg = st.navigation(
    {
        "Menu Utama":[dashboard], #""(key), [](value)
        "Transaksi":[nabung, penarikan],
    }
)

if "jumlah" not in st.session_state:
    st.session_state['jumlah'] = []

# menjalankan navigasi
pg.run()
