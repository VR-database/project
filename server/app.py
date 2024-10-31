import os
import uuid
import psycopg2
from psycopg2 import extras, Error
from flask import Flask, jsonify, request, session, make_response, send_from_directory
from flask_cors import CORS
import base64
import io
from dotenv import load_dotenv
import logging
from typing import Tuple, Union
import hashlib

load_dotenv()

PASSWORD_PG = os.getenv('PASSWORD_PG')
USER_PG = os.getenv('USER_PG')
SECRET_KEY = os.getenv('SECRET_KEY')
HOST_PG = os.getenv('HOST_PG')
PORT_PG = os.getenv('PORT_PG')
HPST = os.getenv("HOST")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_hash, password):
    return stored_hash == hash_password(password)

def check_password_hash(stored_hash, input_password):
    return verify_password(stored_hash, input_password)

# SetUp
app = Flask(__name__)

app.secret_key = SECRET_KEY
app.config['PERMANENT_SESSION_LIFETIME'] = 3600 * 24
app.config['MAX_CONTENT_LENGTH'] = 1000 * 1024 * 1024 * 20   # 20000 Mb limit
# app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = "None"
app.config.update(
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_HTTPONLY=True
)

try:
    pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
except (Exception, Error) as error:
    logging.error(f'DB: ', error)



CORS(app, resources={r"*": {"origins": "*", 'supports_credentials': True}})
MEDIA_FOLDER = os.getenv('MEDIA')

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y—%m—%d %H:%M:%S",
)


@app.route('/api', methods=['GET'])
def api():
    if request.origin != HPST:
        return jsonify({"message": "Forbidden", "origin": request.origin}), 403
    if request.origin != HPST:
        return jsonify({"message": "Forbidden"}), 403
    return jsonify(message="Hello from API!")

def all_tables():
    pg = psycopg2.connect(f"""
        host={HOST_PG}
        dbname=postgres
        user={USER_PG}
        password={PASSWORD_PG}
        port={PORT_PG}
    """)
    
    pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
    cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('''CREATE TABLE IF NOT EXISTS vr (
                        id text,
                        Code text,
                        Fio text,
                        Floor text,
                        Age text,
                        NumberHistory text,
                        Date1 text,
                        Date2 text,
                        Result text,
                        Diagnosis text,
                        Date3 text,
                        NameOperation text,
                        CktDisk text,
                        MrtDisk text,
                        CktModel text,
                        MrtModel text,
                        OperationVideo text,
                        EffectOfUse1 text,
                        Notes text,



                        Fgds text,
                        Fks text,
                        Ckt text,
                        Mrt text,
                        Research text,
                        Protocol text,
                        DrugVideo text,
                        GistolСonclusion text
                        )
                        ''')
    

    cursor.execute('''CREATE TABLE IF NOT EXISTS admins (
                        admin_pass text,
                        person_pass text
                        )''')

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id uuid, email text, password text, surname text);")
    cursor.execute('''INSERT INTO admins (admin_pass, person_pass)
                        SELECT '1', '2'
                        WHERE NOT EXISTS (SELECT 1 FROM admins);''')
    pg.commit()
    cursor.close
    pg.close
    logging.info("Соединение с PostgreSQL закрыто")
# Логин  
def login_user(pas):
    try:         
        
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f'SELECT * FROM admins')
        logging.info(pas)

        password = cursor.fetchall()

        passwords = []

        for row in password:
            passwords.append(dict(row))
        pg.commit()
        logging.info(passwords)
        if pas==passwords[0]['admin_pass']: 
            return_data = True
            session['isAdmin'] = 'True'
            session.modified = True
            session.permanent = True
        elif pas==passwords[0]['person_pass']: 
            return_data = False
            session['isAdmin'] = 'False'
            session.permanent = True
            session.modified = True

        else: 
            return_data = "Неверный пароль!"
    except (Exception, Error) as error:
        logging.error(f'DB ERROR: ', error)
        return_data = 'ошибка дб'
    finally:
        return return_data
# Добавление строчки
def add_string(info):
    try: 
        dang_key = ['Fgds', 'Fks', 'Ckt', 'Mrt', 'Research', 'DrugVideo', 'GistolConclusion', 'CktDisk', 'MrtDisk', 'CktModel', 'MrtModel', 'OperationVideo', 'Protocol']
        id = uuid.uuid4().hex
        info_for_db = f"'{id}'"
        xyi= {
              'CktDisk': info['xyi']['xyi1'],
              'MrtDisk': info['xyi']['xyi2'],
              'CktModel': info['xyi']['xyi3'],
              'MrtModel': info['xyi']['xyi4'],
              'OperationVideo': info['xyi']['xyi5'],
              'EffectOfUse1': info['xyi']['xyi6'],
              '7': info['xyi']['xyi7'],
              'Fgds': info['xyi']['xyi8'],
              'Fks': info['xyi']['xyi9'],
              'Ckt': info['xyi']['xyi10'],
              'Mrt': info['xyi']['xyi11'],
              'Research': info['xyi']['xyi12'],
              'Protocol': info['xyi']['xyi13'],
              'DrugVideo': info['xyi']['xyi14'],
              'GistolConclusion': info['xyi']['xyi15']
            }
        logging.info(xyi)

        for key in info:
            if key != 'xyi':
                if key not in dang_key:
                    info_for_db+=f", '{info[key]}'"
                else:
                    if key=='CtkModel': logging.info(1)
                    # logging.info(key, xyi[key])
                    if key!='Note':
                        src = add_img(key, info[key], info['Fio'], xyi[key], False, id)
                        info_for_db+=f", '{src}'"
                    else: info_for_db+=", 'rdfkek'"
        
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f'INSERT INTO vr VALUES({info_for_db})')
        pg.commit()

        return_data = 'Иформация добавлена'

    except (Exception, Error) as error:
        logging.error(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}"
        return 0

    finally:
        return return_data
# Обновление строчки
def update_string(info,xyi,  id):
    try: 
        dang_key = ['Fgds', 'Fks', 'Ckt', 'Mrt', 'Research', 'DrugVideo', 'GistolConclusion', 'CktDisk', 'MrtDisk', 'CktModel', 'MrtModel', 'OperationVideo', 'Protocol']
        info_for_db = ""
        xyi= {
              'CktDisk': xyi['xyi1'],
              'MrtDisk': xyi['xyi2'],
              'CktModel': xyi['xyi3'],
              'MrtModel': xyi['xyi4'],
              'OperationVideo': xyi['xyi5'],
              'EffectOfUse1': xyi['xyi6'],
              '7': xyi['xyi7'],
              'Fgds': xyi['xyi8'],
              'Fks': xyi['xyi9'],
              'Ckt': xyi['xyi10'],
              'Mrt': xyi['xyi11'],
              'Research': xyi['xyi12'],
              'Protocol': xyi['xyi13'],
              'DrugVideo': xyi['xyi14'],
              'GistolConclusion': xyi['xyi15']
            }
        # logging.info(xyi)
        for key in info:
            if key != 'Age':
                if key not in dang_key:
                    info_for_db+=f", {key} = $${info[key]}$$"
                else:
                    if key=='CtkModel': logging.info(1)

                    if key!='Note':
                        if xyi[key]!='':
                            logging.info('base64' in info[key], key)
                            if 'base64' in info[key]:
                                logging.info(key)
                                print(key, info['Fio'], xyi[key], True, id)
                                src = add_img(key, info[key], info['Fio'], xyi[key], True, id)
    
                                info_for_db+=f", {key} = $${src}$$"
                                continue
                            info_for_db+=f", {key} = $${info[key]}$$"
                            continue
                        info_for_db+=f", {key} = $${info[key]}$$"

                    else: info_for_db+=", ''"
            else: 
                info_for_db+=f" {key} = $${info[key]}$$"
        
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f''' UPDATE vr 
                       SET {info_for_db}
                       WHERE id=$${id}$$''')
        pg.commit()

        return_data = 'Иформация обновлена'

    except (Exception, Error) as error:
        logging.error(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        return return_data
# удаление строчки
def delete_string(ids):
    try: 
        
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        for id in ids:
            cursor.execute(f'''DELETE FROM vr
                        WHERE id=$${id}$$''')
        
        pg.commit()
        return_data = 'Success'
    except (Exception, Error) as error:
        logging.error(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}" 

    finally:
        return return_data
# Проверка пароля
def pass_check(pas, Admin): 
    if Admin:
        try: 
            
            pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
            logging.info(pas)
            cursor.execute(f'''SELECT COUNT(*) FROM admins 
                                        WHERE admin_pass=$${pas}$$
                                        ''')
            isTrue = cursor.fetchall()
            logging.info(isTrue)
            if isTrue[0][0] == 1:
                return_data = True
            else: return_data = False



        except (Exception, Error) as error:
            logging.error(f'DB ERROR: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            return return_data
    
# Смена пароля
def new_pass(pas, Admin):
    if Admin:
        try: 
            
            pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute(f'''UPDATE admins 
                                    SET admin_pass=$${pas}$$''')
            return_data = 'Пароль обновлен'
            pg.commit()

        except (Exception, Error) as error:
            logging.error(f'DB ERROR: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            if pg:
                cursor.close
                pg.close
                logging.info("Соединение с PostgreSQL закрыто")
            return return_data
    
    else:
        try: 
            
            pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
            cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute(f'''UPDATE admins 
                            SET person_pass=$${pas}$$''')
            pg.commit()
            return_data = 'Пароль обновлен'


        except (Exception, Error) as error:
            logging.error(f'DB ERROR: ', error)
            return_data = f"Ошибка обращения к базе данных: {error}" 

        finally:
            return return_data


# ФИЛЬТРЫ
def filtration(filters):
    if filters['filtr']!='false':
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
    else: return show_all()
    try:
        
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        

        logging.info(filtr)
        cursor.execute(f"SELECT * FROM vr{filtr}")
        result = cursor.fetchall()
        pg.commit()
        return_data = []
        for row in result:
            return_data.append(form_dict(dict(row)))

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        return return_data

# Добовление файла в папку
def add_img(key, base, fio, name, isId, id):
    print(id, key, name)
    if base!='':
        if isId == False:
            base=base[base.find(',')+1:]
            decoded_bytes = base64.b64decode(base)

            name = name[name.find('.'):]
            
            name=key+'_'+id+name
            logging.info(name)

            with open(os.path.join(MEDIA_FOLDER, name), "wb") as file:
                file.write(decoded_bytes)

            return 'https://api.ar-vmgh.ru/media/'+name
        else:
            d = show_one(id)
            base=base[base.find(',')+1:]
            logging.info(d)
            d = d[0][key]
            logging.info(d)
            # name = d[key][d[key].find('m'):]
            if d == '' or d == '-':
                return add_img(key, base, fio, name, False, id)
            name = d[d.find('media')+6:]
            logging.info(name)

            decoded_bytes = base64.b64decode(base)
            with open(os.path.join(MEDIA_FOLDER, name), "wb") as file:
                file.write(decoded_bytes)
            return d
    else: return '-'


def trim_to_first_dot(s):
    # Возвращаем подстроку до первого вхождения точки включительно
    return s[:s.find('.')] if '.' in s else s

# Показ всего
def show_all():
    try:
        
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f"SELECT * FROM vr")
        result = cursor.fetchall()
        pg.commit()

        return_data = []
        for row in result:
            return_data.append(form_dict(dict(row)))

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        return return_data
    
# показ одной строки
def show_one(id):
    try:        
        logging.info(id)
        
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        pg.commit()

        cursor.execute(f'''SELECT * FROM vr 
                       WHERE id=$${id}$$''')
        result = cursor.fetchall()

        return_data = []
        for row in result:
            logging.info(dict(row))
            return_data.append(form_dict(dict(row)))

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        return return_data
    
def form_dict(slovar):
    form = {
        'id': slovar['id'],
        'Code': slovar['code'],
        'Fio': slovar['fio'],
        'Floor': slovar['floor'],
        'Age': slovar['age'],
        'NumberHistory': slovar['numberhistory'],
        'Date1': slovar['date1'],
        'Date2': slovar['date2'],
        'Result': slovar['result'],
        'Diagnosis': slovar['diagnosis'],
        'Date3': slovar['date3'],
        'NameOperation': slovar['nameoperation'],
        'CktDisk': slovar['cktdisk'],
        'MrtDisk': slovar['mrtdisk'],
        'CktModel': slovar['cktmodel'],
        'MrtModel': slovar['mrtmodel'],
        'OperationVideo': slovar['operationvideo'],
        'EffectOfUse1': slovar['effectofuse1'],
        'Notes': slovar['notes'],
        'Fgds': slovar['fgds'],
        'Fks': slovar['fks'],
        'Ckt': slovar['ckt'],
        'Mrt': slovar['mrt'],
        'Research': slovar['research'],
        'Protocol': slovar['protocol'],
        'DrugVideo': slovar['drugvideo'],
        'GistolСonclusion': slovar['gistolСonclusion']
    }
    
    return form

def mini(id):
    return id
# ========================================================================================


# Декоратор для логина
@app.route('/login', methods=['POST'])
def login():
    if request.origin != HPST:
        return jsonify({"message": "Forbidden"}), 403
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        response_object['isAdmin'] = login_user(post_data.get('Login'))
        return jsonify(response_object)
    

# Декоратор для создания нововй строки
@app.route('/new-string', methods=['POST'])
def new_string():
    if request.origin != HPST:
        return jsonify({"message": "Forbidden"}), 403
    response_object = {'status': 'success'}
    post_data = request.get_json()

    add_string(post_data.get('form'))

    return jsonify(response_object)


# Декоратор для обновления строки
@app.route('/update-string', methods=['PUT'])
def update_stringaaaaaaaaaaaaaaaaa():
    if request.origin != HPST:
        return jsonify({"message": "Forbidden"}), 403
    response_object = {'status': 'success'}
    post_data = request.get_json()
    post_data = post_data.get('body')
    form = post_data.get('form')
    xyi = post_data.get('xyi')
    # logging.info(form)
    response_object['res'] = update_string(form, xyi, form['id'])

    return jsonify(response_object)


# Декоратор для удаления строки
@app.route('/delete-string', methods = ['DELETE'])
def del_srt():
    if request.origin != HPST:
        return jsonify({"message": "Forbidden"}), 403
    responce_object = {'status' : 'success'}
    post_data = request.get_json()
    logging.info(post_data)
    responce_object['res'] = delete_string(post_data.get('id'))

    return jsonify(responce_object)


# Декоратор для семены пароля
@app.route('/change-pass', methods=['POST'])
def change():
    if request.origin != HPST:
        return jsonify({"message": "Forbidden"}), 403
    responce_object = {'status' : 'success'}
    post_data = request.get_json()

    # Проверка на то, админ ли это и проходит лит он проверку (pass_check возращает True/False в зависимости от совпадаемости паролей)
    if post_data.get('Admin') and pass_check(post_data.get('Login').get('passwordOld'), True):
        responce_object['res'] = new_pass(post_data.get('Login').get('Newpassword1'), True)
    
    # Проверка на то проходит ли он проверку (pass_check возращает True/False в зависимости от совпадаемости паролей)
    elif not post_data.get('Admin') and pass_check(post_data.get('Login').get('passwordOld'), True):
        responce_object['res'] = new_pass(post_data.get('Login').get('Newpassword1'), False)
    
    # Иначе возращаем, что пароль неверный
    else: responce_object['res'] = 'Неверный пороль'
    
    logging.info(responce_object['res'])

    return jsonify(responce_object)


# Декоратор для проверки юзера
@app.route('/check', methods=['GET'])
def checking():
    if request.origin != HPST:
        return jsonify({"message": "Forbidden"}), 403
    responce_object = {'status': 'success'}
    logging.info(session.get('isAdmin'))
    if session.get('isAdmin') == 'True':
        responce_object['isAdmin'] = 'True'
    elif session.get('isAdmin') == 'False':
        responce_object['isAdmin'] = 'False'
    else: 
        responce_object['isAdmin'] = 'Он никто'
    logging.info(responce_object)
    return jsonify(responce_object)

@app.route('/filtre', methods=['POST'])
def filtre_():
    if request.origin != HPST:
        return jsonify({"message": "Forbidden"}), 403
    responce_object = {'status': 'success'}
    post_data = request.get_json()
    filtre_data = post_data.get('body').get('filters')

    responce_object['all'] = filtration(filtre_data)

    return jsonify(responce_object)

@app.route('/show-all', methods=['GET'])
def shows():
    if request.origin != HPST:
        return jsonify({"message": "Forbidden"}), 403
    responce_object = {'status': 'success'}
    if session.get('isAdmin') == 'True':
        responce_object['all'] = show_all()
    else: responce_object["all"] = "Отказано в доступе"
    return jsonify(responce_object)

@app.route('/media/<path:filename>')
def serve_file(filename):
    # if request.origin != HPST:
    #     return jsonify({"message": "Forbidden"}), 403
    path = filename
    logging.info(MEDIA_FOLDER+path)
    if not os.path.exists('{}/{}'.format(MEDIA_FOLDER, '/'+filename)):
        return jsonify({'error': 'File not found'}), 404

    return send_from_directory(directory=MEDIA_FOLDER, path=path)

@app.route('/show-one', methods=['GET'])
def one():
    if request.origin != HPST:
        return jsonify({"message": "Forbidden"}), 403
    responce_object = {'status': 'success'}
    id = request.args.get('id')

    responce_object['all'] = show_one(id)

    return jsonify(responce_object)

@app.route('/test', methods=['POST'])
def test_():
    logging.info("1")
    res = []
    lst = ["1", "2"]
    for i in lst:
        if i not in request.files:
            # return 'No file part', 400
            continue
        logging.info(2)
        file = request.files[i]
        if file.filename == '':
            return 'No selected file', 400
        res.append(add_img_f(file, file.filename))
        logging.info(3)

    response_object = {'status': 'success'} #БаZа
    logging.info(4)
    
    # post_data = request.get_json()
    # logging.info(request)
    response_object["res"] = res
    # response_object["res"] = post_data


    return jsonify(response_object)
    
    # return jsonify({"err": request.content_type}), 400

def add_img_f(file, name, id):

    # name = file.filename
    try:
        logging.info(type(name))
        res = id+name
        logging.info(file)
        file.save(os.path.join(MEDIA_FOLDER, res))
        return_data = 'https://api.ar-vmgh.ru/media/'+res
    except (Exception, Error) as error:
        logging.error(f'DB: ', error)
        return_data = error 
    finally:
        return return_data
    print("ну накрутил до 2 часов, ну имею права, идте нахуй бляди, я всю ночь с эим еблюсь блять и ура, я могу поспать нахуй, питухон язык долбаебов, я так вам скажу, все, я спать, перфекционист мой в норме, 2 часа в проекте, 04.07.2024 2:34, заебанный всем Костя")

def new_string_text(form):
    info_for_db = ""
    columns='id'
    for key in form:
        columns+=f', {key}'
        info_for_db+=f", '{form[key]}'"
        
    try:
        id = uuid.uuid4().hex
        
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f"INSERT INTO vr ({columns}) VALUES ('{id}' {info_for_db})")
        session["string"] = id
        session.modified = True
        return_data = "success"
        pg.commit()
    except (Exception, Error) as error:
        logging.info(f"""Ошибка добовления данных: {error}""")
        return_data = 'Error'

    finally:
        return return_data  
    
def new_string_file(id):
    info_for_db = ""
    keys = ['Fgds', 'Fks', 'Ckt', 'Mrt', 'Research', 'DrugVideo', 'GistolConclusion', 'CktDisk', 'MrtDisk', 'CktModel', 'MrtModel', 'OperationVideo', 'Protocol']
    for i in keys:
        if i not in request.files: continue
        if i == 'GistolConclusion':
            info_for_db += f", gistolСonclusion = $${add_img_f(request.files[i], i + request.files[i].filename, id)}$$"
            continue
        if info_for_db == "":
            info_for_db += f"{i} = $${add_img_f(request.files[i], i + request.files[i].filename, id)}$$"
            continue
        info_for_db += f", {i} = $${add_img_f(request.files[i], i +request.files[i].filename, id)}$$"
    try:
        
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        logging.info(f"""UPDATE vr SET {info_for_db} WHERE id = $${id}$$""")

        cursor.execute(f"""UPDATE vr SET {info_for_db} WHERE id = $${id}$$""")
        pg.commit()
        # cursor.execute(f"""SELECT * FROM vr WHERE id = $${id}$$""")
        # return_data = cursor.fetchall()
        return_data = "Ok"
    except (Exception, Error) as error:
        logging.info(f"""Ошибка добовления данных: {error}""")
        return_data = 'Error'
    finally:
        return return_data  

def upd_string_text(form, id):
    info_for_db = ""
    dang_keys = ['Fgds', 'Fks', 'Ckt', 'Mrt', 'Research', 'DrugVideo', 'GistolConclusion', 'CktDisk', 'MrtDisk', 'CktModel', 'MrtModel', 'OperationVideo', 'Protocol']

    for key in form:
        if key in dang_keys: continue
        if info_for_db != "":
            info_for_db+=f", {key} = $${form[key]}$$"
            continue
        info_for_db+=f" {key} = $${form[key]}$$"
        
        
    try:
        
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f"""UPDATE vr SET {info_for_db} WHERE id = $${id}$$""")
        session["upd_string"] = id
        session.modified = True
        return_data = "success"
        pg.commit()
    except (Exception, Error) as error:
        logging.info(f"""Ошибка добовления данных: {error}""")
        return_data = 'Error'

    finally:
        return return_data  

def upd_string_file(id):
    info_for_db = ""
    keys = ['Fgds', 'Fks', 'Ckt', 'Mrt', 'Research', 'DrugVideo', 'GistolConclusion', 'CktDisk', 'MrtDisk', 'CktModel', 'MrtModel', 'OperationVideo', 'Protocol']
    for i in keys:
        if i not in request.files: 
            logging.info(i)
            continue
        if i == 'GistolConclusion':
            info_for_db += f"gistolСonclusion = $${add_img_f(request.files[i], i + request.files[i].filename, id)}$$"
            continue
        if info_for_db == "":
            info_for_db += f"{i} = $${add_img_f(request.files[i], i + request.files[i].filename, id)}$$"
            continue
        info_for_db += f", {i} = $${add_img_f(request.files[i], i +request.files[i].filename, id)}$$"
    try:
        
        pg = psycopg2.connect(f"""
            host={HOST_PG}
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={PORT_PG}
        """)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        logging.info(f"""UPDATE vr SET {info_for_db} WHERE id = $${id}$$""")
        cursor.execute(f"""UPDATE vr SET {info_for_db} WHERE id = $${id}$$""")
        pg.commit()
        return_data = "Ok"
    except (Exception, Error) as error:
        logging.info(f"""Ошибка добовления данных: {error}""")
        return_data = 'Error'
    finally:
        return return_data
    
@app.route('/new-string/text', methods=["POST"])
def new_string_text_():
    responce_object = {"status":"success"}
    form = request.get_json().get("form")
    responce_object["res"] = new_string_text(form)
    return jsonify(responce_object)

@app.route('/new-string/file', methods=["POST"])
def new_string_file_():
    responce_object = {"status":"success"}
    
    responce_object["res"] =  new_string_file(session.get("string"))
    session.pop("string")

    return jsonify(responce_object)
     
@app.route('/update-string/text', methods=["PUT"])
def upd_string_text_():
    responce_object = {"status":"success"}
    post_data = request.get_json()
    responce_object["res"] = upd_string_text(post_data.get("form"), post_data.get("id"))
    return jsonify(responce_object)

@app.route('/update-string/file', methods=["PUT"])
def upd_string_file_():
    responce_object = {"status":"success"}
    
    responce_object["res"] =  upd_string_file(session.get("upd_string"))
    session.pop("upd_string")

    return jsonify(responce_object)

def SurSearch(query: str) -> Union[str, list]:
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        cursor.execute(f"SELECT * FROM vr WHERE Fio LIKE '%{query}%'")
        result = cursor.fetchall()
        pg.commit()

        return_data = []
        for row in result:
            return_data.append(form_dict(dict(row)))

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data


@app.route('/surname-search', methods=['GET'])
def surname_search():
    responce_object = {'status': 'success'}

    responce_object['all'] = SurSearch(request.args.get('query'))

    return jsonify(responce_object)

@app.route('/new-login', methods=["POST"])
def new_login():
    if request.origin != HPST:
        return jsonify({"message": "Forbidden"}), 403
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()  
        response_object["isA"] = str(login_user(post_data.get('Login')))
        session["isA"] = response_object["isA"]
        session.modified = True
        return jsonify(response_object)

def send_pass_code(email: str) -> str:
    pass
# TODO: офрмление отправки и сама отправка


@app.route('/send-email', methods=["POST"])
def send_email():
    if request.origin != HPST:
        return jsonify({"message": "Forbidden"}), 403
    response_object = {'status': 'success'}
    post_data = request.get_json()
    session["surname"], session["email"], session["password"], session["code"] = post_data.get("surname"), post_data.get("email"), post_data.get("password"), send_pass_code(post_data.get("email"))
    if session.get("code") != "err":
        return jsonify(response_object)
    else: 
        response_object["code"] = "Invalid email"
        return jsonify(response_object)

def add_user(email: str, password: str, surname: str) -> str:
    try:
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user={USER_PG}
            password={PASSWORD_PG}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        id = uuid.uuid4().hex

        cursor.execute(f"INSERT INTO users VALUES({id}, {email}, {password}, {surname})")
        result = cursor.fetchall()
        pg.commit()

        return_data = id

    except (Exception, Error) as error:
        logging.info(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if pg:
            cursor.close
            pg.close
            logging.info("Соединение с PostgreSQL закрыто")
            return return_data

@app.route("/check-send-code", methods=["POST"])
def chek_code_():
    if request.origin != HPST:
        return jsonify({"message": "Forbidden"}), 403
    response_object = {'status': 'success'}
    post_data = request.get_json()

    if session.get("code") == post_data.get("code"):
        res = add_user(session.get("email"), session.get("password"), session.get("surname"))
        session["isAdmin"] = session.get("isA")
        session.modified = True
        session.permanent = True
        session.pop("isA", None)
        if res == "Error":
            response_object["res"] = "500"
        else:
            session["id"] = res
            session.modified = True
            session.permanent = True
            response_object["res"] = "200"
        
    else:
        response_object["res"] = "Bad Code"
    
    return jsonify(response_object)
#БаZа
if __name__ == '__main__':
      all_tables()
      app.run(host='0.0.0.0', port=80)
