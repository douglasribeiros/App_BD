import pandas as pd

def consultar_animal(cursor,animal_code):
    sql = f"""  SELECT a.p_nome,a.a_nome,a.a_tipo,a.a_especie,a.a_sexo,a.a_porte,a.a_cor,
                    p.prop_endereco,p.prop_comunidade,p.prop_municipio,p.prop_uf, 
                    l.nome,l.tipo 
                FROM dt_animal a
                JOIN dt_propriedade p ON p.prop_code = a.prop_code
                JOIN rt_locais l ON l.loc_code = a.a_local
                WHERE a.animal_code='{animal_code}'"""
    cursor.execute(sql)
    linhas = cursor.fetchall()
    if linhas!=[]:
        valores_obito = []
        for i in range(0,12):
            valores_obito.append(str(linhas[0][i]).replace('None','Não informado'))
        return valores_obito
    else:
         return 'Nenhum resultado'
    
    