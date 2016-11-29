from flask import redirect, render_template, render_template_string, Blueprint,request,url_for
from flask_user import login_required,current_user
from app import main
from .forms import TestForm, StationHQForm, StationYSIForm, StationListForm,histoHQForm
from app import db, app
from .functions import *
from app.dlb import functions
from app.config import config
from . import dlb



@dlb.route('/oproep')
def oproep_page():
    return render_template('dlb/oproep.html')


# app.config['UPLOAD_FOLDER'] = 'uploads/'
# app.config['DOWNLOAD_FOLDER'] = 'downloads/'
# app.config['STATIONLIST_FILENAME'] = "stations.txt"

# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

import os
# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded

# Route that will process the file upload
@dlb.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = file.filename
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['DLB_UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        print filename
        return render_template('dlb/uploadfile.html', txt=filename)
        #return redirect(url_for('dlb.test_page', txt=filename))


@dlb.route('/uploadfile', methods=['GET', 'POST'])
def uploadfile_page():
    txt = ""
    return render_template('dlb/uploadfile.html', txt=txt)

@dlb.route('/userList', methods=['GET', 'POST'])
def userList_page():
    form = userListForm(request.form)
    if request.method == 'POST':
        if form.validate():
            print "Userlistform : ok"
            userid1 = request.form.get('userid')
            print userid1
            if (int(userid1) > 0):
            #user = functions.getUserDetail(userid)
                return redirect(url_for('dlb.userdetail_page', userid = userid1))
            else:
                return redirect(url_for('dlb.newuser_page'))
        else:
            print "Userlistform : not ok"
            userList = functions.getUserList()
            return render_template( 'dlb/userlist.html', tableList=userList, alert=True)

    userList = functions.getUserList()
    print "oooo"
    return render_template('dlb/userList.html', tableList=userList, alert=False)

@dlb.route('/newuser', methods=['GET', 'POST'])
def newuser_page():
    form = userdetailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            print "newuser : ok"
            userid = request.form.get('userid')
            newRoles = request.form.get('newRoles')
            functions.setUserRoles(int(userid),newRoles)
            print "roles updated"
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')
            gsmnr = request.form.get('gsmnr')
            active = request.form.get('active')
            username = request.form.get('username')

            inewuser = functions.setUser(int(userid),username,first_name,last_name,email,gsmnr,active)
            functions.setUserRoles(int(inewuser),newRoles)
            userList = functions.getUserList()
            return render_template('dlb/userList.html', tableList=userList, alert=False)
        else:
            print "newuser : NOT ok"
            print "newuser requets"
            cuser = functions.getUserDetail(-1)
            croles = functions.getUserRoles(-1)
            return render_template('dlb/userdetail.html', cuser=cuser, croles = croles, alert=True)


    print "newuser requets"
    cuser = functions.getUserDetail(-1)
    croles = functions.getUserRoles(-1)
    return render_template('dlb/userdetail.html', cuser=cuser, croles = croles, alert=False)



@dlb.route('/userdetail/<userid>', methods=['GET', 'POST'])
def userdetail_page(userid):
    form = userdetailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            print "userdetailForm : ok"
            userid = request.form.get('userid')
            newRoles = request.form.get('newRoles')
            functions.setUserRoles(int(userid),newRoles)
            print "roles updated"
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')
            gsmnr = request.form.get('gsmnr')
            active = request.form.get('active')
            username = request.form.get('username')

            functions.setUser(int(userid),username,first_name,last_name,email,gsmnr,active)
            userList = functions.getUserList()
            return render_template('dlb/userList.html', tableList=userList, alert=False)
        else:
            print "userdetailForm : NOT ok"
            print "userdetail requets"
            cuser = functions.getUserDetail(userid)
            croles = functions.getUserRoles(userid)
            return render_template('dlb/userdetail.html', cuser=cuser, croles = croles, alert=True)


    print "userdetail requets"
    cuser = functions.getUserDetail(userid)
    croles = functions.getUserRoles(userid)
    return render_template('dlb/userdetail.html', cuser=cuser, croles = croles, alert=False)


@dlb.route('/stationlist', methods=['GET', 'POST'])
def stationlist_page():
    print "stationlist_page():"
    form = StationListForm(request.form)
    if request.method == 'POST':
        if form.validate():
            print "StationListForm : ok"
            stationid = request.form.get('stationid')
            print stationid
            op = request.form.get('op')
            if (op == "HQ"):
                #stationHQ_page(stationid)
                # return stationHQ_page(stationid)
                return redirect(url_for('dlb.stationHQ_page',stationid=stationid))
            elif (op == "YSI"):
                    #stationYSI_page(stationid)
                    # return stationHQ_page(stationid)
                return redirect(url_for('dlb.stationYSI_page', stationid=stationid))
            elif (op == "histoHQ"):
                    #stationCTD_page(stationid)
                    # return stationHQ_page(stationid)
                return redirect(url_for('dlb.histoHQ_page', stationid=stationid))
            elif (op == "histoYSI"):
                return redirect(url_for('dlb.histoYSI_page', stationid=stationid))
                        #
            # lst = functions.getStationInfo(stationid)
            # lstHistory = functions.getHistoryHQs(stationid)
            # return render_template('dlb/stationHQ.html', lst=lst, lstHistory = lstHistory)   #, ii = ii)
        else:
            print "StationListForm : not ok"
            stationList = functions.getStationList()
            return render_template( 'dlb/stationlist.html', stationList=stationList, alert=True)

    stationList = functions.getStationList()
    functions.loadStationListFromFile()             #"c:\\temp\\stations.txt")
    print stationList[1].stationid
    return render_template('dlb/stationlist.html', stationList=stationList, alert=False)


from datetime import datetime

@dlb.route('/histoHQ/<stationid>', methods=['GET', 'POST'])
def histoHQ_page(stationid):
    print "histoHQ_page page..."
    form = histoHQForm(request.form)
    if request.method == 'POST':
        if form.validate():
            print "histoHQ_page : ok"
            stationid = request.form.get('stationid')
            dtfrom = request.form.get('dtfrom')
            dtto = request.form.get('dtto')
            lstHistory = functions.getHistoryHQbyDates(stationid, dtfrom, dtto)
            ostation = functions.getStationInfo(stationid)
            return render_template('dlb/histoHQ.html', ostation=ostation, lstHistory=lstHistory, dtfrom=dtfrom, dtto=dtto,
                                   alert=False)

        else:
            print "histoHQ_page : NOT ok"
            stationid = request.form.get('stationid')

    lstHistory = functions.getHistoryHQ(stationid, 20)
    ostation = functions.getStationInfo(stationid)
    dtfrom = ""
    dtto = ""
    return render_template('dlb/histoHQ.html', ostation=ostation, lstHistory = lstHistory, dtfrom = dtfrom, dtto = dtto, alert=False)


@dlb.route('/stationHQ/<stationid>', methods=['GET', 'POST'])
def stationHQ_page(stationid):
    print "stationHQ page..."
    form = StationHQForm(request.form)
    if request.method == 'POST':
        if form.validate():
            print "StationHQForm : ok"
            stationid = request.form.get('stationid')
            #stationExNumber = request.form.get('stationExNumber')
            recTs = request.form.get('recTs')
            dtrecTs = datetime.strptime(recTs,'%d/%m/%Y %H:%M')
            observator = request.form.get('observator')
            sensorTs = request.form.get('sensorTs')
            dtsensorTs = datetime.strptime(sensorTs,'%d/%m/%Y %H:%M')
            sensorValue = request.form.get('sensorValue')
            gaugeTs = request.form.get('gaugeTs')
            dtgaugeTs = datetime.strptime(gaugeTs,'%d/%m/%Y %H:%M')
            gaugeValue = request.form.get('gaugeValue')
            sensorCleaned = request.form.get('sensorCleaned')
            gaugeCleaned = request.form.get('gaugeCleaned')
            sectionCleaned = request.form.get('sectionCleaned')
            comment = request.form.get('comment')
            deltaT =  request.form.get('deltaT')

            hardwareChanged = request.form.get('hardwareChanged')
            hardwareNumberOld = request.form.get('hardwareNumberOld')
            hardwareNumberNew = request.form.get('hardwareNumberNew')
            hardwareReset = request.form.get('hardwareReset')
            hardwareCalibrated = request.form.get('hardwareCalibrated')
            hardwareConfigured = request.form.get('hardwareConfigured')

            ostation = functions.getStationInfo(stationid)
            operator = "me"
            if (observator == ""):
                observator = operator

            from app import app, db
            from app.main.models import historyItemsHQs
            histo = historyItemsHQs(stationid=stationid,
                                    sensorExNumber=ostation.sensorExNumber,
                                    gaugeExNumber=ostation.gaugeExNumber,
                                    recTs=dtrecTs,
                                    deltaT=deltaT,
                                    operator=operator,
                                    observator=observator,
                                    sensorTs=dtsensorTs,
                                    sensorValue=sensorValue,
                                    gaugeTs=dtgaugeTs,
                                    gaugeValue=gaugeValue,
                                    sensorCleaned=sensorCleaned,
                                    gaugeCleaned=gaugeCleaned,
                                    sectionCleaned=sectionCleaned,
                                    hardwareChanged=hardwareChanged,
                                    hardwareNumberOld=hardwareNumberOld,
                                    hardwareNumberNew=hardwareNumberNew,
                                    hardwareReset=hardwareReset,
                                    hardwareConfigured=hardwareConfigured,
                                    hardwareCalibrated=hardwareCalibrated,
                                    comment=comment
                                    )

            db.session.add(histo)
            db.session.commit()
            functions.saveToZrxFileHQ(histo)
            print "historyItemsHQs inserted"
            stationList = functions.getStationList()

            return render_template('dlb/stationlist.html', stationList=stationList, alert=False)
        else:
            print "StationHQForm : NOT ok"
            ostation = functions.getStationInfo(stationid)
            lstHistory = functions.getHistoryHQ(stationid, 5)
            return render_template('dlb/stationHQ.html', ostation=ostation, lstHistory = lstHistory, alert=True)

    lstHistory = functions.getHistoryHQ(stationid, 5)
    ostation = functions.getStationInfo(stationid)
    return render_template('dlb/stationHQ.html', ostation=ostation, lstHistory = lstHistory, alert=False)

@dlb.route('/histoYSI/<stationid>', methods=['GET', 'POST'])
def histoYSI_page(stationid):
    print "histoYSI_page page..."
    form = histoYSIForm(request.form)
    if request.method == 'POST':
        if form.validate():
            print "histoYSI_page : ok"
            stationid = request.form.get('stationid')
            dtfrom = request.form.get('dtfrom')
            dtto = request.form.get('dtto')
            lstHistory = functions.getHistoryYSIbyDates(stationid, dtfrom, dtto)
            ostation = functions.getStationInfo(stationid)
            return render_template('dlb/histoYSI.html', ostation=ostation, lstHistory=lstHistory, dtfrom=dtfrom, dtto=dtto,
                                   alert=False)

        else:
            print "histoUSI_page : NOT ok"
            stationid = request.form.get('stationid')

    lstHistory = functions.getHistoryYSI(stationid, 20)
    ostation = functions.getStationInfo(stationid)
    dtfrom = ""
    dtto = ""
    return render_template('dlb/histoYSI.html', ostation=ostation, lstHistory = lstHistory, dtfrom = dtfrom, dtto = dtto, alert=False)


@dlb.route('/stationYSI/<stationid>', methods=['GET', 'POST'])
def stationYSI_page(stationid):
    print "stationYSI page..."
    form = StationYSIForm(request.form)
    if request.method == 'POST':
        if form.validate():
            print "StationYSIForm : ok"
            stationid = request.form.get('stationid')
            observator = request.form.get('observator')
            recTs = request.form.get('recTs')
            dtrecTs = datetime.strptime(recTs,'%d/%m/%Y %H:%M')
            gaugeTs = request.form.get('gaugeTs')
            dtgaugeTs = datetime.strptime(gaugeTs,'%d/%m/%Y %H:%M')
            gaugeValue = request.form.get('gaugeValue')
            comment = request.form.get('comment')
            deltaT = request.form.get('deltaT')


            hardwareChanged = request.form.get('hardwareChanged')
            hardwareNumberOld = request.form.get('hardwareNumberOld')
            hardwareTsOld = request.form.get('hardwareTsOld')
            dthardwareTsOld = datetime.strptime(hardwareTsOld,'%d/%m/%Y %H:%M')
            hardwareNumberNew = request.form.get('hardwareNumberNew')
            hardwareTsNew = request.form.get('hardwareTsNew')
            dthardwareTsNew = datetime.strptime(hardwareTsNew,'%d/%m/%Y %H:%M')


            hardwareCleaned = request.form.get('hardwareCleaned')
            hardwareCalibrated = request.form.get('hardwareCalibrated')
            samplesCollected = request.form.get('samplesCollected')
            sectionCleaned = request.form.get('sectionCleaned')

            ostation = functions.getStationInfo(stationid)
            operator = "me"
            if (observator == ""):
                observator = operator

            from app import app, db
            from app.main.models import historyItemsYSIs
            histo = historyItemsYSIs(stationid=stationid,
                                    recTs = dtrecTs,
                                    deltaT = deltaT,
                                    operator = operator,
                                    observator = observator,
                                    gaugeExNumber = ostation.gaugeExNumber,
                                    gaugeTs = dtgaugeTs,
                                    gaugeValue = gaugeValue,
                                    hardwareChanged = hardwareChanged,
                                    hardwareNumberOld = hardwareNumberOld,
                                    hardwareTsOld = dthardwareTsOld,
                                    hardwareNumberNew = hardwareNumberNew,
                                    hardwareTsNew = dthardwareTsNew,
                                    hardwareCleaned = hardwareCleaned,
                                    hardwareCalibrated = hardwareCalibrated,
                                    samplesCollected = samplesCollected,
                                    sectionCleaned = sectionCleaned,
                                    comment = comment
                                    )
            db.session.add(histo)
            db.session.commit()
            print "historyItemsYSIs inserted"
            print stationid
            stationList = functions.getStationList()
            return render_template('dlb/stationlist.html', stationList=stationList, alert=False)
        else:
            print "StationYSIForm : NOT ok"
            ostation = functions.getStationInfo(stationid)
            lstHistory = functions.getHistoryYSI(stationid, 5)
            return render_template('dlb/stationYSI.html', ostation=ostation, lstHistory = lstHistory, alert=True)

    lstHistory = functions.getHistoryYSI(stationid, 5)
    ostation = functions.getStationInfo(stationid)
    return render_template('dlb/stationYSI.html', ostation=ostation, lstHistory = lstHistory, alert=False)


@dlb.route('/test', methods=['GET', 'POST'])
def test_page():

    txt = "origin"
    return render_template('dlb/test.html', txt=txt)

# @dlb.route('/test', methods=['GET', 'POST'])
# def test_page():
#     form = TestForm(request.form)
#     if request.method == 'POST':
#         if form.validate():
#             # Copy form fields to user_profile fields
#
#             # Redirect to home page
#             txt = "pas d'erreur"
#             return render_template('dlb/test.html',txt = txt)
#         else:
#     # Process GET or invalid POST
#             txt = "error"
#             return render_template('dlb/test.html',txt=txt)
#
#
#     txt = "rien"
#     return render_template('dlb/test.html', txt=txt)
