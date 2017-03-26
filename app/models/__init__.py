# coding=utf-8

from flask_principal import RoleNeed, Permission, identity_loaded


_user_role = RoleNeed('user')
user_permission = Permission(_user_role)

_mender_role = RoleNeed('mender')
mender_permission = Permission(_mender_role)

_admin_role = RoleNeed('admin')
admin_permission = Permission(_admin_role)


from app.utils.constants import USER_PREFIX, MENDER_PREFIX, ADMIN_PREFIX


def identity_config(app):
    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        identity_id = str(identity.id)
        if identity_id:
            if identity_id.startswith(USER_PREFIX):
                identity.provides.add(_user_role)
            elif identity_id.startswith(MENDER_PREFIX):
                identity.provides.add(_mender_role)
            elif identity_id.startswith(ADMIN_PREFIX):
                identity.provides.add(_admin_role)


from app import login_manager
from app.models.User import User


@login_manager.user_loader
def load_user(user_id):
    user_id = user_id.rpartition(':')[-1]
    return User.query.get(int(user_id))


from app import db


def generate_fake(count=100):
    from sqlalchemy.exc import IntegrityError
    from random import seed
    import forgery_py

    seed()

    for i in xrange(count):
        try:
            u = User(email=forgery_py.internet.email_address(),
                     username=forgery_py.internet.user_name(True),
                     password=forgery_py.lorem_ipsum.word(),
                     confirmed=True,
                     name=forgery_py.name.full_name(),
                     location=forgery_py.address.city(),
                     about_me=forgery_py.lorem_ipsum.sentence(),
                     member_since=forgery_py.date.date(True))
            db.session.add(u)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
