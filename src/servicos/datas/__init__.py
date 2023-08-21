from datetime import date
import datetime
def obtem_data_atual():
    today = date.today()
    today = str(today)
    today = today.split('-')
    ano = int(today[0])
    mes = int(today[1])
    dia = int(today[2])
    return datetime.date(ano, mes, dia)