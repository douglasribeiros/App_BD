import mysql.connector
from mysql.connector import errorcode
from configparser import ConfigParser, ExtendedInterpolation

def conectar_bd():
    #informações de login do banco
    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read(r"..\conf.ini")

    try:
        db_connection = mysql.connector.connect(host=config['BANCO']['host'], user=config['LOGIN']['user'], password=config['LOGIN']['password'], database=config['BANCO']['database'])
        return db_connection
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database não existe")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario ou senha incorretos")
