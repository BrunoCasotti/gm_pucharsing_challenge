import streamlit as st
import forecastController
import pandas as pd
from streamlit_modal import Modal;

# Inicializa as modais utilizadas na tela
modal_forecast_delete = Modal(key="modal_forecast_delete", title="Delete record Forecast")
modal_forecast_update = Modal(key="modal_forecast_update", title="Update record Forecast")

# Header
st.header("Purchase Forecast", divider="gray")

# Popover com botões de delete e update
with st.popover("Actions"):
    delete_button = st.button("Delete")
    update_button = st.button("Update")

    if delete_button:
        st.write("Você clicou em 'Delete'.")
        modal_forecast_delete.open()

    if update_button:
        st.write("Você clicou em 'Update'.")
        modal_forecast_update.open()

st.write("")

# Dataframe 
columns = forecastController.read_column_forecast()
data = forecastController.read_all_forecast()

df_forecast = pd.DataFrame(
    data, columns=columns
)

st.dataframe(df_forecast.set_index(df_forecast.columns[0]),height=700)

# Criação da modal de deleção
if modal_forecast_delete.is_open():

    with modal_forecast_delete.container():

        st.session_state["modal_open"] = True

        st.write("Which id do you want to delete? Enter to continue")

        input_id_delete_forecast = st.text_input(label="Id")

        if not input_id_delete_forecast.strip():
            st.write("")
        else:
            df_delete_forecast = forecastController.read_forecast_by_id(input_id_delete_forecast)
            df_delete_forecast = pd.DataFrame(
            forecastController.read_forecast_by_id(input_id_delete_forecast), columns=columns)
            st.write(df_delete_forecast.set_index(df_delete_forecast.columns[0]))
            st.write("Do you want to delete this record?")
            
            if st.button("Delete",key='btn_delete'):
                forecastController.delete_forecast(input_id_delete_forecast)
                st.rerun()
                st.success("Record deleted!")

# Criação da modal de alteração
if modal_forecast_update.is_open():

    with modal_forecast_update.container():

        st.write("Which id do you want to update? Enter to continue")

        input_id_delete_forecast = st.text_input(label="Id")


        if not input_id_delete_forecast.strip():
            st.write("")
        else:
            df_delete_forecast = forecastController.read_forecast_by_id(input_id_delete_forecast)
            df_delete_forecast = pd.DataFrame(
            forecastController.read_forecast_by_id(input_id_delete_forecast), columns=columns)
            st.write(df_delete_forecast.set_index(df_delete_forecast.columns[0]))
            st.write("Do you want to update this record?")
            
            if st.button("Update",key='btn_update'):
                session_id = st.session_state["id"] = input_id_delete_forecast
                st.switch_page("forecastInsert.py")





