import uuid
import psycopg2
from psycopg2 import extras, Error
from flask import Flask, jsonify, request, session, make_response
from flask_cors import CORS


app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['PERMANENT_SESSION_LIFETIME'] = 3600
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] = "None"

CORS(app, resources={r"*": {"origins": "http://localhost:5173", 'supports_credentials': True}})

def db_get():
    try:
        pg = psycopg2.connect("""
            host=localhost
            dbname=postgres
            user=postgres
            password=kos120675
            port=5432
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
        

def login_user(pas):
        
    if pas=='kodvfwdse': return_data = 'Добро пожаловать!'
    elif pas=='fdwji': return_data = 'Добро пожаловать, админ!'
    else: return_data = "Неверный пароль!"
    return return_data

def add_string(info):
    try: 
        pg = psycopg2.connect("""
            host=localhost
            dbname=postgres
            user=postgres
            password=kos120675
            port=5432
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f' INSERT INTO patient $${info}$$')
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
    
def update_string(info, id):
    try: 
        pg = psycopg2.connect("""
            host=localhost
            dbname=postgres
            user=postgres
            password=kos120675
            port=5432
        """)

        cursor = pg.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute(f''' UPDATE patient 
                       SET $${info}$$
                       WHERE id==$${id}$$''')
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        print(login_user(post_data.get('password')))
        return jsonify(response_object)
        
    else:
        response_object['message'] = db_get()
        return jsonify(response_object)


@app.route('/new-string', methods=['POST'])
def new_string():
    response_object = {'status': 'success'}
    post_data = request.get_json()

    add_string(post_data.get().values())

    return jsonify(response_object)


@app.route('/update-string', methods=['UPDATE'])
def new_string():
    response_object = {'status': 'success'}
    post_data = request.get_json()

    update_string(post_data.get().values(), post_data.get('id'))

    return jsonify(response_object)


if __name__ == '__main__':
    app.run()