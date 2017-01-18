
from . import log

#
# def is_safe_url(target):
#     from flask import request
#     from flask_admin._compat import urljoin, urlparse, iteritems
#     ref_url = urlparse(request.host_url)
#     test_url = urlparse(urljoin(request.host_url, target))
#     return (test_url.scheme in ('http', 'https') and
#             ref_url.netloc == test_url.netloc)

def getUserList():
    log.debug('def getStationList()')
    from .models import User
    tblUsers = User.query.filter(User.id >= 0)
    #    lstStations = []
    #    for station in tblStations:
    #        lstStations.append(getStationInfo(station.stationid))
    return tblUsers

def getUserDetail(id):
    log.debug('def getUserDetail()')
    from .models import User
    if (id > -1):
        cuser = User.query.filter(User.id == id).first()
        print cuser.username
    else:
        cuser = User()
        cuser.username = ""
        cuser.first_name = ""
        cuser.last_name = ""
        cuser.email = ""
        cuser.gsmnr = ""
        cuser.is_active = True
        cuser.id = -1
    return cuser

def setUser(id, username, first_name, last_name, email, gsmnr, active):
    log.debug('def setUser()')
    from .models import User
    from app import app, db
    if (int(id) == -1):
        cuser = User()
    else:
        cuser = User.query.filter(User.id == int(id)).first()

    cuser.username = username.strip()
    cuser.first_name = first_name.strip()
    cuser.last_name = last_name.strip()
    cuser.email = email.strip()
    cuser.gsmnr = gsmnr.strip()
    cuser.is_active = active

    if (id == -1):
        db.session.add(cuser)
    #cuser.save()
    db.session.commit()
    return cuser.id

def getUserRoles(id):
    log.debug('def getUserRoles()')
    from .models import UsersRoles, Role
    tblRoleDescs = []
    tblRole = Role.query.filter(Role.id >= 0)
    for cRole in tblRole:
        tblRoleDesc = []
        tblRoleDesc.append(cRole.id)
        tblRoleDesc.append(cRole.name)
        tblRoleDesc.append(cRole.label)
        urole = UsersRoles.query.filter(UsersRoles.role_id == cRole.id, UsersRoles.user_id == id )
        if urole.count() == 0:
            tblRoleDesc.append(False)
        else:
            tblRoleDesc.append(True)
        tblRoleDescs.append(tblRoleDesc)
    return tblRoleDescs

def setUserRoles(userid,newRoles):
    log.debug('def setUserRoles()')
    from .models import UsersRoles, Role
    from app import app, db
    print userid
    for record in db.session.query(UsersRoles).filter(UsersRoles.user_id == int(userid)):
        db.session.delete(record)

    db.session.commit()
    for record in UsersRoles.query.filter(UsersRoles.user_id == userid).all():
        db.session.delete(record)

    for newr in newRoles.split(";"):
        ur = UsersRoles(user_id=int(userid),
                        role_id=int(newr))
        db.session.add(ur)
        db.session.commit()
