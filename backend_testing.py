import requests
import  pymysql
#try:
res = requests.post('http://127.0.0.1:5000/users/7',json={"user_name": "john1"})
#print(res.content)
#res = requests.get('http://127.0.0.1:5000/users/2')
if res.ok:
    respose= res.json()
    print(respose)
    print("user added")
else:
    print(res.content)
    print("user doesnt exist")

conn = pymysql.connect(host='devops_project-db-1', port=3306, user='user', password='password', db='db')
cursor = conn.cursor()
cursor.execute("select user_name from public.users where user_id=2;")
username=cursor.fetchall()
print(username[0][0])
        #if username == "john":
       #     print("The user john is stored under id 1")
       # else:
       #     print("The user john is not stored under id 1")
#except Exception as e:
 #   print("test failed")
