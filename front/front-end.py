import streamlit as st
import pandas as pd




urls_list = ["../data/front-end.csv", "../data/back-end.csv", "../data/database.csv", "../data/auth.csv", "../data/ecommerce.csv", "../data/cloudhosting.csv", "../data/cicd devops.csv", "../data/message.csv", "../data/search engine.csv", "../data/media storage.csv"]


def special_internal_function(value):
    return value


# Ejecuto esta funcion para que el modelo no gaste tokens leyendo todos los datasets en cada peticion
def filter_data(ar1,ar2):

    # Recorro el primer array
    for i in range(len(ar1)):


        for i in range(len(ar2)):
            # Para que cuando se acabe el primer array no de error
            if i < len(ar1):
                # Aquí accedo a los valores de los diccionarios para poder compararlo con el string primer array
                for key, value in ar2[i].items():

                    # Comparo la clave del diccionario con el string del primer array
                    if ar1[i] == key:
                        value = True
                        # Se iguala a True para cuando haya que hacer el filtrado
                        ar2[i] = {key:value}
            else:
                break
 

    return ar2



def get_data_filtered(arUrl, arParameter):
    data_to_read = []
    # La data que le pasemos finalmente al modelo

    for h in arUrl:
        for i in range(len(arParameter)):

            arParameter[i] = arParameter[i].lower()
            if arParameter[i] in h:
                st.write("Parametro a comparar: " + arParameter[i])
                st.write("Url a comparar: " + h)
                data_to_read.append(h)
            
    return data_to_read

def read_data(data_to_read):
    data = []
    for i in range(len(data_to_read)):
        data.append(pd.read_csv(data_to_read[i]))
    return data

    



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

    subparameter_list = []
    checkbox_list = []
    dataset_list = []
    dataset_prelist = [{"Front-End":False}, {"Back-End":False}, {"Database":False}, {"Auth":False}, {"Ecommerce":False}, {"CloudHosting":False}, {"Ci CD DevOps":False}, {"Message":False}, {"Search Engine":False}, {"Media Storage":False}]
    

    # Bloque Front
checkbox_front = st.checkbox("Front-End", key="front-End")
if checkbox_front:

    # Crear columnas
    col_escalabilidad_front, col_nivel_uso_front, col_coste_front, col_seguridad_front = st.columns(4)
    with col_escalabilidad_front:
        escalabilidad_front = st.selectbox("Escalabilidad:", ["N/A", "Alta", "Media", "Baja"], key="escalabilidad_front")
    with col_nivel_uso_front:
        nivel_uso_front = st.selectbox("Nivel de uso:", ["N/A", "Sencillo", "Intermedio", "Difícil"], key="nivel_uso_front")

    with col_coste_front:
        coste_front = st.selectbox("Coste:", ["N/A", "Gratuito", "De pago", "Freemium"], key="coste_front")

    with col_seguridad_front:
        seguridad_front = st.selectbox("Seguridad:", ["N/A", "Alta", "Media", "Básica"], key="seguridad_front")
    
    
    front_list = [{"Escalabilidad":escalabilidad_front},{ "Nivel de Uso":nivel_uso_front}, {"Coste":coste_front}, {"Seguridad":seguridad_front}] 
    subparameter_list.append(front_list)
    checkbox_list.append({"Front-End":checkbox_front})


# Bloque Back
checkbox_back = st.checkbox("Back-End", key="back-End") 
if checkbox_back:
    # Crear columnas
    col_escalabilidad_back, col_nivel_uso_back, col_coste_back, col_seguridad_back = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_back:
        escalabilidad_back = st.selectbox("Escalabilidad " , ["N/A", "Alta", "Media", "Baja"], key="escalabilidad_back")
    with col_nivel_uso_back:
        nivel_uso_back = st.selectbox("Nivel de uso:", ["N/A", "Sencillo", "Intermedio", "Difícil"], key="nivel_uso_back")

    with col_coste_back:
        coste_back = st.selectbox("Coste:", ["N/A", "Gratuito", "De pago", "Freemium"], key="coste_back")

    with col_seguridad_back:
        seguridad_back = st.selectbox("Seguridad:", ["N/A", "Alta", "Media", "Básica"], key="seguridad_back")

    back_list = [{"Escalabilidad":escalabilidad_back},{ "Nivel de Uso":nivel_uso_back}, {"Coste":coste_back}, {"Seguridad":seguridad_back}] 
    subparameter_list.append(back_list)
    checkbox_list.append({"Back-End":checkbox_back})

# Bloque Database
checkbox_database = st.checkbox("Database", key="database")
if checkbox_database:
    # Crear columnas
    col_escalabilidad_database, col_nivel_uso_database, col_coste_database, col_seguridad_database = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_database:
        escalabilidad_database = st.selectbox("Escalabilidad:", ["N/A", "Alta", "Media", "Baja"], key="escalabilidad_database")
    with col_nivel_uso_database:
        nivel_uso_database = st.selectbox("Nivel de uso:", ["N/A", "Sencillo", "Intermedio", "Difícil"], key="nivel_uso_database")

    with col_coste_database:
        coste_database = st.selectbox("Coste:", ["N/A", "Gratuito", "De pago", "Freemium"], key="coste_database")

    with col_seguridad_database:
        seguridad_database = st.selectbox("Seguridad:", ["N/A", "Alta", "Media", "Básica"], key="seguridad_database")

    database_list = [{"Escalabilidad":escalabilidad_database},{ "Nivel de Uso":nivel_uso_database}, {"Coste":coste_database}, {"Seguridad":seguridad_database}]  
    subparameter_list.append(database_list)
    checkbox_list.append({"Database":checkbox_database})

# Bloque Authentication
checkbox_auth = st.checkbox("Authentication", key="authentication")
if checkbox_auth:
    # Crear columnas
    col_escalabilidad_auth, col_nivel_uso_auth, col_coste_auth, col_seguridad_auth = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_auth:
        escalabilidad_auth = st.selectbox("Escalabilidad:", ["N/A", "Alta", "Media", "Baja"], key="escalabilidad_auth")
    with col_nivel_uso_auth:
        nivel_uso_auth = st.selectbox("Nivel de uso:", ["N/A", "Sencillo", "Intermedio", "Difícil"], key="nivel_uso_auth")

    with col_coste_auth:
        coste_auth = st.selectbox("Coste:", ["N/A", "Gratuito", "De pago", "Freemium"], key="coste_auth")

    with col_seguridad_auth:
        seguridad_auth = st.selectbox("Seguridad:", ["N/A", "Alta", "Media", "Básica"], key="seguridad_auth")

    auth_list = [{"Escalabilidad":escalabilidad_auth},{ "Nivel de Uso":nivel_uso_auth}, {"Coste":coste_auth}, {"Seguridad":seguridad_auth}]
    subparameter_list.append(auth_list)
    checkbox_list.append({"Auth":checkbox_auth})

# Bloque E-commerce
checkbox_ecommerce = st.checkbox("E-Commerce", key="e-Commerce")
if checkbox_ecommerce:
    # Crear columnas
    col_escalabilidad_ecommerce, col_nivel_uso_ecommerce, col_coste_ecommerce, col_seguridad_ecommerce = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_ecommerce:
        escalabilidad_ecommerce = st.selectbox("Escalabilidad :", ["N/A", "Alta", "Media", "Baja"], key="escalabilidad_ecommerce")
    with col_nivel_uso_ecommerce:
        nivel_uso_ecommerce = st.selectbox("Nivel de uso:", ["N/A", "Sencillo", "Intermedio", "Difícil"], key="nivel_uso_ecommerce")

    with col_coste_ecommerce:
        coste_ecommerce = st.selectbox("Coste:", ["N/A", "Gratuito", "De pago", "Freemium"], key="coste_ecommerce")

    with col_seguridad_ecommerce:
        seguridad_ecommerce = st.selectbox("Seguridad:", ["N/A", "Alta", "Media", "Básica"], key="seguridad_ecommerce")

    ecommerce_list = [{"Escalabilidad":escalabilidad_ecommerce},{ "Nivel de Uso":nivel_uso_ecommerce}, {"Coste":coste_ecommerce}, {"Seguridad":seguridad_ecommerce}]
    subparameter_list.append(ecommerce_list)
    checkbox_list.append({"Ecommerce":checkbox_ecommerce})

# Bloque CloudHosting
checkbox_cloud_hosting = st.checkbox("CloudHosting", key="cloud_hosting")
if checkbox_cloud_hosting:
    # Crear columnas
    col_escalabilidad_cloud_hosting, col_nivel_uso_cloud_hosting, col_coste_cloud_hosting, col_seguridad_cloud_hosting = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_cloud_hosting:
        escalabilidad_cloud_hosting = st.selectbox("Escalabilidad:", ["N/A", "Alta", "Media", "Baja"], key="escalabilidad_cloud_hosting")
    with col_nivel_uso_cloud_hosting:
        nivel_uso_cloud_hosting = st.selectbox("Nivel de uso:", ["N/A", "Sencillo", "Intermedio", "Difícil"], key="nivel_uso_cloud_hosting")

    with col_coste_cloud_hosting:
        coste_cloud_hosting = st.selectbox("Coste:", ["N/A", "Gratuito", "De pago", "Freemium"], key="coste_cloud_hosting")

    with col_seguridad_cloud_hosting:
        seguridad_cloud_hosting = st.selectbox("Seguridad:", ["N/A", "Alta", "Media", "Básica"], key="seguridad_cloud_hosting")

    cloud_hosting_list = [{"Escalabilidad":escalabilidad_cloud_hosting},{ "Nivel de Uso":nivel_uso_cloud_hosting}, {"Coste":coste_cloud_hosting}, {"Seguridad":seguridad_cloud_hosting}]
    subparameter_list.append(cloud_hosting_list)
    checkbox_list.append({"CloudHosting":checkbox_cloud_hosting})

# Bloque CD/CI & DevOps
checkbox_cdci_devops = st.checkbox("CD/CI & DevOps", key="cd/ci_devOps")
if checkbox_cdci_devops:
    # Crear columnas
    col_escalabilidad_cdci_devops, col_nivel_uso_cdci_devops, col_coste_cdci_devops, col_seguridad_cdci_devops = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_cdci_devops:
        escalabilidad_cdci_devops = st.selectbox("Escalabilidad:", ["N/A", "Alta", "Media", "Baja"], key="escalabilidad_cdci_devops")
    with col_nivel_uso_cdci_devops:
        nivel_uso_cdci_devops = st.selectbox("Nivel de uso:", ["N/A", "Sencillo", "Intermedio", "Difícil"], key="nivel_uso_cdci_devops")

    with col_coste_cdci_devops:
        coste_cdci_devops = st.selectbox("Coste:", ["N/A", "Gratuito", "De pago", "Freemium"], key="coste_cdci_devops")

    with col_seguridad_cdci_devops:
        seguridad_cdci_devops = st.selectbox("Seguridad:", ["N/A", "Alta", "Media", "Básica"], key="seguridad_cdci_devops")

    cdci_devops_list = [{"Escalabilidad":escalabilidad_cdci_devops},{ "Nivel de Uso":nivel_uso_cdci_devops}, {"Coste":coste_cdci_devops}, {"Seguridad":seguridad_cdci_devops}]
    subparameter_list.append(cdci_devops_list)
    checkbox_list.append({"CD/CI DevOps":checkbox_cdci_devops})

# Bloque Message Service
checkbox_msg = st.checkbox("Message Service", key="message_service")
if checkbox_msg:
    # Crear columnas
    col_escalabilidad_msg, col_nivel_uso_msg, col_coste_msg, col_seguridad_msg = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_msg:
        escalabilidad_msg = st.selectbox("Escalabilidad:", ["N/A", "Alta", "Media", "Baja"], key="escalabilidad_msg")
    
    with col_nivel_uso_msg:
        nivel_uso_msg = st.selectbox("Nivel de uso:", ["N/A", "Sencillo", "Intermedio", "Difícil"], key="nivel_uso_msg")

    with col_coste_msg:
        coste_msg = st.selectbox("Coste:", ["N/A", "Gratuito", "De pago", "Freemium"], key="coste_msg")

    with col_seguridad_msg:
        seguridad_msg = st.selectbox("Seguridad:", ["N/A", "Alta", "Media", "Básica"], key="seguridad_msg")
    
    msg_list = [{"Escalabilidad":escalabilidad_msg},{ "Nivel de Uso":nivel_uso_msg}, {"Coste":coste_msg}, {"Seguridad":seguridad_msg}]
    subparameter_list.append(msg_list)
    checkbox_list.append({"Message":checkbox_msg})

# Bloque Search Engine
checkbox_search_engine = st.checkbox("Search Engine", key="search_engine") 
if checkbox_search_engine:
    # Crear columnas
    col_escalabilidad_search_engine, col_nivel_uso_search_engine, col_coste_search_engine, col_seguridad_search_engine = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_search_engine:
        escalabilidad_search_engine = st.selectbox("Escalabilidad:", ["N/A", "Alta", "Media", "Baja"], key="escalabilidad_search_engine")
    with col_nivel_uso_search_engine:
        nivel_uso_search_engine = st.selectbox("Nivel de uso:", ["N/A", "Sencillo", "Intermedio", "Difícil"], key="nivel_uso_search_engine")

    with col_coste_search_engine:
        coste_search_engine = st.selectbox("Coste:", ["N/A", "Gratuito", "De pago", "Freemium",], key="coste_search_engine")

    with col_seguridad_search_engine:
        seguridad_search_engine = st.selectbox("Seguridad:", ["N/A", "Alta", "Media", "Básica"], key="seguridad_search_engine")

    search_engine_list = [{"Escalabilidad":escalabilidad_search_engine},{ "Nivel de Uso":nivel_uso_search_engine}, {"Coste":coste_search_engine}, {"Seguridad":seguridad_search_engine}]
    subparameter_list.append(search_engine_list)
    checkbox_list.append({"Search Engine":checkbox_search_engine})

# Bloque media_storage

checkbox_media_storage = st.checkbox("Media Storage", key="media_storage") 
if checkbox_media_storage:
    # Crear columnas
    col_escalabilidad_media_storage, col_nivel_uso_media_storage, col_coste_media_storage, col_seguridad_media_storage = st.columns(4)

    # Crear cada columna con su select
    with col_escalabilidad_media_storage:
        escalabilidad_media_storage = st.selectbox("Escalabilidad:", ["N/A", "Alta", "Media", "Baja"], key="escalabilidad_media_storage")
    with col_nivel_uso_media_storage:
        nivel_uso_media_storage = st.selectbox("Nivel de uso:", ["N/A", "Sencillo", "Intermedio", "Difícil"], key="nivel_uso_media_storage")

    with col_coste_media_storage:
        coste_media_storage = st.selectbox("Coste:", ["N/A", "Gratuito", "De pago", "Freemium"], key="coste_media_storage")

    with col_seguridad_media_storage:
        seguridad_media_storage = st.selectbox("Seguridad:", ["N/A", "Alta", "Media", "Básica"], key="seguridad_media_storage")

    media_storage_list = [{"Escalabilidad":escalabilidad_media_storage},{ "Nivel de Uso":nivel_uso_media_storage}, {"Coste":coste_media_storage}, {"Seguridad":seguridad_media_storage}]
    subparameter_list.append(media_storage_list)
    checkbox_list.append({"Media Storage":checkbox_media_storage})

    # Every form must have a submit button.
    
if submitted:

    for x in range(len(checkbox_list)):
        for key in checkbox_list[x]:
            if checkbox_list[x][key]:
                dataset_list.append(key)
    
    filtered_data = (filter_data(dataset_list,dataset_prelist))
    data_to_read = get_data_filtered(urls_list,dataset_list)
    data = read_data(data_to_read)
 
    # Transformamos los subparametros al diccionario cuya clave sea el sector al que pertenecen
    subparameter_dict = {
    dataset_list[i]: {list(d.keys())[0]: list(d.values())[0] for d in subparameter_list[i]}
    for i in range(len(dataset_list))
    }

    # Hacemos que el dataset se vea como un diccionario para poder ver el sector en específico al que se refiere
    data_dict = {dataset_list[i]:data[i].to_dict(orient="records") for i in range(len(dataset_list))}


    promptFinal = {
        "pregunta": idea,
        "subparametros": subparameter_dict,
        "data":data_dict,
        "formato_respuesta":"Devuelve una descripción resumida de la posible arquitectura del proyecto y una lista JSON con recomendaciones de herramientas en formato: categoría, producto, descripción. Esta informacion tiene que estar basada en los parametros_checkeados que esten marcados como True y en sus subparámetros"
    }
    json_response = []
    st.write(promptFinal)
    # Display the DataFrame as a table
    st.dataframe(json_response)
