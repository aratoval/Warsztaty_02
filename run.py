from configparser import ConfigParser


def login_data():
    path_config_file = "login_data.ini"
    Config = ConfigParser()
    Config.read(path_config_file)

    login = Config.get("db", "Login")
    password = Config.get("db", "Password")
    database = Config.get("db", "Database")
    host = Config.get("db", "Host")

    return login, password, database, host
