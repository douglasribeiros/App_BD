def consultar_codigo_animal(cursor):
        cursor.execute('SELECT animal_code FROM dt_animal')
        cod_animal = list(cursor.fetchall())
        codigo = []
        for cod in cod_animal:
            cod = str(cod).replace("',)","").replace("('","")
            codigo.append(cod)
        return codigo    