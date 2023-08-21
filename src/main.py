from conexao_bd import *
from paginas import * 
import streamlit as st
from PIL import Image


conexao = conectar_bd()
image = Image.open('Imagens/veterinario.png')
st.sidebar.image(image,width=100)
st.sidebar.title("Banco Veterinario")

opcao = st.sidebar.selectbox(
    'Selecione a opção',['Buscar registro de obito','Registrar obito','Procurar animal'])
if opcao == 'Buscar registro de obito':
   pesquisar_obito(conexao)

elif opcao == 'Registrar obito':
    registrar_obito(conexao)
    conexao.commit()

elif opcao == 'Procurar animal':
    procurar_animal(conexao)
    
