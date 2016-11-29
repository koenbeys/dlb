from datetime import datetime
from app import app, db



def create_users():
    """ Create users when app starts """
    from app.main.models import User, Role , UsersRoles

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
                    active=True)
        db.session.add(user)
    user = User.query.filter(User.email == u"koen.beys@mow.vlaanderen.be").first()

    usersroles = UsersRoles.query.filter(UsersRoles.user_id == user.id and UsersRoles.role_id == role.id).first()
    if not usersroles:
        usersroles = UsersRoles(user_id=user.id,
                                role_id=role.id)

        db.session.add(usersroles)
    usersroles = UsersRoles.query.filter(UsersRoles.user_id == user.id and UsersRoles.role_id == role.id).first()

    # Save to DB
    db.session.commit()
