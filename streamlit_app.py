

import streamlit as st
from streamlit.hello.utils import show_code

st.set_page_config(page_title="Strategic Data Transform", page_icon="scr/fondo.jpg", layout="wide")
           
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

column_widths = [1, 3, 1]
with st.container():
    
    col1, col2, col3 = st.columns(column_widths)   
    with col1:
        st.title("")
        
    with col3:
        st.title("")
          
    with col2: 
        st.image("scr/SDTLogoC.png",width=1200, use_column_width=True, output_format='auto')

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
        imagen = "scr/barras.png"  
        st.image(imagen, width=500, use_column_width=True, output_format='auto')       

st.title("Nuestra propuesta de valor")
st.write("<hr style='border-top: 0.5px solid grey;'>", unsafe_allow_html=True)
column_widths = [2, 1]
with st.container():

        col1, col2 = st.columns(column_widths)  
        
        with col1:
            st.header("Dashboards de alto impacto.")
            st.subheader("""
            Nuestra idea es hacer dashboards de un gran impacto visual como a la vez completamente funcionales, interactivos e intuitivos para el usuario. En la actualidad se muestran muchas métricas y gráficos de manera apilada, sin dejar espacios libres, haciéndolos densos para ser leídos e interpretados. Nuestra idea es usar gráficos que sean más originales, respetando su imagen corporativa, pero un poco más desafiantes que paneles convencionales, que simplemente sean funcionales.
            """)
            st.header("Analisis Cientificos de datos.")
            st.subheader("""
            Gracias a las nuevas tecnologias y librerias disponibles para las mismas, podemos realizar analisis de datos basandonos en complementos del lenguaje de programacion Python, tales como Pandas, Seaborn y Mathplotlib.
            """)
        with col2:
                imagen = "scr/dash.png"  
                st.image(imagen, width=500, use_column_width=True, output_format='auto')    
            
st.write("""
<style>
    .botones a {
        font-size: 30px;
        margin-top: 10px; /* Espacio después de la imagen */
        text-decoration: none; /* Quitar el subrayado */
        color: #ffffff; /* Cambiar el color del texto del enlace */
        
    }
</style>
""", unsafe_allow_html=True)  
with st.container():
    st.markdown(
    """
    <style>
        a {
            color: red; /* Cambia el color del texto del enlace a rojo */
        }
    </style>
    """,
    unsafe_allow_html=True
   )
    st.markdown('<style>h4{color: white;}, font=</style>', unsafe_allow_html=True)    
    st.markdown('<style>h3 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h2 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>h1 {color: white;}, font=</style>', unsafe_allow_html=True)
    st.markdown('<style>write {color: white;}, font=</style>', unsafe_allow_html=True)
st.title("Nuestros proyectos")    
st.write("<hr style='border-top: 3px solid white;'>", unsafe_allow_html=True)    
column_widths = [2, 1]
with st.container():
     
    col1, col2 = st.columns(column_widths)   
    
    with col1:
        st.header("Greyhound NYC Insercion de mercado")
        st.markdown(""" 
                #### Proyecto de analisis de insercion de mercado al sistema de vehiculos con chofer para la ciudad de NYC, se analizaron tanto los factores economicos como ambientales para tomar desiciones de si invertir o no en este negocio, tomando en cuenta varias hipotesis y llegando a sus respectivas conclusiones
                # """) 
                
        st.write('<div class="botones"><a href="https://greyhound.streamlit.app/">Acceder a la App</a>', unsafe_allow_html=True)
        st.write('<div class="botones"><a href="https://github.com/marceloyuba/SDT">Acceder a la documentacion</a>', unsafe_allow_html=True)
        
    with col2:
        imagen = "scr/grey.png"  
        st.image(imagen, width=500, use_column_width=True, output_format='auto')        

st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)    

with st.container():
    col1, col2 = st.columns(column_widths)
    
    with col1:
        st.header("Accidentes Viales en la Ciudad de Buenos Aires")        
        st.markdown("""
                #### Desde la expansión en 2021, Nuestro cliente analiza nuevos mercados fuera del transporte de buses, por eso nos encomendó analizar la inserción al negocio de los viajes en automóviles, analizando a su competidores directos (Taxis, Uber, Lyft) y comenzando por la ciudad de Nueva York, ya que la misma tiene una de las redes mas complejas de transporte en todo el pais, nuestro trabajo es analizar si es viable el ingreso al sistema cumpliendo con las regulaciones impuestas por el gobierno respecto a tener una ciudad libre de emisiones contaminantes""") 
        st.write('<div class="botones"><a href="https://accidentesbuenosaires.streamlit.app/">Acceder a la App</a>', unsafe_allow_html=True)
        st.write('<div class="botones"><a href="https://github.com/marceloyuba/Proyecto_individual_Data_Analyst">Acceder a la documentacion</a>', unsafe_allow_html=True)
    
    with col2:
        imagen = "scr/BA.png"  
        st.image(imagen, width=500, use_column_width=True, output_format='auto')
    
    
st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)    

with st.container():
    col1, col2 = st.columns(column_widths)
    
    with col1:
        st.header("Callejon Futbol")        
        st.markdown("""
                #### Es una propuesta diferente de analizar el Futbol, tomando a los dos maximos referentes del siglo 21, Lionel messi y Cristiano Ronaldo, hacemos un repaso de sus estadisticas en sus años en La Liga y las comptencias continentales, por su paso por Barcelona y Real Madrid respectivamente 
                """)         
        st.write('<div class="botones"><a href="https://callejonfutbol.streamlit.app/">Acceder a la App</a>', unsafe_allow_html=True)
        #st.write('<div class="botones"><a href="https://greyhound.streamlit.app/">Acceder a la documentacion</a>', unsafe_allow_html=True)
    with col2:
        imagen = "scr/callejon.png"  
        st.image(imagen, width=500, use_column_width=True, output_format='auto')
st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)  

st.title("")

st.title("Nuestro equipo de trabajo")

with st.container():
     
    col1, col2 = st.columns(column_widths)
    
    
    with col1:
        st.header("Elizabeth Fraire")
        st.markdown(""" 
                #### Departamento: Data Science, Engineering, Analist
                #### Background: Ciencias Biológicas
                #### Linkedin: [Acceder a su perfil](https://www.linkedin.com/in/veronica-elizabeth-torres-fraire-a830bb234/)
                #### Github: [Acceder a su perfil](https://github.com/Bethcosima)
                """) 
    
    with col2:
        imagen = "scr/Eli.jpg"  
        st.image(imagen, width=250, use_column_width=False, output_format='auto')    

st.title("")

with st.container():
     
    col1, col2 = st.columns(column_widths)
    
    
    with col1:
        st.header("Marcelo Yuba")
        st.markdown(""" 
                #### Departamento: Data Analist, Graphic Design
                #### Background: Diseño multimedial, Publicidad grafica, E-Commerce
                #### Linkedin: [Acceder a su perfil](www.linkedin.com/in/marcelo-yuba)
                #### Github: [Acceder a su perfil](https://github.com/marceloyuba)
                """) 
    with col2:
        imagen = "scr/fotoLI.jpg"  
        st.image(imagen, width=250, use_column_width=False, output_format='auto')   

st.write("<hr style='border-top: 1px solid grey;'>", unsafe_allow_html=True)    
with st.container():
    
    st.header("Contactanos!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
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