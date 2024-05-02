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
app.config['PERMANENT_SESSION_LIFETIME'] = 3600 * 24
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] = "None"

CORS(app, resources={r"*": {"origins": "http://localhost:5173", 'supports_credentials': True}})
MEDIA_FOLDER = os.getenv('MEDIA')

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
        print(pas)

        password = cursor.fetchall()

        passwords = []

        for row in password:
            passwords.append(dict(row))
        pg.commit()
        print(passwords)
        if pas==passwords[0]['admin_pass']: 
            return_data = True
            session['isAdmin'] = 'True'
        elif pas==passwords[0]['person_pass']: 
            return_data = False
            session['isAdmin'] = 'False'
        else: 
            return_data = "Неверный пароль!"
    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = 'ошибка дб'


    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
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
        print(xyi)

        for key in info:
            if key != 'xyi':
                if key not in dang_key:
                    info_for_db+=f", '{info[key]}'"
                else:
                    if key=='CtkModel': print(1)
                    print(key, xyi[key])
                    if key!='Note':
                        src = add_img(key, info[key], info['Fio'], xyi[key], False, id)
                        info_for_db+=f", '{src}'"
                    else: info_for_db+=", 'rdfkek'"
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(f'INSERT INTO vr VALUES({info_for_db})')
        pg.commit()

        return_data = 'Иформация добавлена'

    except (Exception, Error) as error:
        print(f'DB ERROR: ', error)
        return_data = f"Ошибка обращения к базе данных: {error}"
        return 0

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
            return return_data

# Обновление строчки
def update_string(info,xyi,  id):
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

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
        print(xyi)
        for key in info:
            if key != 'Age':
                if key not in dang_key:
                    info_for_db+=f", {key} = $${info[key]}$$"
                else:
                    if key=='CtkModel': print(1)

                    if key!='Note':
                        if xyi[key]!='':
                            if 'base64' in info[key]:
                                src = add_img(key, info[key], info['Fio'], xyi[key], True, id)
    
                                info_for_db+=f", {key} = $${src}$$"
                            else: info_for_db+=f", {key} = $${info[key]}$$"
                        else: 
                            info_for_db+=f", {key} = ''"

                    else: info_for_db+=", ''"
            else: 
                info_for_db+=f" {key} = $${info[key]}$$"
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f''' UPDATE vr 
                       SET {info_for_db}
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
def delete_string(ids):
    try: 
        pg = psycopg2.connect(f"""
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        for id in ids:
            cursor.execute(f'''DELETE FROM vr
                        WHERE id=$${id}$$''')
        
        pg.commit()
        return_data = 'Success'
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
            print(pas)
            cursor.execute(f'''SELECT COUNT(*) FROM admins 
                                        WHERE admin_pass=$${pas}$$
                                        ''')
            isTrue = cursor.fetchall()
            print(isTrue)
            if isTrue[0][0] == 1:
                return_data = True
            else: return_data = False



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

            cursor.execute(f'''UPDATE admins 
                                    SET admin_pass=$${pas}$$''')
            return_data = 'Пароль обновлен'
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

            cursor.execute(f'''UPDATE admins 
                            SET person_pass=$${pas}$$''')
            pg.commit()
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
            host=localhost
            dbname=postgres
            user=postgres
            password={os.getenv('PASSWORD_PG')}
            port={os.getenv('PORT_PG')}
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        

        print(filtr)
        cursor.execute(f"SELECT * FROM vr{filtr}")
        result = cursor.fetchall()
        pg.commit()
        return_data = []
        for row in result:
            return_data.append(form_dict(dict(row)))

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
def add_img(key, base, fio, name, isId, id):
    print(isId, key, name)
    if isId == False:
        base=base[base.find(',')+1:]
        decoded_bytes = base64.b64decode(base)
        name = name[name.find('.'):]
        name=key+'_'+id+name
        print(name)

        with open(os.path.join(MEDIA_FOLDER, name), "wb") as file:
            file.write(decoded_bytes)

        return 'http://127.0.0.1:5000/media/'+name
    else:
        d = show_one(isId)
        base=base[base.find(',')+1:]
        d = d[0]
        print(d)
        name = d[key][d[key].find('m'):]
        decoded_bytes = base64.b64decode(base)
        with open(os.path.join(name), "wb") as file:
            file.write(decoded_bytes)
        return d[key]


def trim_to_first_dot(s):
    # Возвращаем подстроку до первого вхождения точки включительно
    return s[:s.find('.')] if '.' in s else s

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
        


        cursor.execute(f"SELECT * FROM vr")
        result = cursor.fetchall()
        pg.commit()

        return_data = []
        for row in result:
            return_data.append(form_dict(dict(row)))

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
        print(id)
        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        pg.commit()

        cursor.execute(f'''SELECT * FROM vr 
                       WHERE id=$${id}$$''')
        result = cursor.fetchall()

        return_data = []
        for row in result:
            # print(dict(row))
            return_data.append(form_dict(dict(row)))

    except (Exception, Error) as error:
        print(f"Ошибка получения данных: {error}")
        return_data = 'Error'

    finally:
        if pg:
            cursor.close
            pg.close
            print("Соединение с PostgreSQL закрыто")
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
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        response_object['isAdmin'] = login_user(post_data.get('Login'))
        return jsonify(response_object)
    

# Декоратор для создания нововй строки
@app.route('/new-string', methods=['POST'])
def new_string():
    response_object = {'status': 'success'}
    post_data = request.get_json()

    add_string(post_data.get('form'))

    return jsonify(response_object)


# Декоратор для обновления строки
@app.route('/update-string', methods=['PUT'])
def update_stringaaaaaaaaaaaaaaaaa():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    post_data = post_data.get('body')
    form = post_data.get('form')
    xyi = post_data.get('xyi')
    print(form)
    response_object['res'] = update_string(form, xyi, form['id'])

    return jsonify(response_object)


# Декоратор для удаления строки
@app.route('/delete-string', methods = ['DELETE'])
def del_srt():
    responce_object = {'status' : 'success'}
    post_data = request.get_json()
    print(post_data)
    responce_object['res'] = delete_string(post_data.get('id'))

    return jsonify(responce_object)


# Декоратор для семены пароля
@app.route('/change-pass', methods=['POST'])
def change():
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
    
    print(responce_object['res'])

    return jsonify(responce_object)


# Декоратор для проверки юзера
@app.route('/check', methods=['GET'])
def checking():
    responce_object = {'status': 'success'}

    if session.get('isAdmin') == 'True':
        responce_object['isAdmin'] = 'True'
    elif session.get('isAdmin') == 'False':
        responce_object['isAdmin'] = 'False'
    else: 
        responce_object['isAdmin'] = 'Он никто'
    print(responce_object)
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
    # print(responce_object['all'])
    return jsonify(responce_object)

@app.route('/media/<path:filename>')
def serve_file(filename):
    path = filename
    print(MEDIA_FOLDER+path)
    if not os.path.exists('{}/{}'.format(MEDIA_FOLDER, '/'+filename)):
        return jsonify({'error': 'File not found'}), 404

    return send_from_directory(directory=MEDIA_FOLDER, path=path)

@app.route('/show-one', methods=['GET'])
def one():
    responce_object = {'status': 'success'}
    id = request.args.get('id')

    responce_object['all'] = show_one(id)



    return jsonify(responce_object)

#БаZа
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
