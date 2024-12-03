import streamlit as st;
import loginController;

# Criação da página de login
def page_login():

    with st.container(border=True):
        st.markdown(
            """
            <div style="text-align: center; font-size: 24px; font-weight: bold;">
                Purchasing Challenge GM
            </div>
            """, 
            unsafe_allow_html=True
        )

        st.markdown(
        '''
        Esta aplicação é composta por duas páginas:

        - Página de Cosulta: Permite aos usuários visualizar os dados armazenados na base de dados. Além disso, por meio do botão "Actions", é possível editar ou excluir registros existentes.

        - Página de Inserção: Permite aos usuários adicionar novos registros à base de dados.
        '''
        )
        st.markdown("#### Enter your credentials")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):

            if loginController.authenticate_user(username,password) == True:
                st.session_state.authenticated = True
                st.success("Login successful!")
                st.rerun()

            else:
                st.error("Credentials are incorrect.")
                
    return st.session_state.authenticated
