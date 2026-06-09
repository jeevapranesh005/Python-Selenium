from configparser import ConfigParser

def get_config(category, key):
    config = ConfigParser()
    config.read("D:\python selenium-D\PY_pytest\TutuorialNinja_DataDriven\config.ini")
    return config.get(category, key)