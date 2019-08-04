## 启动
* set ops_config=local&&python manager.py runserver
## flask-sqlacodegen用法
* flask-sqlacodegen "mysql://root:@127.0.0.1/food_db" --outfile "common/models/model.py"  --flask

* flask-sqlacodegen "mysql://root:@127.0.0.1/food_db" --tables user --outfile "common/models/user.py"  --flask
