from werkzeug.utils import secure_filename
from application import app, db
from common.libs.Helper import getCurrentDate
import os, stat, uuid
from common.models.food.Image import Image


class UploadService():
    @staticmethod
    def uploadByFile(file):
        config_upload  = app.config['UPLOAD']
        resp = {"code": 200, "msg":"操作成功~~", "data":{}}
        filename  = secure_filename(file.filename)         # 获取安全的文件名
        ext = filename.split(".",1)[1]
        # app.logger.error(ext)
        if ext not in config_upload['ext']:
            resp['code']= -1
            resp['msg'] = "不允许的扩展类型文件"
            return resp

        root_path = app.root_path + config_upload['prefix_path']
        file_dir= getCurrentDate("%Y%m%d")
        save_dir = root_path + file_dir
        if  not os.path.exists(save_dir):
            os.mkdir(save_dir)
            os.chmod(save_dir, stat.S_IRWXU | stat.S_IRGRP | stat.S_IRWXO)

        filename = str(uuid.uuid4()).replace("-", "") + "."  + ext
        file.save("{0}/{1}".format(save_dir, filename))

        model_image = Image()
        model_image.file_key = file_dir + "/" + filename
        model_image.created_time = getCurrentDate()
        db.session.add(model_image)
        db.session.commit()

        resp['data'] = {
            'file_key': model_image.file_key
        }
        return resp