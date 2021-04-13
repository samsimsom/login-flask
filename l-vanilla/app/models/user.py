

from datetime import datetime
from slugify import slugify

from werkzeug.security import generate_password_hash, check_password_hash
from app.exts.database import db


class Role(db.Document):
    name = db.StringField(max_length=64, required=True, unique=True)
    description = db.StringField(max_length=128)
    slug = db.StringField(max_length=128)
    creation_date = db.DateTimeField(default=datetime.utcnow())

    meta = {'collection': 'role', 'indexes': ['name', '-creation_date']}

    def __init__(self, *args, **values):
        super().__init__(*args, **values)
        # print('-- ROLE MODEL --')

    def __repr__(self) -> str:
        return f'<Role | name: {self.name}, description: {self.description}>'

    def set_name(self, name):
        self.name = (str(name).replace(' ', '')).upper()

    def set_slug(self, name):
        self.slug = slugify(name)


class User(db.Document):
    username = db.StringField(max_length=64, required=True, unique=True)
    email = db.EmailField(max_length=128, required=True, unique=True)
    password_hash = db.StringField(max_length=128, required=True)
    slug = db.StringField(max_length=128)
    role = db.ReferenceField(Role, reverse_delete_rule=db.CASCADE)
    creation_date = db.DateTimeField(default=datetime.utcnow())

    meta = {'collection': 'user', 'indexes': ['username',
                                              'email',
                                              '-creation_date']}

    def __init__(self, *args, **values):
        super().__init__(*args, **values)
        # print('-- USER MODEL --')

    def __repr__(self) -> str:
        return f'<User | username: {self.username}, email: {self.email}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)

    def set_slug(self, username):
        self.slug = slugify(username)

    def set_username(self, username):
        self.username = (str(username).replace(' ', '')).lower()

    def set_email(self, email):
        self.email = str(email).lower()
