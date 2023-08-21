

def cadastrar_obito(cursor,valores):
    sql = f"INSERT INTO dt_obito (zona_id,animal_code,o_proced,o_data,o_local,o_ficha,o_descricao,carcaca_destino) VALUES ({valores[0]},'{valores[1]}','{valores[2]}',{valores[3]},'{valores[4]}','{valores[5]}','{valores[6]}','{valores[7]}')"
    if cursor.execute(sql):
        return 'cadastrado' 
    else:
        return False









