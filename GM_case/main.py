import streamlit as st;
from login import page_login;

# Verifica se o usuário está logado
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

st.set_page_config(page_title="Purchase Challenge GM", layout="wide")

# Caso não esteja, manda para a pagina de login
if not st.session_state.authenticated:
    page_login()

else:

#Criação da main page
    ForecastInsert_page = st.Page(
        page="forecastInsert.py",
        title="Register"
    )

    forecastConsult_page = st.Page(
        page="forecastConsult.py",
        title="Consult",
        default=True
    )


    with st.sidebar:

        pg = st.navigation(
            {
                "Forecast": [forecastConsult_page, ForecastInsert_page]
            }
        )

         # Botão de Logout
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.rerun()

    pg.run()

