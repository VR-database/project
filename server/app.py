import os
import uuid
import psycopg2
from psycopg2 import extras, Error
from flask import Flask, jsonify, request, session, make_response, send_from_directory
from flask_cors import CORS
import base64
import io
from dotenv import load_dotenv

load_dotenv()

# SetUp
app = Flask(__name__)

app.secret_key = os.getenv('PASSWORD_PG')
app.config['PERMANENT_SESSION_LIFETIME'] = 3600
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] = "None"

CORS(app, resources={r"*": {"origins": "http://localhost:5173", 'supports_credentials': True}})
MEDIA_FOLDER = os.getenv('MEDIA')


# BaZa
def db_get():
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        pg.commit()

        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()

        return_data = []
        for row in result:
            return_data.append(dict(row))

    except (Exception, Error) as error:
        return_data = f"Ошибка получения данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data

# Логин  
def login_user(pas):
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)
         
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f'SELECT * FROM admins')

        password = cursor.fetchone()
        passwords = []
        for row in password:
            passwords.append(dict(row))
        pg.commit()
    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = 'ошибка дб'


    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data
        
    if pas==passwords['admin']: 
        return_data = True
        session['isAdmin'] = True
    elif pas==passwords['person']: 
        return_data = False
        session['isAdmin'] = False
    else: 
        return_data = "Неверный пароль!"
    return return_data

# Добавление строчки
def add_string(info):
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)
        
        dang_key = ['Fgds', 'Fks', 'Ckt', 'Mrt', 'Research', 'NameOperation', 'DrugVideo', 'GistolСonclusion', 'CktDisk', 'MrtDisk', 'CktModel', 'MrtModel', 'OperationVideo']
        info_for_db = [uuid.uuid4.hex]

        for key in info:
            if key not in dang_key:
                info_for_db.append(info[key])
            else: 
                src = add_img(key, info[key], info['Fio'])
                info_for_db.append(src)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f' INSERT INTO VR VALUES({info_for_db})')
        pg.commit()

        return_data = 'Иформация добавлена'

    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data

# Обновление строчки
def update_string(info, id):
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f''' UPDATE patient 
                       SET $${info}$$
                       WHERE id=$${id}$$''')
        pg.commit()

        return_data = 'Иформация обновлена'

    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data

# удаление строчки
def delete_string(id):
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f'''DELETE patients
                        WHERE id=$${id}$$''')
        
        pg.commit()

    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data

# Проверка пароля
def pass_check(pas, Admin): 
    if Admin:
        try: 
            pg = psycopg2.connect(f"""                
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}               
                port={os.getenv('PORT_PG')}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            isTrue = cursor.execute(f'''SELECT COUNT FROM password_admin 
                                        WHERE password=$${pas}$$
                                        ''')
            if isTrue == 1:
                return_data = True


        except (Exception, Error) as error:
            print(f'DB ERROR: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            if pg:
                cursor.close
                pg.close
                print("Соединение с PostgreSQL закрыто")
                return return_data
    
    else:
        try: 
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}               
                port={os.getenv('PORT_PG')}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            isTrue = cursor.execute(f'''SELECT COUNT FROM password 
                                        WHERE password=$${pas}$$
                                        ''')
            if isTrue == 1:
                return_data = True


        except (Exception, Error) as error:
            print(f'DB ERROR: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            if pg:
                cursor.close
                pg.close
                print("Соединение с PostgreSQL закрыто")
                return return_data

# Смена пароля
def new_pass(pas, Admin):
    if Admin:
        try: 
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}               
                port={os.getenv('PORT_PG')}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute(f'''UPDATE password_admin 
                                    SET password =$${pas}$$''')
            return_data = 'Пароль обновлен'


        except (Exception, Error) as error:
            print(f'DB ERROR: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            if pg:
                cursor.close
                pg.close
                print("Соединение с PostgreSQL закрыто")
                return return_data
    
    else:
        try: 
            pg = psycopg2.connect(f"""
                host=localhost
                dbname=postgres
                user=postgres
                password={os.getenv('PASSWORD_PG')}               
                port={os.getenv('PORT_PG')}
            """)

            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute(f'''SELECT COUNT FROM password 
                                        SET password =$${pas}$$''')

            return_data = 'Пароль обновлен'


        except (Exception, Error) as error:
            print(f'DB ERROR: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            if pg:
                cursor.close
                pg.close
                print("Соединение с PostgreSQL закрыто")
                return return_data

# Добовление файла в дб
def file_to_db(base: str):
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)


        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f"INSERT INTO ggg VALUES('{base}', decode('{base}', 'base64'))")
        pg.commit()
        cursor.close
        pg.close
    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data

# Получение файла из дб
def file_from_db():
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * from ggg")
        to_encode = bytes(cursor.fetchall()[1][1])
        base64_bytes = base64.b64encode(to_encode)
        return_data = base64_bytes
        with open("bb.txt", "w") as f:
            f.write(base64_bytes.decode())

    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data

# ФИЛЬТРЫ
def filtration(filters):

    if not filters['filtr']:
        filtr = ''
    elif filters["filtr"]:
        filtr = ' WHERE'
        for i in filters:
            if filters[i] != 'false':
                if i == 'filtr':
                    continue
                if filtr == ' WHERE':
                    filtr += f' {i}=$${filters[i]}$$'
                else:
                    filtr += f' AND {i}=$${filters[i]}$$'

    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        pg.commit()

        cursor.execute(f"SELECT * FROM vr{filtr}")
        result = cursor.fetchall()

        return_data = []
        for row in result:
            return_data.append(dict(row))

    except (Exception, Error) as error:
        print(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data

# Добовление файла в папку
def add_img(key, base, fio):
    decoded_bytes = base64.b64decode(base)

    name=key+fio

    with open(os.path.join(MEDIA_FOLDER, name), "wb") as file:
        # Записываем данные в файл
        file.write(decoded_bytes)

    return MEDIA_FOLDER+'/'+name

# Показ всего
def show_all():
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        pg.commit()

        cursor.execute(f"SELECT * FROM vr")
        result = cursor.fetchall()

        return_data = []
        for row in result:
            print(dict(row))
            return_data.append(dict(row))

    except (Exception, Error) as error:
        print(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data
        
# показ одной строки
def show_one(id):
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        pg.commit()

        cursor.execute(f"SELECT * FROM vr 
                       WHERE id=$${id}$$")
        result = cursor.fetchall()

        return_data = []
        for row in result:
            print(dict(row))
            return_data.append(dict(row))

    except (Exception, Error) as error:
        print(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data
        

# ========================================================================================


# Декоратор для логина
@app.route('/login', methods=['POST'])
def login():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        post_data['isAdmin'] = login_user(post_data.get('password'))
        return jsonify(response_object)
    

# Декоратор для создания нововй строки
@app.route('/new-string', methods=['POST'])
def new_string():
    response_object = {'status': 'success'}
    post_data = request.get_json()

    add_string(post_data.get().values())

    return jsonify(response_object)


# Декоратор для обновления строки
@app.route('/update-string', methods=['UPDATE'])
def update_string():
    response_object = {'status': 'success'}
    post_data = request.get_json()

    response_object['res'] = update_string(post_data.get().values(), post_data.get('id'))

    return jsonify(response_object)


# Декоратор для удаления строки
@app.route('/delete-string', methods = ['DELETE'])
def del_srt():
    responce_object = {'status' : 'success'}
    post_data = request.get_json()

    responce_object['res'] = delete_string(post_data.get('id'))

    return jsonify(responce_object)


# Декоратор для семены пароля
@app.route('/change_pass', methods=['UPDATE'])
def change():
    responce_object = {'status' : 'success'}
    post_data = request.get_json()

    # Проверка на то, админ ли это и проходит лит он проверку (pass_check возращает True/False в зависимости от совпадаемости паролей)
    if post_data.get('Admin') and pass_check(post_data.get('old_pass'), True):
        responce_object['res'] = new_pass(post_data.get('old_pass'), True)
    
    # Проверка на то проходит ли он проверку (pass_check возращает True/False в зависимости от совпадаемости паролей)
    elif pass_check(post_data.get('old_pass'), False):
        responce_object['res'] = new_pass(post_data.get('old_pass'), False)
    
    # Иначе возращаем, что пароль неверный
    else: responce_object['res'] = 'Неверный пороль'
    
    print(responce_object['res'])

    return jsonify(responce_object)


# Декоратор для проверки юзера
@app.route('/check', methods=['GET'])
def checking():
    responce_object = {'status': 'success'}

    if session.get('isAdmin') == True:
        responce_object['isAdmin'] = True
    elif not session.get('isAdmin'):
        responce_object['isAdmin'] = False
    else: 
        responce_object['isAdmin'] = 'Он никто'
    
    return jsonify(responce_object)

@app.route('/filtre', methods=['POST'])
def filtre_():
    responce_object = {'status': 'success'}
    post_data = request.get_json()
    filtre_data = post_data.get('body').get('filters')

    responce_object['all'] = filtration(filtre_data)

    return jsonify(responce_object)

@app.route('/show-all', methods=['GET'])
def shows():
    responce_object = {'status': 'success'}

    responce_object['all'] = show_all()
    print(responce_object['all'])
    return jsonify(responce_object)

@app.route('/media/<path:filename>')
def serve_file(filename):
    if not os.path.exists('{}/{}'.format(MEDIA_FOLDER, filename)):
        return jsonify({'error': 'File not found'}), 404
    
    return send_from_directory(directory=MEDIA_FOLDER, path='/'+filename)

@app.route('/show-one', methods=['GET'])
def one():
    responce_object = {'status': 'success'}

    id = request.args.get('id')
    responce_object['all'] = show_one(id)

    return jsonify(responce_object)
#БаZа
if __name__ == '__main__':
    app.run()