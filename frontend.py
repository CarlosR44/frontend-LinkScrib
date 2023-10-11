import streamlit as st


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

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "Login"

    if st.session_state.page == "Login":
        login()
    elif st.session_state.page == "Registro":
        register()
    elif st.session_state.page == "Inicio":
        home()

def login():
    st.title("Inicio de Sesión")
    username = st.text_input("Nombre de Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar Sesión"):
        # Verifica las credenciales (agrega tu lógica de autenticación aquí)
        if username == "usuario" and password == "contraseña":
            st.success("Inicio de Sesión Exitoso")
            Inicio_sucess = True
            if Inicio_sucess:
               st.session_state.page = "Extraer Características"
               st.experimental_rerun()
        else:
            st.error("Nombre de Usuario o Contraseña Incorrectos")

    # Enlace para ir a la página de registro
    if st.button("¿Aún no estás registrado?"):
        st.session_state.page = "Registro"

def register():
    # st.title("Registro")
    st.markdown('<label class="text-label">Nombre de usuario:</label>', unsafe_allow_html=True)
    username = st.text_input("", "", key="username")
    
    st.markdown('<label class="text-label">Contrasena:</label>', unsafe_allow_html=True)
    password = st.text_input("", type="password", key="password")
    
    st.markdown('<label class="text-label">Confirmar Contrasena:</label>', unsafe_allow_html=True)
    confirm_password = st.text_input("", type="password", key="confirm_password")
    
    register_button = '<button class="button-primary">Registrarse</button>'
    st.markdown(register_button, unsafe_allow_html=True)


    
# Pagina de inicio
def home():

    logo_path = "RACpeq.jpg"
    # logo_path = "RACsinfondo.jpg"
    # logo_path = "LogoRac.jpg"
    # logo_path = "OIG.M.jpg"

    col1, col2 = st.columns([0.1, 0.2], gap='small')

    with col1:
     st.image(logo_path, use_column_width=False)

    with col2:
     st.markdown('<h1 class="title">LinkScribe</h1>', unsafe_allow_html=True)

    # st.title("Clasificador de Links Web")

    st.sidebar.title("Menu")
    page = st.sidebar.radio("Selecciona una pagina:", ["Extraer Caracteristicas", "Lista de Links", "Login", "Registro"])

    if page == "Extraer Caracteristicas":
        extract_features()
    elif page == "Lista de Links":
        show_links()
    elif page == "Cerrar Sesión":
        st.write("Has cerrado sesión.")
        st.session_state.page ="Login"
        st.session_state.username = ""
 

def extract_features():
    # st.markdown('<div class="link-input-bar"><input type="text" placeholder="Ingresa un enlace"></div>', unsafe_allow_html=True)
    link = st.text_input("Ingresa el link:")
    st.write("")  # Espacio en blanco para separar los elementos
    
    green_button = '<button class="button-primary">Procesar</button>'
    # Variable de estado para controlar la visibilidad de la frase
    show_success_message = False
    
    if st.markdown(green_button, unsafe_allow_html=True):
        # Aquí puedes poner la lógica para procesar el enlace cuando se hace clic en el botón
        if show_success_message:
            st.success("Enlace procesado exitosamente")
        show_success_message = True
    
    # Aqua puedes implementar la lgica de extraccin de caractersticas

# Pigina para mostrar la lista de links con filtros
def show_links():
    st.markdown('<h2 style="color: white;">Filtrar por:</h2>', unsafe_allow_html=True)
    
    # Aplicar estilo al selectbox al hacer clic
    st.markdown('<style>.st-ef .st-e6.st-e7 .st-bm { background-color: #005500; color: white; }</style>', unsafe_allow_html=True)
    
    filter_option = st.selectbox("Filtrar por:", ["Nombre", "Fecha de Ingreso"])
    # Aqu puedes implementar la lgica de mostrar la lista de links y aplicar filtros

# Pgina de login
# def login():
    # # st.title("Login")
    # st.markdown('<label class="text-label">Nombre de usuario:</label>', unsafe_allow_html=True)
    # username = st.text_input("", "", key="username")
    # st.markdown('<label class="text-label">Contrasena:</label>', unsafe_allow_html=True)

    # password = st.text_input("", type="password", key="password")
    # # username = st.text_input("Nombre de usuario:")
    # # password = st.text_input("Contrasena:", type="password")
    # # login_button = st.button("Iniciar Sesion")
    # button_html = '<button class="button-primary">Iniciar Sesion</button>'
    # st.markdown(button_html, unsafe_allow_html=True)

    # # if login_button:
    #     # Aquo puedes implementar la logica de autenticacion

# def login():
#     st.title("Inicio de Sesión")
#     username = st.text_input("Nombre de Usuario")
#     password = st.text_input("Contraseña", type="password")

#     if st.button("Iniciar Sesión"):
#         # Verifica las credenciales (agrega tu lógica de autenticación aquí)
#         if username == "usuario" and password == "contraseña":
#             st.success("Inicio de Sesión Exitoso")
#             st.session_state.page = "Inicio"
#             st.session_state.username = username
#         else:
#             st.error("Nombre de Usuario o Contraseña Incorrectos")

#     # Enlace para ir a la página de registro
#     if st.button("¿Aún no estás registrado?"):
#         st.session_state.page = "Registro"

# Pogina de registro
# def register():
#     # st.title("Registro")
#     st.markdown('<label class="text-label">Nombre de usuario:</label>', unsafe_allow_html=True)
#     username = st.text_input("", "", key="username")
    
#     st.markdown('<label class="text-label">Contrasena:</label>', unsafe_allow_html=True)
#     password = st.text_input("", type="password", key="password")
    
#     st.markdown('<label class="text-label">Confirmar Contrasena:</label>', unsafe_allow_html=True)
#     confirm_password = st.text_input("", type="password", key="confirm_password")
    
#     register_button = '<button class="button-primary">Registrarse</button>'
#     st.markdown(register_button, unsafe_allow_html=True)


    # if register_button:
        # Aqui puedes implementar la logica de registro

if __name__ == "__main__":
    st.session_state.page = "Login"
    main()