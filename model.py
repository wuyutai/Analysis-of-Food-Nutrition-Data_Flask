from flask import Flask
import pymysql
from sqlalchemy import create_engine

import config

manager = Flask(__name__)
# 打开数据库连接
db = pymysql.connect("127.0.0.1",config.username,config.password,config.db_name)
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/food')

