from flask import redirect, render_template, request,url_for, flash
from flask_user import login_required,current_user,roles_accepted
from . import dlb
from .forms import StationListForm, TestForm, StationHQForm, StationYSIForm, histoHQForm, histoYSIForm

from app import app,db
from . import functions
from app.config import config

from datetime import datetime

#.functions import getStationList
# The Home page is accessible to anyone



@dlb.route('/user')
@login_required  # Limits access to authenticated users
def user_page():
    return render_template('main/user_page.html')

@dlb.route('/oproep')
def oproep_page():
    return render_template('main/oproep.html')


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
    from flask import flash
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if (file.filename.lower() != ""):
        if allowed_file(file.filename):
            # Make the filename safe, remove unsupported chars
            filename = file.filename
            # Move the file form the temporal folder to
            # the upload folder we setup
            file.save(os.path.join(app.config['DLB_UPLOAD_FOLDER'], filename))
            # Redirect the user to the uploaded_file route, which
            # will basicaly show on the browser the uploaded file
            functions.checkAndLoadFile(filename)
                #flash('Wrong file')
    #            file.save(os.path.join(app.config['DLB_TEMP_FOLDER'], filename))

            return render_template('uploadFile.html')
        else:
            flash("File not allowed to upload !")
            return render_template('uploadFile.html')
        #return redirect(url_for('main.test_page', txt=filename))
    else:
        print "no file selected"
        flash("No file selected !")
        return render_template('uploadFile.html')


@dlb.route('/uploadFile', methods=['GET', 'POST'])
@login_required
@roles_accepted('admin','validator')
def uploadFile_page():
   return render_template('uploadFile.html')





@dlb.route('/stationlist', methods=['GET', 'POST'])
@login_required

def stationlist_page():
    from flask import session
    from classes import stationItem
    form = StationListForm(request.form)
    if request.method == 'POST':
        if form.validate():
            print "StationListForm : ok"
            stationid = request.form.get('stationid')
            session['stationid'] = stationid

            isValidator = False


            print stationid
            op = request.form.get('op')
            if (op == "HQ"):
                return redirect(url_for('.stationHQ_page',stationid=stationid))
            elif (op == "YSI"):
                return redirect(url_for('.stationYSI_page', stationid=stationid))
            elif (op == "histoHQ"):
                return redirect(url_for('.histoHQ_page', stationid=stationid))
            elif (op == "histoYSI"):
                return redirect(url_for('.histoYSI_page', stationid=stationid))
        else:
            print "StationListForm : not ok"
            stationList = functions.getStationList()
            return render_template( 'stationlist.html', stationList=stationList, alert=True)

    stationList = functions.getStationList()
    #functions.isObserver()
    if 'stationid' not in session:
        session['stationid']="-1"
        station=stationItem()
    else:
        station = functions.getStationInfo(session['stationid'])

    return render_template('stationlist.html', stationList=stationList, station=station, alert=False)



@dlb.route('/histoHQ/<stationid>', methods=['GET', 'POST'])
def histoHQ_page(stationid):
    print "histoHQ_page page..."
    form = histoHQForm(request.form)
    if request.form.get('formname')=='histoHQ':
        if request.method == 'POST':
            if form.validate():
                print "histoHQ_page : ok"
                stationid = request.form.get('stationid')
                dtfrom = request.form.get('dtfrom')
                dtto = request.form.get('dtto')
                lstHistory = functions.getHistoryHQbyDates(stationid, dtfrom, dtto)
                ostation = functions.getStationInfo(stationid)
                return render_template('histoHQ.html', ostation=ostation, lstHistory=lstHistory, dtfrom=dtfrom, dtto=dtto)
            else:
                print "histoHQ_page : NOT ok"
                functions.flash_errors(form)
                stationid = request.form.get('stationid')

    lstHistory = functions.getHistoryHQ(stationid, app.config['DLB_NB_HISTO_HISTORY_ITEMS'])
    ostation = functions.getStationInfo(stationid)
    dtfrom = ""
    dtto = ""
    return render_template('histoHQ.html', ostation=ostation, lstHistory = lstHistory, dtfrom = dtfrom, dtto = dtto)


@dlb.route('/stationHQ/<stationid>', methods=['GET', 'POST'])
def stationHQ_page(stationid):
    from app import app, db
    from .models import historyItemsHQs
    from flask import  session
    print "stationHQ page..."

    form = StationHQForm(request.form)
    if request.form.get('formname')=='stationHQ':
        if request.method == 'POST':
            if form.validate():
                print "StationHQForm : ok"
                histo = historyItemsHQs()
                histo.stationid = request.form.get('stationid')
                ostation = functions.getStationInfo(histo.stationid)
                histo.sensorExNumber=ostation.sensorExNumber
                histo.gaugeExNumber=ostation.gaugeExNumber
                recTs = request.form.get('recTs')
                histo.recTs = datetime.strptime(recTs, '%d/%m/%Y %H:%M')
                histo.operator = current_user.username
                histo.observator = request.form.get('observator')
                if (histo.observator == ""):
                    histo.observator = histo.operator
                sensorTs = request.form.get('sensorTs')
                histo.sensorTs = datetime.strptime(sensorTs, '%d/%m/%Y %H:%M')
                histo.sensorValue = request.form.get('sensorValue')
                gaugeTs = request.form.get('gaugeTs')
                histo.gaugeTs = datetime.strptime(gaugeTs, '%d/%m/%Y %H:%M')
                histo.gaugeValue = request.form.get('gaugeValue')
                histo.sensorCleaned = request.form.get('sensorCleaned')
                histo.gaugeCleaned = request.form.get('gaugeCleaned')
                histo.sectionCleaned = request.form.get('sectionCleaned')
                histo.comment = request.form.get('comment')
                histo.deltaT = request.form.get('deltaT')

                histo.hardwareChanged = request.form.get('hardwareChanged')
                histo.hardwareNumberOld = request.form.get('hardwareNumberOld')
                histo.hardwareNumberNew = request.form.get('hardwareNumberNew')
                histo.hardwareReset = request.form.get('hardwareReset')
                histo.hardwareCalibrated = request.form.get('hardwareCalibrated')
                histo.hardwareConfigured = request.form.get('hardwareConfigured')

                db.session.add(histo)
                db.session.commit()
                flash("HQ logbook entry saved !", "success")
                functions.saveToZrxFileHQ(histo)
                print "historyItemsHQs inserted"
                stationList = functions.getStationList()
                station = functions.getStationInfo(session['stationid'])

                return render_template('stationlist.html', stationList=stationList, station=station)
            else:
                print "StationHQForm : NOT ok"
                functions.flash_errors(form)
                ostation = functions.getStationInfo(stationid)

                lstHistory = functions.getHistoryHQ(stationid, app.config['DLB_NB_STATION_HISTORY_ITEMS'])
                return render_template('stationHQ.html', ostation=ostation, lstHistory = lstHistory, form=form)

    lstHistory = functions.getHistoryHQ(stationid, app.config['DLB_NB_STATION_HISTORY_ITEMS'])
    ostation = functions.getStationInfo(stationid)

    return render_template('stationHQ.html', ostation=ostation, lstHistory = lstHistory, form=form)

@dlb.route('/histoYSI/<stationid>', methods=['GET', 'POST'])
def histoYSI_page(stationid):
    print "histoYSI_page page..."
    form = histoYSIForm(request.form)
    if request.form.get('formname')=='histoYSI':
        if request.method == 'POST':
            if form.validate():
                print "histoYSI_page : ok"
                stationid = request.form.get('stationid')
                dtfrom = request.form.get('dtfrom')
                dtto = request.form.get('dtto')
                lstHistory = functions.getHistoryYSIbyDates(stationid, dtfrom, dtto)
                ostation = functions.getStationInfo(stationid)
                return render_template('histoYSI.html', ostation=ostation, lstHistory=lstHistory, dtfrom=dtfrom, dtto=dtto,
                                       alert=False)

            else:
                print "histoUSI_page : NOT ok"
                stationid = request.form.get('stationid')

    lstHistory = functions.getHistoryYSI(stationid, app.config['DLB_NB_HISTO_HISTORY_ITEMS'])
    ostation = functions.getStationInfo(stationid)
    dtfrom = ""
    dtto = ""
    return render_template('histoYSI.html', ostation=ostation, lstHistory = lstHistory, dtfrom = dtfrom, dtto = dtto, alert=False)


@dlb.route('/stationYSI/<stationid>', methods=['GET', 'POST'])
def stationYSI_page(stationid):
    from app import app, db
    from .models import historyItemsYSIs
    from flask import session
    print "stationYSI page..."
    form = StationYSIForm(request.form)
    if request.form.get('formname')=='stationYSI':
        if request.method == 'POST':

            if form.validate():
                print "StationYSIForm : ok"
                histo = historyItemsYSIs()
                histo.stationid = request.form.get('stationid')
                ostation = functions.getStationInfo(histo.stationid)
                histo.sensorExNumber=ostation.sensorExNumber
                histo.gaugeExNumber=ostation.gaugeExNumber
                recTs = request.form.get('recTs')
                histo.recTs = datetime.strptime(recTs, '%d/%m/%Y %H:%M')
                histo.operator = current_user.username
                histo.observator = request.form.get('observator')
                if (histo.observator == ""):
                    histo.observator = histo.operator

                gaugeTs = request.form.get('gaugeTs')
                histo.gaugeTs = datetime.strptime(gaugeTs, '%d/%m/%Y %H:%M')
                histo.gaugeValue = request.form.get('gaugeValue')
                histo.gaugeCleaned = request.form.get('gaugeCleaned')
                histo.comment = request.form.get('comment')
                histo.deltaT = request.form.get('deltaT')

                histo.hardwareChanged = request.form.get('hardwareChanged')
                histo.hardwareNumberOld = request.form.get('hardwareNumberOld')
                hardwareTsOld = request.form.get('hardwareTsOld')
                histo.hardwareTsOld = datetime.strptime(hardwareTsOld, '%d/%m/%Y %H:%M')
                histo.hardwareNumberNew = request.form.get('hardwareNumberNew')
                hardwareTsNew = request.form.get('hardwareTsNew')
                histo.hardwareTsNew = datetime.strptime(hardwareTsNew, '%d/%m/%Y %H:%M')

                histo.hardwareCleaned = request.form.get('hardwareCleaned')
                histo.hardwareCalibrated = request.form.get('hardwareCalibrated')
                histo.samplesCollected = request.form.get('samplesCollected')
                histo.sectionCleaned = request.form.get('sectionCleaned')

                db.session.add(histo)
                db.session.commit()
                flash("Phys.Par. logbook entry saved !","success")
                print "historyItemsYSIs inserted"
                print stationid
                stationList = functions.getStationList()
                station = functions.getStationInfo(session['stationid'])
                return render_template('stationlist.html', stationList=stationList, station=station)
            else:
                print "StationYSIForm : NOT ok"
                ostation = functions.getStationInfo(stationid)
                lstHistory = functions.getHistoryYSI(stationid, app.config['DLB_NB_STATION_HISTORY_ITEMS'])
                functions.flash_errors(form)
                return render_template('stationYSI.html', ostation=ostation, lstHistory = lstHistory, form=form)

    lstHistory = functions.getHistoryYSI(stationid, app.config['DLB_NB_STATION_HISTORY_ITEMS'])
    ostation = functions.getStationInfo(stationid)
    return render_template('stationYSI.html', ostation=ostation, lstHistory = lstHistory, form=form)


@dlb.route('/test', methods=['GET', 'POST'])
def test_page():

    txt = "origin"
    return render_template('test.html', txt=txt)




# @dlb.route('/test', methods=['GET', 'POST'])
# def test_page():
#     form = TestForm(request.form)
#     if request.method == 'POST':
#         if form.validate():
#             # Copy form fields to user_profile fields
#
#             # Redirect to home page
#             txt = "pas d'erreur"
#             return render_template('test.html',txt = txt)
#         else:
#     # Process GET or invalid POST
#             txt = "error"
#             return render_template('test.html',txt=txt)
#
#
#     txt = "rien"
#     return render_template('test.html', txt=txt)


