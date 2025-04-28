import streamlit as st
from helpers import set_img, set_video

# ***--- Configuration ---***
st.set_page_config(page_title="PEC 2 Plataformas de publicación y distribución", layout="wide")

exercises = {
    "Ejercicio 1": "exercises/exercise1.md",
    "Ejercicio 2": "exercises/exercise2.md",
    "Ejercicio 3": "exercises/exercise3.md",
    "Ejercicio 4": "exercises/exercise4.md",
    "Ejercicio 5": "exercises/exercise5.md"
}
# ***--- Configuration ---***


# ***--- Sidebar ---***
st.sidebar.title("Navegación")
st.sidebar.markdown("Esta aplicación la he generado con Streamlit. En esta barra de navegación se puede\
    elegir el ejercicio que se quiere consultar. Además, cada ejercicio tiene un apartado con los assets\
    referenciados en el ejercicio.")
st.sidebar.markdown("Si quieres ver el código de la aplicación, puedes hacerlo [aquí](https://github.com/ToroData/Plataformas-de-publicacion-y-distribucion)")
st.sidebar.markdown("Para acceder a todos los vídeo assets como ZIP comprimido, puedes hacerlo [aquí]()")
selection = st.sidebar.radio("Ir a:", list(exercises.keys()))
# ***--- Sidebar ---***


# ***--- Main ---***
st.title(selection)

with open(exercises[selection], "r", encoding="utf-8") as file:
    content = file.read()
tab1, tab2 = st.tabs(["PEC - Respuestas escritas", "Assets referenciados en el ejercicio seleccionado"])


with tab1:
    st.markdown(content, unsafe_allow_html=True)

with tab2:
    if selection == "Ejercicio 1":
        set_video(
            "Asset-01",
            "https://plataforma-distribucion-streamlit.s3.eu-west-3.amazonaws.com/asset-01.mp4",
        )
        set_img(
            "https://plataforma-distribucion-streamlit.s3.eu-west-3.amazonaws.com/propiedades-asset-01.png",
            "Fig. 1. Propiedades del asset-01",
            "Imágenes del asset-01",
        )
        set_img(
            "https://plataforma-distribucion-streamlit.s3.eu-west-3.amazonaws.com/propiedades-mediaarea.png",
            "Fig. 2. Propiedades del MediaInfo"
        )

    elif selection == "Ejercicio 2":
        set_video(
            "Asset-02",
            "https://plataforma-distribucion-streamlit.s3.eu-west-3.amazonaws.com/asset-02.mp4",
        )
        set_img(
            "https://plataforma-distribucion-streamlit.s3.eu-west-3.amazonaws.com/propiedades-asset-02.png",
            "Fig. 1. Propiedades del asset-02",
            "Imágenes del asset-02",
        )
        set_img(
            "https://plataforma-distribucion-streamlit.s3.eu-west-3.amazonaws.com/propiedades-mediaarea-asset-02.png",
            "Fig. 2. Propiedades del MediaInfo"
        )
    elif selection == "Ejercicio 3":
        st.warning('Es posible que dado que los vídeos tienen formato `.mpg` no se puedan reproducir en algunos navegadores. \
            En caso de que no se reproduzcan, se encuentran en el repositorio.')
        set_video(
            "pec2_dvd",
            "https://plataforma-distribucion-streamlit.s3.eu-west-3.amazonaws.com/pec2_dvd.mpg",
        )
        set_video(
            "pec2_dvd_m2_n8",
            "https://plataforma-distribucion-streamlit.s3.eu-west-3.amazonaws.com/pec2_dvd_m2_n8.mpg",
        )
        set_video(
            "pec2_dvd_m3_n15",
            "https://plataforma-distribucion-streamlit.s3.eu-west-3.amazonaws.com/pec2_dvd_m3_n15.mpg",
        )
        set_img(
            "https://plataforma-distribucion-streamlit.s3.eu-west-3.amazonaws.com/propiedades-pec2_dvd.png",
            "Fig. 1. Propiedades del pec2_dvd"
        )
        set_img(
            "https://plataforma-distribucion-streamlit.s3.eu-west-3.amazonaws.com/propiedades-pec2_dvd_m3_n15.png",
            "Fig. 2. Propiedades del pec2_dvd_m3_n15"
        )
    elif selection == "Ejercicio 4":
        set_video(
            "hevc-70",
            "https://plataforma-distribucion-streamlit.s3.eu-west-3.amazonaws.com/hevc-70.mkv",
        )
        set_video(
            "hevc-40",
            "https://plataforma-distribucion-streamlit.s3.eu-west-3.amazonaws.com/hevc-40.mkv"
        )
        set_video(
            "hevc-40-gop-30",
            "https://plataforma-distribucion-streamlit.s3.eu-west-3.amazonaws.com/hevc-40-gop-30.mkv"
        )
# ***--- Main ---***
