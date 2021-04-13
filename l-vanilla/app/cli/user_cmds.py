

import os
import click

from app.cli import user_cli

from app.exts.database import db
from app.models.user import User, Role


@user_cli.cli.command('drop-all')
def drop_all_colection():
    """Drop All Collection"""
    collections = db.get_db().list_collection_names()
    for collection in collections:
        db.get_db().drop_collection(collection)
    print('All Collections Record DELETED.')


@ user_cli.cli.command('drop-user')
def drop_colection():
    """Drop User Collection"""
    User.drop_collection()
    print('All Users Record DELETED.')


@ user_cli.cli.command('add-role')
@ click.argument('name')
def add_role(name):
    """ Add New User Role """
    r = Role()
    r.set_name(name)
    r.set_slug(name)
    r.description = 'Default Description'
    r.save()

    print(r.__repr__())
