import streamlit as st;
import forecastController;
import time;

# Recupera o id para alteração
id_update = st.session_state.get("id", None)

# Inicialização da variável
id_recovered = None

# Verificação para saber se a chamada é para insert ou update
if id_update is not None:
    st.header("Update", divider="gray")
    id_recovered = forecastController.read_forecast_by_id(id_update)[0][0]
else:
    st.header("Register", divider="gray")

with st.container(height=800, border=0):

    with st.form(key="forecast_insert", clear_on_submit=True):

        list_year = [2024, 2025, 2026]

        if id_recovered == None:
            input_buyer_code = st.text_input(label="Buyer code")
            input_team_code = st.number_input(label="Team code",step=1)
            input_region = st.text_input(label="Region")
            input_piece_code = st.text_input(label="Piece code")
            input_description = st.text_input(label="Description")
            input_sup_country = st.text_input(label="Sup Country")
            input_sup_code = st.number_input(label="Sup Code",step=1)
            input_year = st.selectbox(label="Year",
                                        options=list_year,
                                        index=None,
                                        placeholder="Choose year")
            input_price = st.number_input(label="Price")
            input_volume = st.number_input(label="Volume",step=1)
            
        else:
            input_buyer_code = st.text_input(label="Buyer code",
                                            value= forecastController.read_forecast_by_id(id_update)[0][1])
            input_team_code = st.number_input(label="Team code",
                                            value= forecastController.read_forecast_by_id(id_update)[0][2])
            input_region = st.text_input(label="Region",
                                        value= forecastController.read_forecast_by_id(id_update)[0][3])
            input_piece_code = st.text_input(label="Piece code",
                                            value= forecastController.read_forecast_by_id(id_update)[0][4])
            input_description = st.text_input(label="Description",
                                            value= forecastController.read_forecast_by_id(id_update)[0][5])
            input_sup_country = st.text_input(label="Sup Country",
                                            value= forecastController.read_forecast_by_id(id_update)[0][6])
            input_sup_code = st.number_input(label="Sup Code",
                                            value= forecastController.read_forecast_by_id(id_update)[0][7])
            input_year = st.selectbox(label="Year",
                                        options=list_year,
                                        index=list_year.index(forecastController.read_forecast_by_id(id_update)[0][8]))
            input_price = st.number_input(label="Price",
                                        value= forecastController.read_forecast_by_id(id_update)[0][9])
            input_volume = st.number_input(label="Volume",
                                        value= forecastController.read_forecast_by_id(id_update)[0][10])
            
        input_button_submit = st.form_submit_button("Submit")

# Botão de submit 

    if input_button_submit:
        errors = []

# Verificação de erros no preenchimento
        if not input_buyer_code.strip():
            errors.append("Buyer code is required.")
        if input_team_code == 0:
            errors.append("Team code is required.")
        if not input_region.strip():
            errors.append("Region is required.")
        if not input_piece_code.strip():
            errors.append("Piece code is required.")
        if not input_description.strip():
            errors.append("Description is required.")
        if not input_sup_country.strip():
            errors.append("Sup country is required.")
        if input_sup_code == 0:
            errors.append("Sup code is required.")
        if input_year == None:
            errors.append("Please select a valid year.")
        if input_price <= 0:
            errors.append("Price must be greater than 0.")
        if input_volume <= 0:
            errors.append("Volume must be greater than 0.")

        if errors:
            for error in errors:
                st.error(error)
        else:
            if id_recovered == None:
                forecastController.insert_forecast(input_buyer_code, input_team_code, input_region, 
                                                input_piece_code, input_description, input_sup_country, 
                                                input_sup_code, input_year, input_price, input_volume)
            else:
                forecastController.update_forecast(id_update,input_buyer_code, input_team_code, input_region, 
                                                input_piece_code, input_description, input_sup_country, 
                                                input_sup_code, input_year, input_price, input_volume)
                
                st.success("Forecast submitted successfully!")
                del st.session_state["id"]
                time.sleep(1)
                st.switch_page("forecastConsult.py")
                st.rerun()

            st.success("Forecast submitted successfully!")
        