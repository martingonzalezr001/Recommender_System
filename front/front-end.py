import streamlit as st

def special_internal_function(value):
    return value


st.markdown(
    f"""<h1 style='text-align: center; font-size: 28px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;'>¡Bienvenido a la plataforma de ideas de proyectos!</h1>""",
    unsafe_allow_html=True,
)
with st.form("my_form"):    
   
    label = ""
    #options = ["Front-End", "Back-End", "Database", "Authentication", "E-Commerce" ,"CD/CI & DevOps", "Message Service", "Search Engine" ,"Media & Storage"]
    idea = st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None,placeholder="¿Cuál es tu idea de proyecto?", disabled=False, label_visibility="visible")
    #check_form = st.radio(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, horizontal=False, captions=None, label_visibility="visible")

    submitted = st.form_submit_button(label="Enviar", help=None, on_click=None, args=None, kwargs=None, type="secondary", icon=None, disabled=False, use_container_width=False)

    # Every form must have a submit button.
    
    if submitted:
        st.write(idea)
    
# Bloque Front
checkbox_front = st.checkbox("Front-End", key="front-End")
if checkbox_front:

    # Crear columnas
    col_escalabilidad_front, col_nivel_uso_front, col_coste_front, col_seguridad_front = st.columns(4)
    with col_escalabilidad_front:
        escalabilidad_front = st.selectbox("Escalabilidad:", ["Alta", "Media", "Baja","N/A"], key="escalabilidad_front")
    with col_nivel_uso_front:
        nivel_uso_front = st.selectbox("Nivel de uso:", ["Sencillo", "Intermedio", "Difícil", "N/A"], key="nivel_uso_front")

    with col_coste_front:
        coste_front = st.selectbox("Coste:", ["Gratuito", "De pago", "Freemium", "N/A"], key="coste_front")

    with col_seguridad_front:
        seguridad_front = st.selectbox("Seguridad:", ["Alta", "Media", "Básica", "N/A"], key="seguridad_front") 

# Bloque Back
checkbox_back = st.checkbox("Back-End", key="back-End") 
if checkbox_back:
    # Crear columnas
    col_escalabilidad_back, col_nivel_uso_back, col_coste_back, col_seguridad_back = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_back:
        escalabilidad_back = st.selectbox("Escalabilidad:", ["Alta", "Media", "Baja","N/A"], key="escalabilidad_back")
    with col_nivel_uso_back:
        nivel_uso_back = st.selectbox("Nivel de uso:", ["Sencillo", "Intermedio", "Difícil", "N/A"], key="nivel_uso_back")

    with col_coste_back:
        coste_back = st.selectbox("Coste:", ["Gratuito", "De pago", "Freemium", "N/A"], key="coste_back")

    with col_seguridad_back:
        seguridad_back = st.selectbox("Seguridad:", ["Alta", "Media", "Básica", "N/A"], key="seguridad_back")   


# Bloque Database
checkbox_database = st.checkbox("Database", key="database")
if checkbox_database:
    # Crear columnas
    col_escalabilidad_database, col_nivel_uso_database, col_coste_database, col_seguridad_database = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_database:
        escalabilidad_database = st.selectbox("Escalabilidad:", ["Alta", "Media", "Baja","N/A"], key="escalabilidad_database")
    with col_nivel_uso_database:
        nivel_uso_database = st.selectbox("Nivel de uso:", ["Sencillo", "Intermedio", "Difícil", "N/A"], key="nivel_uso_database")

    with col_coste_database:
        coste_database = st.selectbox("Coste:", ["Gratuito", "De pago", "Freemium", "N/A"], key="coste_database")

    with col_seguridad_database:
        seguridad_database = st.selectbox("Seguridad:", ["Alta", "Media", "Básica", "N/A"], key="seguridad_database")  


# Bloque Authentication
checkbox_auth = st.checkbox("Authentication", key="authentication")
if checkbox_auth:
    # Crear columnas
    col_escalabilidad_auth, col_nivel_uso_auth, col_coste_auth, col_seguridad_auth = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_auth:
        escalabilidad_auth = st.selectbox("Escalabilidad:", ["Alta", "Media", "Baja","N/A"], key="escalabilidad_auth")
    with col_nivel_uso_auth:
        nivel_uso_auth = st.selectbox("Nivel de uso:", ["Sencillo", "Intermedio", "Difícil", "N/A"], key="nivel_uso_auth")

    with col_coste_auth:
        coste_auth = st.selectbox("Coste:", ["Gratuito", "De pago", "Freemium", "N/A"], key="coste_auth")

    with col_seguridad_auth:
        seguridad_auth = st.selectbox("Seguridad:", ["Alta", "Media", "Básica", "N/A"], key="seguridad_auth")


# Bloque E-commerce
checkbox_ecommerce = st.checkbox("E-Commerce", key="e-Commerce")
if checkbox_ecommerce:
    # Crear columnas
    col_escalabilidad_ecommerce, col_nivel_uso_ecommerce, col_coste_ecommerce, col_seguridad_ecommerce = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_ecommerce:
        escalabilidad_ecommerce = st.selectbox("Escalabilidad:", ["Alta", "Media", "Baja","N/A"], key="escalabilidad_ecommerce")
    with col_nivel_uso_ecommerce:
        nivel_uso_ecommerce = st.selectbox("Nivel de uso:", ["Sencillo", "Intermedio", "Difícil", "N/A"], key="nivel_uso_ecommerce")

    with col_coste_ecommerce:
        coste_ecommerce = st.selectbox("Coste:", ["Gratuito", "De pago", "Freemium", "N/A"], key="coste_ecommerce")

    with col_seguridad_ecommerce:
        seguridad_ecommerce = st.selectbox("Seguridad:", ["Alta", "Media", "Básica", "N/A"], key="seguridad_ecommerce")


# Bloque CloudHosting
checkbox_cloud_hosting = st.checkbox("CloudHosting", key="cloud_hosting")
if checkbox_cloud_hosting:
    # Crear columnas
    col_escalabilidad_cloud_hosting, col_nivel_uso_cloud_hosting, col_coste_cloud_hosting, col_seguridad_cloud_hosting = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_cloud_hosting:
        escalabilidad_cloud_hosting = st.selectbox("Escalabilidad:", ["Alta", "Media", "Baja","N/A"], key="escalabilidad_cloud_hosting")
    with col_nivel_uso_cloud_hosting:
        nivel_uso_cloud_hosting = st.selectbox("Nivel de uso:", ["Sencillo", "Intermedio", "Difícil", "N/A"], key="nivel_uso_cloud_hosting")

    with col_coste_cloud_hosting:
        coste_cloud_hosting = st.selectbox("Coste:", ["Gratuito", "De pago", "Freemium", "N/A"], key="coste_cloud_hosting")

    with col_seguridad_cloud_hosting:
        seguridad_cloud_hosting = st.selectbox("Seguridad:", ["Alta", "Media", "Básica", "N/A"], key="seguridad_cloud_hosting")

# Bloque CD/CI & DevOps
checkbox_cdci_devops = st.checkbox("CD/CI & DevOps", key="cd/ci_devOps")
if checkbox_cdci_devops:
    # Crear columnas
    col_escalabilidad_cdci_devops, col_nivel_uso_cdci_devops, col_coste_cdci_devops, col_seguridad_cdci_devops = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_cdci_devops:
        escalabilidad_cdci_devops = st.selectbox("Escalabilidad:", ["Alta", "Media", "Baja","N/A"], key="escalabilidad_cdci_devops")
    with col_nivel_uso_cdci_devops:
        nivel_uso_cdci_devops = st.selectbox("Nivel de uso:", ["Sencillo", "Intermedio", "Difícil", "N/A"], key="nivel_uso_cdci_devops")

    with col_coste_cdci_devops:
        coste_cdci_devops = st.selectbox("Coste:", ["Gratuito", "De pago", "Freemium", "N/A"], key="coste_cdci_devops")

    with col_seguridad_cdci_devops:
        seguridad_ecommerce = st.selectbox("Seguridad:", ["Alta", "Media", "Básica", "N/A"], key="seguridad_cdci_devops") 

# Bloque Message Service
checkbox_msg = st.checkbox("Message Service", key="message_service")
if checkbox_msg:
    # Crear columnas
    col_escalabilidad_msg, col_nivel_uso_msg, col_coste_msg, col_seguridad_msg = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_msg:
        escalabilidad_msg = st.selectbox("Escalabilidad:", ["Alta", "Media", "Baja","N/A"], key="escalabilidad_msg")
    with col_nivel_uso_msg:
        nivel_uso_msg = st.selectbox("Nivel de uso:", ["Sencillo", "Intermedio", "Difícil", "N/A"], key="nivel_uso_msg")

    with col_coste_msg:
        coste_msg = st.selectbox("Coste:", ["Gratuito", "De pago", "Freemium", "N/A"], key="coste_msg")

    with col_seguridad_msg:
        seguridad_msg = st.selectbox("Seguridad:", ["Alta", "Media", "Básica", "N/A"], key="seguridad_msg")

# Bloque Search Engine
checkbox_search_engine = st.checkbox("Search Engine", key="search_engine") 
if checkbox_search_engine:
    # Crear columnas
    col_escalabilidad_search_engine, col_nivel_uso_search_engine, col_coste_search_engine, col_seguridad_search_engine = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_search_engine:
        escalabilidad_search_engine = st.selectbox("Escalabilidad:", ["Alta", "Media", "Baja","N/A"], key="escalabilidad_search_engine")
    with col_nivel_uso_search_engine:
        nivel_uso_search_engine = st.selectbox("Nivel de uso:", ["Sencillo", "Intermedio", "Difícil", "N/A"], key="nivel_uso_search_engine")

    with col_coste_search_engine:
        coste_search_engine = st.selectbox("Coste:", ["Gratuito", "De pago", "Freemium", "N/A"], key="coste_search_engine")

    with col_seguridad_search_engine:
        seguridad_search_engine = st.selectbox("Seguridad:", ["Alta", "Media", "Básica", "N/A"], key="seguridad_search_engine")

# Bloque media_storage

checkbox_media_storage = st.checkbox("Media Storage", key="media_storage") 
if checkbox_media_storage:
    # Crear columnas
    col_escalabilidad_media_storage, col_nivel_uso_media_storage, col_coste_media_storage, col_seguridad_media_storage = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_media_storage:
        escalabilidad_media_storage = st.selectbox("Escalabilidad:", ["Alta", "Media", "Baja","N/A"], key="escalabilidad_media_storage")
    with col_nivel_uso_media_storage:
        nivel_uso_media_storage = st.selectbox("Nivel de uso:", ["Sencillo", "Intermedio", "Difícil", "N/A"], key="nivel_uso_media_storage")

    with col_coste_media_storage:
        coste_media_storage = st.selectbox("Coste:", ["Gratuito", "De pago", "Freemium", "N/A"], key="coste_media_storage")

    with col_seguridad_media_storage:
        seguridad_media_storage = st.selectbox("Seguridad:", ["Alta", "Media", "Básica", "N/A"], key="seguridad_media_storage")
