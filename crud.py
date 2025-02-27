import mysql.connector
from config import MYSQYL_HOST,MYSQYL_USER,MYSQYL_PASSWORD,MYSQYL_DATABASE

def get_connection():
    return mysql.connector.connect(
        host = MYSQYL_HOST,
        user = MYSQYL_USER,
        password = MYSQYL_PASSWORD,
        database = MYSQYL_DATABASE)

def create_user(nome,telefone,email,usuario,senha):
    conn = get_connection()
    cursor=conn.cursor()
    querry = "insert usuario(nome,telefone,email,usuario,senha)VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(querry,(nome,telefone,email,usuario,senha))
    conn.commit()
    cursor.close()
    conn.close()

def read_users():
    conn = get_connection()
    cursor=conn.cursor()
    querry = "SELECT * FROM usuario"
    cursor.execute(querry)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def update_user(user_id,nome,telefone,email,usuario,senha):
    conn = get_connection()
    cursor=conn.cursor()
    querry = "UPDATE usuario SET nome=%s,telefone=%s,email=%s,usuario=%s,senha=%s WHERE idusuario = %s"
    cursor.execute(querry,(nome,telefone,email,usuario,senha,user_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cursor=conn.cursor()
    querry = "DELETE FROM usuario WHERE idusuario = %s"
    cursor.execute(querry,(user_id,))
    conn.commit()
    cursor.close()
    conn.close()