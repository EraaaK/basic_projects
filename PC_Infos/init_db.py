import sqlite3
import os.path
from app_data import MachineInfos


def initDB():
    pc_info = MachineInfos()
    connection = sqlite3.connect('database.db')

    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    cur.execute(
        "INSERT INTO machine (marca, modelo, nome, qtd_cpu, arquitetura, familia) VALUES(?, ?, ?, ?, ?, ?)",
        (
            pc_info[0],
            pc_info[1],
            pc_info[2],
            pc_info[3],
            pc_info[4],
            pc_info[5],
        )
    )

    connection.commit()
    connection.close()
