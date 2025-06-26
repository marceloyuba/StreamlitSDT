import streamlit as st
from streamlit.hello.utils import show_code

st.set_page_config(page_title="Strategic Data Transform", page_icon="scr/fondo.jpg", layout="wide")

# Aplicar estilos globales para texto en negro y enlaces
st.markdown(
    """
    <style>
        h1, h2, h3, h4, h5, h6, p, div, span, li, strong, em {
            color: black !important;
        }

        a {
            color: #00a4de !important;
            text-decoration: none;
        }

        .botones a {
            font-size: 30px;
            margin-top: 10px;
            color: #00a4de !important;
        }

        input, textarea, button {
            font-size: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

column_widths = [1, 3, 1]
with st.container():
    col1, col2, col3 = st.columns(column_widths)
    with col2:
        st.image("scr/SDTLogoC.png", width=1200, use_container_width=True, output_format='auto')

st.title("")

st.title("Sobre nosotros")
st.write("<hr style='border-top: 0.5px solid grey;'>", unsafe_allow_html=True)
column_widths = [2, 1]
with st.container():
    col1, col2 = st.columns(column_widths)
    with col1:
        st.subheader("""
        Strategic Data Transform es una consultora de información, para generar estrategias de negocios, basado en datos.
        #### Se basa en un tipo de negocio B2B. Como empresa, ofrecer servicios a otras empresas, que estén dentro de la esfera del IT, tanto como empresas no relacionadas a la actividad y tengan necesidades de analizar sus datos y que permita poder desarrollar mejor sus actividades, teniendo conciencia de donde se encuentran las fallas en relación con cómo administran su información de negocio. 
        """)
    with col2:
        st.image("scr/barras.png", width=500, use_container_width=True, output_format='auto')

st.title("Nuestra propuesta de valor")
st.write("<hr style='border-top: 0.5px solid grey;'>", unsafe_allow_html=True)
with st.container():
    col1, col2 = st.columns(column_widths)
    with col1:
        st.header("Dashboards de alto impacto.")
        st.subheader("""
        Nuestra idea es hacer dashboards de un gran impacto visual como a la vez completamente funcionales, interactivos e intuitivos para el usuario. En la actualidad se muestran muchas métricas y gráficos de manera apilada, sin dejar espacios libres, haciéndolos densos para ser leídos e interpretados. Nuestra idea es usar gráficos que sean más originales, respetando su imagen corporativa, pero un poco más desafiantes que paneles convencionales, que simplemente sean funcionales.
        """)
        st.header("Análisis Científicos de datos.")
        st.subheader("""
        Gracias a las nuevas tecnologías y librerías disponibles para las mismas, podemos realizar análisis de datos basándonos en complementos del lenguaje de programación Python, tales como Pandas, Seaborn y Matplotlib.
        """)
    with col2:
        st.image("scr/dash.png", width=500, use_container_width=True, output_format='auto')

st.title("Nuestros proyectos")
st.write("<hr style='border-top: 3px solid white;'>", unsafe_allow_html=True)
with st.container():
    col1, col2 = st.columns(column_widths)
    with col1:
        st.header("Greyhound NYC Inserción de mercado")
        st.markdown(""" 
        #### Proyecto de análisis de inserción de mercado al sistema de vehículos con chofer para la ciudad de NYC, se analizaron tanto los factores económicos como ambientales para tomar decisiones de si invertir o no en este negocio, tomando en cuenta varias hipótesis y llegando a sus respectivas conclusiones
        """) 
        st.write('<div class="botones"><a href="https://greyhound.streamlit.app/">Acceder a la App</a>', unsafe_allow_html=True)
        st.write('<div class="botones"><a href="https://github.com/marceloyuba/SDT">Acceder a la documentación</a>', unsafe_allow_html=True)
    with col2:
        st.image("scr/grey.png", width=500, use_container_width=True, output_format='auto')

st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)
with st.container():
    col1, col2 = st.columns(column_widths)
    with col1:
        st.header("Accidentes Viales en la Ciudad de Buenos Aires")
        st.markdown("""
        #### Desde la expansión en 2021, Nuestro cliente analiza nuevos mercados fuera del transporte de buses, por eso nos encomendó analizar la inserción al negocio de los viajes en automóviles, analizando a sus competidores directos (Taxis, Uber, Lyft) y comenzando por la ciudad de Nueva York, ya que la misma tiene una de las redes más complejas de transporte en todo el país, nuestro trabajo es analizar si es viable el ingreso al sistema cumpliendo con las regulaciones impuestas por el gobierno respecto a tener una ciudad libre de emisiones contaminantes
        """) 
        st.write('<div class="botones"><a href="https://accidentesbuenosaires.streamlit.app/">Acceder a la App</a>', unsafe_allow_html=True)
        st.write('<div class="botones"><a href="https://github.com/marceloyuba/Proyecto_individual_Data_Analyst">Acceder a la documentación</a>', unsafe_allow_html=True)
    with col2:
        st.image("scr/BA.png", width=500, use_container_width=True, output_format='auto')

st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)
with st.container():
    col1, col2 = st.columns(column_widths)
    with col1:
        st.header("Callejón Futbol")
        st.markdown("""
        #### Es una propuesta diferente de analizar el Futbol, tomando a los dos máximos referentes del siglo 21, Lionel Messi y Cristiano Ronaldo, hacemos un repaso de sus estadísticas en sus años en La Liga y las competencias continentales, por su paso por Barcelona y Real Madrid respectivamente 
        """)
        st.write('<div class="botones"><a href="https://callejonfutbol.streamlit.app/">Acceder a la App</a>', unsafe_allow_html=True)
    with col2:
        st.image("scr/callejon.png", width=500, use_container_width=True, output_format='auto')

st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)

st.title("")
st.title("Nuestro equipo de trabajo")
st.title("")

with st.container():
    col1, col2 = st.columns(column_widths)
    with col1:
        st.header("Marcelo Yuba")
        st.markdown(""" 
        #### Departamento: Data Analyst, Data Engineering, Graphic Design
        #### Background: Diseño multimedial, Publicidad gráfica, E-Commerce
        #### Linkedin: [Acceder a su perfil](https://www.linkedin.com/in/marcelo-yuba)
        #### Github: [Acceder a su perfil](https://github.com/marceloyuba)
        """)
    with col2:
        st.image("scr/fotoLI.jpg", width=250, use_container_width=False, output_format='auto')

st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)
with st.container():
    st.header("¡Contactanos!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/strategicdatatransform@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Nombre" required>
        <input type="email" name="email" placeholder="E-mail" required>
        <textarea name="message" placeholder="Tu consulta" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://github.com/marceloyuba/StreamlitSDT/blob/main/scr/fondoi.png?raw=true");
    background-position: top left;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: cover;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

