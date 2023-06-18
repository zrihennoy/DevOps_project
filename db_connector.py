import pymysql
def db_connect():
    conn = pymysql.connect(host='devops_project-db-1', port=3306, user='root', password='password', db='db')
    return conn

def get_username(user_id):
    conn = db_connect()
    cursor = conn.cursor()
    len= cursor.execute("select user_name from db.users where user_id=%s;", user_id)
    user = (cursor.fetchall())
    cursor.close()
    conn.close()
    print(user)
    if len == 0 :
        return "The is no such user"
    else:
        return user[0][0]

def create_user(user_id, user_name):
    conn = pymysql.connect(host='devops_project-db-1', port=3306, user='root', password='password', db='db')
    cursor = conn.cursor()
    cursor.execute("insert into db.users (user_id, user_name) VALUES (%s,%s);", (user_id, user_name))
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(user_id):
    conn = pymysql.connect(host='devops_project-db-1', port=3306, user='root', password='password', db='db')
    cursor = conn.cursor()
    cursor.execute("delete from db.users where user_id = %s;", user_id)
    conn.commit()
    cursor.close()
    conn.close()

def update_user(user_id, user_name):
    conn = pymysql.connect(host='devops_project-db-1', port=3306, user='root', password='password', db='db')
    cursor = conn.cursor()
    cursor.execute("update db.users set user_name = %s WHERE (user_id = %s);", (user_name, user_id))
    conn.commit()
    cursor.close()
    conn.close()
