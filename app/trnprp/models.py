from flask_user import UserMixin
from app import db

class cust(db.Model, UserMixin):
    __tablename__ = 'cust'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    last_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')


    active = db.Column(db.Boolean(), nullable=False, server_default='0')



