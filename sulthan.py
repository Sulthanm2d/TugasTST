from flask import Flask, request, jsonify
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)
app.config['DEBUG'] = True

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'sulthan'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/kodepos/city')
def home():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    kota = ("%"+request.args.get('name')+"%")
    sql = "SELECT *  FROM db_postal_code_data WHERE city LIKE %s"
    cur.execute(sql,kota)
    ret= cur.fetchall()
    res ={
        'desc': "BERHASIL GET DATA",
        'results': ret
    }
    return jsonify(res)


@app.route('/kodepos/urban')
def index():
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    urban = ("%"+request.args.get('name')+"%")
    sql = "SELECT *  FROM db_postal_code_data WHERE urban LIKE %s"
    cur.execute(sql,urban)
    ret= cur.fetchall()
    res = {
        'desc': "BERHASIL GET DATA",
        'results': ret
    }
    return jsonify(res)


if __name__ == "__main__":
    app.run()