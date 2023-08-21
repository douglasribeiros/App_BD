import streamlit as st
from PIL import Image
from obito import *

def pesquisar_obito(conexao):
    cursor = conexao.cursor()
    col1,col2 = st.columns([1,2])
    with col1:
        image = Image.open('Imagens/obito.png')
        st.image(image,width=100)
    with col2:    
        st.title('PESQUISAR DE OBITOS')

    cod_animal = st.text_input('Digite o codigo do animal')

    if st.button("Buscar"):
        consulta = consultar_obito_animal(cursor,cod_animal)
        if consulta=='Nenhum resultado':
            st.warning('Nenhum animal encontrado!')
        else:
            st.header(f'**_INFORMAÇÕES DO ÓBITO_**')
            st.markdown(f'**_NOME DO DONO_**:{consulta[0]}')
            st.markdown(f'**_DATA_ÓBITO_**:{consulta[1]}')
            st.markdown(f'**_LOCAL_ÓBITO_**:{consulta[2]}')        
            st.markdown(f'**_DESCRIÇÃO DO ANIMAL_**:{consulta[3]}')
            st.markdown(f'**_ESPÉCIE_**:{consulta[4]}')
            st.markdown(f'**_CAUSA_**:{consulta[5]}')        
            st.markdown(f'**_DESTINO_CORPO_**:{consulta[6]}')
            st.markdown(f'**_MARCAÇÃO_**:{consulta[7]}')
            st.markdown(f'**_VETERINÁRIO_**:{consulta[8]}')      

            
