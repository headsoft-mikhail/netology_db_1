import sqlalchemy
import passwords
import requests

def open_db(name, password):
    db_url = f"postgresql+psycopg2://postgres:{password}@localhost:5432/"
    engine = sqlalchemy.create_engine(f"{db_url}{name}")
    connection = engine.connect()
    return connection

def create_db(name, password, default_db_name='postgres'):
    connection = open_db(default_db_name, password)
    connection.execute("COMMIT")
    connection.execute(f"CREATE DATABASE {name} WITH OWNER = postgres;")
    connection = open_db(name, password)
    return connection

def get_commands_from_github(url):
    commands_text = requests.get(url).content.decode("utf-8").replace("\t", "").replace("\r", "").replace("\n", "")
    commands_list = [command + ";" for command in commands_text.split(";") if command != ""]
    return commands_list


db_name = 'music'
db_password = passwords.db_password

try:
    db = open_db(db_name, db_password)
except sqlalchemy.exc.OperationalError:
    db = create_db(db_name, db_password)

sql_code_url = "https://raw.githubusercontent.com/headsoft-mikhail/netology_db_1/main/create_db_code_updated.txt"
sql_commands = get_commands_from_github(sql_code_url)
for command_num in range(2, len(sql_commands)):
    db.execute(sql_commands[command_num])

db.close()

