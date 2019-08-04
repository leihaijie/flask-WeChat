SERVER_PORT = 8000
DEBUG = False
SQLALCHEMY_ECHO = False
AUTH_COOKIE_NAME = "mooc_food"
JSON_AS_ASCII = False     # Chrome浏览器返回值看到中文而不是编码


# 过滤url
IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

# 分页
PAGE_SIZE = 5
PAGE_DISPLAY = 10
# 状态
STATUS_MAPPING = {
    "1": "正常",
    "0": "已删除"
}
# 小程序配置
MINA_APP = {
    'appid': 'wxdb7209d47a0ef002',
    'appkey': 'c90def6cefe741d6edb434bce867ae6d',
    'paykey':'',# 商户秘钥
    'mch_id':'',# 商户信息
    'callback_url':'/api/order/callback'
}
# 图片上传配置
UPLOAD =  {
    'ext':['jpg', 'gif', 'bmp', 'jpeg', 'png'],
    'prefix_path':'/web/static/upload/',
    'prefix_url':'/static/upload/',
}
APP = {
    'domain':'http://127.0.0.1:8000'
}
API_IGNORE_URLS = [
    "^/api"
]
# 支付状态值
PAY_STATUS_DISPLAY_MAPPING={
    "0":"订单关闭",
    "1":"支付成功",
    "-8":"待支付",
    "-7":"代发货",
    "-6":"待确认",
    "-5":"待评价"
}
PAY_STATUS_MAPPING={
    "1": "已支付 ",
    "-8": "待支付",
    "0": "已关闭 ",
}