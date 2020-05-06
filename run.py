from manager import manager
from flask_script import Manager, Shell

flaskScript = Manager(manager)  # 注册一个manager实例，自带runserver命令


def make_shell_context():
    return dict(app=manager)

flaskScript.add_command("shell", Shell(make_context=make_shell_context))

@flaskScript.command
def deploy():
    pass

if __name__ == '__main__':
    flaskScript.run()
