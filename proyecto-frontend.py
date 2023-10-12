import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path
import pandas as pd
import plotly.express as px
from logup import sign_up, fetch_users

# st.write('<link rel="shortcut icon" href="RACpeqA.ico">', unsafe_allow_html=True)
st.set_page_config(
    page_title="RAC LinkScribe",
    page_icon="LogoRACA.ico",
    layout="centered",
    initial_sidebar_state="auto",
)

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown(
    """
<style>
/* Estilos para el botón */

.text-label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
    color: #ffffff;
    }


/* Espaciado entre los campos de entrada y los títulos */
.text-input {
    margin-top: 2px;
    }
.st-ef .st-e6.st-e7 .st-bm {

    background-color: #005500; /* Cambiar color de fondo al hacer clic */
    color: white; /* Cambiar color del texto al hacer clic */

    }

  /* Estilos para el contenedor de entrada de texto */
    .text-input-container {
        margin-bottom: 15px;
    }

    .button-primary {
        background-color: #008000;
        color: white;
        padding: 0.5rem 1rem;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    /* Estilos cuando el cursor pasa sobre el botón */
    .button-primary:hover {
        background-color: #0056b3; /* Cambia el fondo al pasar el cursor */
        color: #00FF00; /* Cambia el color de la letra al pasar el cursor */
    }

    /* Estilos para cambiar el fondo de la página */
    .stApp {
        background-color: #333333; /* Cambia el color de fondo a gris claro */
    }
    .title {
        color: #c9d0d3;
        margin-bottom: 80px; /* Cambia el color del título a azul */
    }

    .link-input-bar {
        background-color: #005500; /* Cambia el fondo a verde oscuro */
        padding: 10px; /* Añade espacio alrededor de la barra de entrada de texto */
        margin-top: -20px; /* Sube la barra de entrada de texto */
    }


    /* Estilos cuando el cursor pasa sobre el botón y cambia el fondo de la página */
    .button-primary:hover + body {
        background-color: #f0f0f0; /* Cambia el fondo de la página al pasar el cursor sobre el botón */
    }

    .stColumn > div {
    padding: 0px 10px; /* Ajusta el valor de padding según tu preferencia */
}
    </style>
    """,
    unsafe_allow_html=True
)

names = ["Carlos Reyes", "Rebeca Miller"]
usernames = ["Empanada", "bunuelo"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
                                    "sales_dashboard", "fgyuh", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login(":green[Sign In]", "main")

if authentication_status == False:
    st.error("Usuario o contrasena incorrecta")

if authentication_status == None:
    st.warning("Por favor ingrese su contrasena y usuario")

if not authentication_status:
        sign = st.sidebar.radio("Not registered yet?", ["Login", "Sing Up"])
        if sign == "Sing Up":
            sign_up()
        
if authentication_status:
# Pagina de inicio
 def home():

    logo_path = "RACpeqA.png"
    # logo_path = "RACsinfondo.jpg"
    # logo_path = "LogoRac.jpg"
    # logo_path = "OIG.M.jpg"

    col1, col2 = st.columns([0.1, 0.2], gap='small')

    with col1:
     st.image(logo_path, use_column_width=False)

    with col2:
     st.markdown('<h1 class="title">LinkScribe</h1>', unsafe_allow_html=True)

    # st.title("Clasificador de Links Web")
    st.sidebar.header(f'Welcome {username}')
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Select page:", ["Extract Links", "List of Links"])

    if page == "Extract Links":
        extract_features()
        
    elif page == "List of Links":
        show_links()
    authenticator.logout(":green[Logout]", "sidebar")

 def extract_features():
    link = st.text_input("Enter link:")
    
    green_button = '<button class="button-primary">Process :bulb:</button>'
    show_success_message = False
    show_image = False 
    
    if st.markdown(green_button, unsafe_allow_html=True):
        user_input_link = link

        if user_input_link:
            st.write(f"Enlace procesado... funciona Aljenadro??: {user_input_link}")
            boton = st.button("Save to Lists", key='Noregister')
            if boton:
               logo_path2 = "RACsinfondo.jpg"
               st.image(logo_path2, use_column_width=False)

        else:
            st.warning("Enter a Link")
    
    #la lgica de extraccin de caractersticas

# Pigina para mostrar la lista de links con filtros
 def show_links():
    # st.markdown('<h2 style="color: white;">Filtrar por:</h2>', unsafe_allow_html=True)
    
    #estilo al selectbox al hacer clic
    st.markdown('<style>.st-ef .st-e6.st-e7 .st-bm { background-color: #005500; color: white; }</style>', unsafe_allow_html=True)
    
    filter_option = st.selectbox("Filtrar por:", ["Filter by", "Category", "Entry date"])
    # lgica de mostrar la lista de links y aplicar filtros
    if filter_option == "Category":
        logo_path2 = "RACsinfondo.jpg"
        st.image(logo_path2, use_column_width=False)
    elif filter_option == "Entry date":
        logo_path = "LogoRac.jpg"
        st.image(logo_path, use_column_width=False)

 if __name__ == "__main__":
     home()
