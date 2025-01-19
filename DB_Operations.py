import pymysql

def connect():
    return pymysql.connect(host="localhost",
                            user="root",
                            passwd="",
                            database="uas_web",
                            cursorclass=pymysql.cursors.DictCursor)
def fetch_all_items():
    connection=connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM tb_camping")
            rows = cursor.fetchall()
        return rows
    finally:
        connection.close()

def insert_item(nama_paket,fasilitas,harga):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO tb_camping (nama_paket, fasilitas, harga) VALUES (%s, %s, %s)",
                           (nama_paket,fasilitas,harga))
            connection.commit()
        return 1
    finally:
        connection.close()

def fetch_item_by_id(item_id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM tb_camping WHERE id = %s",(item_id))
            rows = cursor.fetchone()
        return rows
    finally:
        connection.close()

def update_item(item_id, nama_paket, fasilitas, harga):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE tb_camping SET nama_paket = %s, fasilitas = %s, harga = %s WHERE id = %s",
                           (nama_paket,fasilitas,harga,item_id))
            connection.commit()
        return 1
    finally:
        connection.close()

def delete_item(item_id):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM tb_camping WHERE id = %s",(item_id))
            connection.commit()
        return 1
    finally:
        connection.close()