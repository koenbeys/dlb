from datetime import datetime
from app import app, db



def create_users():
    """ Create users when app starts """
    from app.user.models import User, Role , UsersRoles

    # Create all tables
    db.create_all()

    # Adding role

    role = Role.query.filter(Role.name == 'admin').first()
    if not role:
        role = Role(name=u'admin', label=u'Admin')
        db.session.add(role)
    role = Role.query.filter(Role.name == 'admin').first()

    # Add users
    user = User.query.filter(User.email == "koen.beys@mow.vlaanderen.be").first()
    if not user:
        user = User(email="koen.beys@mow.vlaanderen.be",
                    username=u"appadmin",
                    first_name=u"Application admin",
                    last_name=u"Admin",
                    password=app.user_manager.hash_password("Borg2140"),
                    confirmed_at=datetime.utcnow(),
                    active=True)
        db.session.add(user)
    user = User.query.filter(User.email == u"koen.beys@mow.vlaanderen.be").first()

    usersroles = UsersRoles.query.filter(UsersRoles.user_id == user.id and UsersRoles.role_id == role.id).first()
    if not usersroles:
        usersroles = UsersRoles(user_id=user.id,
                                role_id=role.id)

        db.session.add(usersroles)
    usersroles = UsersRoles.query.filter(UsersRoles.user_id == user.id and UsersRoles.role_id == role.id).first()

    role = Role.query.filter(Role.name == 'controler').first()
    if not role:
        role = Role(name='controler', label=u'controler')
        db.session.add(role)
    role = Role.query.filter(Role.name == 'controler').first()

    # Add users
    user = User.query.filter(User.email == "appuser@mow.vlaanderen.be").first()
    if not user:
        user = User(email="appuser@mow.vlaanderen.be",
                    username="appuser",
                    first_name=u"Application User",
                    last_name=u"User",
                    password=app.user_manager.hash_password("Borg2140"),
                    confirmed_at=datetime.utcnow(),
                    active=True)
        db.session.add(user)
    user = User.query.filter(User.email == u"appuser@mow.vlaanderen.be").first()

    usersroles = UsersRoles.query.filter(UsersRoles.user_id == user.id and UsersRoles.role_id == role.id).first()
    if not usersroles:
        usersroles = UsersRoles(user_id=user.id,
                                role_id=role.id)
        db.session.add(usersroles)
    usersroles = UsersRoles.query.filter(UsersRoles.user_id == user.id and UsersRoles.role_id == role.id).first()

    role = Role.query.filter(Role.name == 'validator').first()
    if not role:
        role = Role(name='validator', label=u'Validator')
        db.session.add(role)
    role = Role.query.filter(Role.name == 'validator').first()

    # Add users
    user = User.query.filter(User.email == "appvalid@mow.vlaanderen.be").first()
    if not user:
        user = User(email="appvalid@mow.vlaanderen.be",
                    username="appvalid",
                    first_name=u"Application Valid",
                    last_name=u"Valid",
                    password=app.user_manager.hash_password("Borg2140"),
                    confirmed_at=datetime.utcnow(),
                    active=True)
        db.session.add(user)
    user = User.query.filter(User.email == u"appvalid@mow.vlaanderen.be").first()
    from flask_user import login_required, current_user
    current_user = User.query.filter(User.email == u"appvalid@mow.vlaanderen.be").first()

    usersroles = UsersRoles.query.filter(UsersRoles.user_id == user.id and UsersRoles.role_id == role.id).first()
    if not usersroles:
        usersroles = UsersRoles(user_id=user.id,
                                role_id=role.id)
        db.session.add(usersroles)
    usersroles = UsersRoles.query.filter(UsersRoles.user_id == user.id and UsersRoles.role_id == role.id).first()

    # Save to DB
    db.session.commit()
