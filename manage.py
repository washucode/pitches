from flask_script import Manager , Server
from app import pitch_app,db



app=pitch_app()


manager =  Manager(app)
manager.add_command('server',Server(use_debugger=True))


@manager.shell
def  add_shell_context():
    return {'db':db}


if __name__=="__main__":
    manager.run()
