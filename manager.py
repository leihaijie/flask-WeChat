from application import app,manager
from flask_script import Server
from jobs.launcher import runJob
import www

# web server
manager.add_command("runserver", Server(host="0.0.0.0", port=app.config['SERVER_PORT'], use_debugger=True,))

# job entrance
manager.add_command("runjob", runJob())

def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())  # 0正常退出,其他不正常退出捕获异常
    except Exception as e:
        import traceback  # 捕获异常那个文件哪一行
        traceback.print_exc()