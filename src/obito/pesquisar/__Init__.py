import pandas as pd

def consultar_obito_animal(cursor,animal_code):
    sql = f"SELECT a.p_nome,o.o_data,l.nome,o.o_descricao,a.a_grupo,o.o_causa,o.carcaca_destino,o.a_marcacao,o.o_veterinario FROM dt_obito o JOIN dt_animal a ON o.animal_code = a.animal_code JOIN rt_locais l ON l.loc_code = o.o_local WHERE o.animal_code='{animal_code}'"
    cursor.execute(sql)
    linhas = cursor.fetchall()
    if linhas!=[]:
        valores_obito = ([linhas[0][0],linhas[0][1].strftime('%d/%m/%y'),linhas[0][2],linhas[0][3],linhas[0][4],linhas[0][5],linhas[0][6],linhas[0][7],linhas[0][8]])
        return valores_obito
    else:
        return 'Nenhum resultado'
    
    