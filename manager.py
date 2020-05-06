from flask_cors import CORS

from api import food
from model import manager
CORS(manager, supports_credentials=True)  # 跨域
manager.register_blueprint(food.food_info)  # 后台登录
