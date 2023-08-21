import streamlit as st
from PIL import Image
from servicos import *
from obito import *

def registrar_obito(conexao):
    cursor = conexao.cursor()
    valores = []
    col1,col2 = st.columns([1,2])
    with col1:
        image = Image.open('Imagens/registro_obito.png')
        st.image(image,width=100)
    with col2:    
        st.title('REGISTRAR OBITO')

    col1,col2 = st.columns([1,1])
    with col1:
        zona = st.text_input('DIGITE O ID DA ZONA')

    with col2:

        animal_cod = st.selectbox('Selecione o codigo do animal',consultar_codigo_animal(cursor))
    
    col1,col2 = st.columns([1,1])
    with col1:
        procedimento = st.text_input('INFORME A DESCRIÇÃO EX(Óbito,Sacrificio,Enfermidade)')

    with col2:
        data = st.date_input("DATA:",obtem_data_atual())
        
    col1,col2 = st.columns([1,1])
    with col1:
        local = st.text_input('INFORME O LOCAL')

    with col2:
        ficha = st.text_input('INFORME A FICHA DE OBITO')

    col1,col2 = st.columns([1,1])
    with col1:
        desc = st.text_input('INFORME A DESCRIÇÃO DO ANIMAL')

    with col2:
        destino = st.text_input('INFORME O DESTINO DO CORPO')

    valores = [zona,animal_cod,procedimento,data,local,ficha,desc,destino]
 
 
    if st.button("Enviar"):
        registro = cadastrar_obito(cursor,valores)
        if registro == False:
            st.error('Não foi possivel registrar o obito!')
        else:
            st.success('Registro salvo com sucesso!')
