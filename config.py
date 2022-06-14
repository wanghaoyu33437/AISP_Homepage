class BaseConfig(object):

    # 数据库的配置
    DIALCT = "mysql"
    DRITVER = "pymysql"
    HOST = 'localhost'
    PORT = "3306"
    USERNAME = "root"
    PASSWORD = "1234"
    DBNAME = 'aisp'

    SQLALCHEMY_DATABASE_URI = f"{DIALCT}+{DRITVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'TPmi4aLWRbyVq8zu9v82dWYW1'