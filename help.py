# 1.create the project
# 2.create file requirements .txt
# 3.write list in libraries
# 4. install all in libraries
# 5 pip freeze > requerements.txt
# 6. django-admin startproject config . -> command for the creation of the prject where config is title of project,point it is imprtant , без точки будет вложенность
# 7. django-admin startapp post  -> command for create new app
# 8.python3 manage.py makemigrations -> command для считывания данных с моделек like git commit. all migrations saved in file 'migrations'
        # !!!!psql -- create database with name from settings.
# 9. python3 manage.py migrate for отправки данных в бд user should be like my user in psql
# 10.  python3 manage.py runserver for  server's start
# 11. python3 manage.py createsuperuser for create user with admin

# --------------------------------
# python3 manage.py shell -  открывает интерактивный интерпритатор python
# . с помощью нее может работать с Django с командой строки.
# Это удобно для выполнения запросов и тестинга фрагмегтов кода

# ---------------------------------------------------------------------
# realated_name - используется для определения имени обратной связи с другой
# моделью .Он устанавливает имя ,по которому можно обращатся к связанным
# обьектам из моделеи  и обычно используется в поле Foreignkey


# realated_query_name - опция испльзуется для определения имени  обратной связи,
# используемого в запросах. Он определяет как связанные обьекты могут быть запрошенны
# с помощью методов filter(),exclude()

import json
# json-> python
json_data = '{"category": "ferrari", "title": "carlos sinze", "body": "smooooth operator"}'
data = json.loads(json_data)
print(data)
print(type(data))
# python -> json
json_data = json.dumps(data)
print(json_data)
