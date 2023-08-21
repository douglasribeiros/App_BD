from servicos.animal import *
import streamlit as st
from PIL import Image
from animal import *
def procurar_animal(conexao):

    cursor = conexao.cursor()
    col1,col2 = st.columns([1,2])
    with col1:
        image = Image.open('Imagens/busca_animal.png')
        st.image(image,width=100)
    with col2:    
        st.title('BUSCAR ANIMAL')

    cod_animal = st.text_input('Digite o codigo do animal')

    if st.button("Buscar"):
        consulta = consultar_animal(cursor,cod_animal)
        if consulta=='Nenhum resultado':
            st.warning('Nenhum animal encontrado!')
        else:
            st.header(f'**_INFORMAÇÕES DO ANIMAL_**')
            st.markdown(f'**_NOME DO DONO_**:  {consulta[0]}')
            st.markdown(f'**_NOME DO ANIMAL_**:   {consulta[1]}')
            st.markdown(f'**_TIPO DO ANIMAL_**:  {consulta[2]}')        
            st.markdown(f'**_ESPÉCIE_**:  {consulta[3]}')
            st.markdown(f'**_SEXO_**:  {consulta[4]}')
            st.markdown(f'**_PORTE_**:  {consulta[5]}')        
            st.markdown(f'**_COR_**:  {consulta[6]}')
            st.markdown(f'**_ENDEREÇO_**:  {consulta[7]}')
            st.markdown(f'**_COMUNIDADE_**:  {consulta[8]}')      
            st.markdown(f'**_MUNICIPO_**:  {consulta[9]}') 
            st.markdown(f'**_UF_**:  {consulta[10]}') 
            st.markdown(f'**_LOCAL DO ANIMAL_**:  {consulta[11]}') 