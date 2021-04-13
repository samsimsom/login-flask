

from flask import Blueprint

app_cli = Blueprint('app_cli', __name__, cli_group='app_cli')
user_cli = Blueprint('user_cli', __name__, cli_group='user_cli')


def load_cmds():
    from app.cli import app_cmds
    from app.cli import user_cmds


load_cmds()
