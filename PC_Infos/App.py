from flask import Flask, render_template
import sqlite3
import os.path
import init_db

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    conn = get_db_connection()
    pc_infos = conn.execute('SELECT * from machine').fetchall()
    conn.close()
    return render_template('index.html', machine=pc_infos)


init_db.initDB()
app.run()
