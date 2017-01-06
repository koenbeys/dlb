
from . import classes


def isObserver():
    return False

def getStationList():
    from .models import Stations
    tblStations = Stations.query.filter(Stations.stationname >= '')
#    lstStations = []
#    for station in tblStations:
#        lstStations.append(getStationInfo(station.stationid))
    return tblStations

def getStationInfo(stationname):
    from .models import Stations
    recstation = Stations.query.filter(Stations.stationname == stationname).first()
    # ostation = classes.stationItem()
    # ostation.stationid = recstation.stationid
    # ostation.stationname = recstation.stationname
    # ostation.stationdescription = recstation.stationdescription
    # ostation.stationExNumber = recstation.stationExNumber
    return recstation

def getHistoryHQ(stationname, limit):
    from .models import historyItemsHQs
    tblHistory = historyItemsHQs.query.filter(historyItemsHQs.stationname == stationname).order_by('-id').limit(limit)
    return tblHistory

def getHistoryHQbyDates(stationname,dtfrom,dtto):
    from datetime import datetime, timedelta
    from .models import historyItemsHQs
    dtdtfrom = datetime.strptime(dtfrom, '%d/%m/%Y')
    dtdtto = datetime.strptime(dtto, '%d/%m/%Y')
    dtdtto =dtdtto + timedelta(days=1)
    tblHistory = historyItemsHQs.query.filter(historyItemsHQs.stationname == stationname, historyItemsHQs.recTs >= dtdtfrom, historyItemsHQs.recTs <= dtdtto).order_by('-id')
    return tblHistory


def saveToZrxFileHQ(rec):
    #will write "historyItemsHQs" record into "rec.id".zrx in "DOWNLOAD_FOLDER"
    import os
    from app import app
    from datetime import datetime


    if (app.config['DLB_GAUGE_TO_ZRX'] == True):
        filename = rec.gaugeExNumber + "_" + str(rec.id) + "." + app.config['DLB_ZRX_FILE_EXTENSION']

        filename = os.path.join(app.config['DLB_ZRX_FOLDER'], filename)
        f = open(filename, 'w')
        f.write('#ZRXPVERSION3014.03|*|WiLiWebSite|*|' + '\n')
        f.write("#REXCHANGE" +rec.gaugeExNumber + "|*|TZUTC+1|*|CUNITm|*|" + '\n')
        f.write("#LAYOUT(timestamp,value,remark)|*|" + '\n')
        f.write(datetime.strftime(rec.gaugeTs, '%Y%m%d%H%M') + '\t' + "%.2f" % (rec.gaugeValue) + "\t" + '"' + rec.comment + '"' + '\n')
        f.close()


    if (app.config['DLB_SENSOR_TO_ZRX'] == True):
        filename = rec.sensorExNumber + "_" + str(rec.id) + "." + app.config['DLB_ZRX_FILE_EXTENSION']

        filename = os.path.join(app.config['DLB_ZRX_FOLDER'], filename)
        f = open(filename, 'w')
        f.write('#ZRXPVERSION3014.03|*|WiLiWebSite|*|' + '\n')
        f.write("#REXCHANGE" + rec.sensorExNumber + "|*|TZUTC+1|*|CUNITm|*|" + '\n')
        f.write("#LAYOUT(timestamp,value,remark)|*|" + '\n')
        f.write(datetime.strftime(rec.sensorTs, '%Y%m%d%H%M') + '\t' + "%.2f" % (
        rec.sensorValue) + "\t" + '"' + rec.comment + '"' + '\n')
        f.close()


def getHistoryYSI(stationname, limit):
    from .models import historyItemsYSIs
    tblHistory = historyItemsYSIs.query.filter(historyItemsYSIs.stationname == stationname).order_by('-id').limit(limit)
    return tblHistory

def getHistoryYSIbyDates(stationname,dtfrom,dtto):
    from datetime import datetime, timedelta
    from .models import historyItemsYSIs
    dtdtfrom = datetime.strptime(dtfrom, '%d/%m/%Y')
    dtdtto = datetime.strptime(dtto, '%d/%m/%Y')
    dtdtto =dtdtto + timedelta(days=1)
    tblHistory = historyItemsYSIs.query.filter(historyItemsYSIs.stationname == stationname, historyItemsYSIs.recTs >= dtdtfrom, historyItemsYSIs.recTs <= dtdtto).order_by('-id')
    return tblHistory

def saveToZrxFileHQ(rec):
    #will write "historyItemsHQs" record into "rec.id".zrx in "DOWNLOAD_FOLDER"
    import os
    from app import app
    from datetime import datetime


    if (app.config['DLB_GAUGE_TO_ZRX'] == True):
        filename = rec.gaugeExNumber + "_" + str(rec.id) + "." + app.config['DLB_ZRX_FILE_EXTENSION']

        filename = os.path.join(app.config['DLB_ZRX_FOLDER'], filename)
        f = open(filename, 'w')
        f.write('#ZRXPVERSION3014.03|*|WiLiWebSite|*|' + '\n')
        f.write("#REXCHANGE" +rec.gaugeExNumber + "|*|TZUTC+1|*|CUNITm|*|" + '\n')
        f.write("#LAYOUT(timestamp,value,remark)|*|" + '\n')
        f.write(datetime.strftime(rec.gaugeTs, '%Y%m%d%H%M') + '\t' + "%.2f" % (rec.gaugeValue) + "\t" + '"' + rec.comment + '"' + '\n')
        f.close()

def checkAndLoadFile(filename):
    from app import app
    from flask import flash
    import os
    bRet = False
    if (filename == app.config['DLB_STATIONLIST_FILENAME']):
        bRet = loadStationListFile()
    else:
        flash(filename + ': unknown file name', "error")
        bRet = False
    if bRet:
        flash(filename + ": loaded successfully !", "success")
    return bRet


def loadStationListFile():
    from flask import flash
    from app import app, db
    from .models import Stations
    import os
    import datetime
    bRet = True
    filename = os.path.join(app.config['DLB_UPLOAD_FOLDER'], app.config['DLB_STATIONLIST_FILENAME'])
    print "checkStationListFile"
    if os.path.exists(filename):
        with open(filename,"r") as inputFile:
            bRet = True
            for line in inputFile.readlines():
                if (len(line.split(";")) <> 6):
                    bRet = False
                else:
                    buf = line.split(";")
                    try:
                        if (int(buf[4]) <> 0 and int(buf[4]) <> 1 ):
                            bRet = False

                        if (int(buf[5]) <> 0 and int(buf[5]) <> 1 ):
                            bRet = False
                    except:
                        bRet = False

            inputFile.close
        if not bRet:
            flash("Invalid value in latest two fields","error")

        if bRet:
            for record in db.session.query(Stations).all():
                db.session.delete(record)

            db.session.commit()

            with open(filename, "r") as inputFile:
                for line in inputFile.readlines():
                    buf = line.split(";")
                    station = classes.stationItem()
                    # station.stationid = buf[0]
                    station.stationname = buf[1]
                    station.gaugeExNumber = buf[2]
                    station.sensorExNumber = buf[2][:-1] + "s"
                    station.stationdescription = buf[3]
                    station.stationHQ = int(buf[4])
                    station.stationYSI = int(buf[5])
                    record = Stations(  #stationid=station.stationid,
                                      sensorExNumber=station.sensorExNumber,
                                      gaugeExNumber=station.gaugeExNumber,
                                      stationname=station.stationname,
                                      stationdescription=station.stationdescription,
                                      stationHQ=station.stationHQ,
                                      stationYSI=station.stationYSI
                                      )
                    db.session.add(record)

                db.session.commit()
                inputFile.close()


            ts = datetime.datetime.now()
            st = datetime.datetime.now().strftime("%Y%m%d%H%M")
            newfilename = os.path.join(app.config['DLB_BACKUP_FOLDER'],
                                       st + '_' + app.config['DLB_STATIONLIST_FILENAME'])
            print newfilename
            if os.path.exists(newfilename):
                os.remove(newfilename)

            os.rename(filename, newfilename)
        else:
            flash(app.config['DLB_STATIONLIST_FILENAME'] + " is not compliant !", "error")
            flash("Each line format must look like:" + '"419079;abk04c;1066abk04c-1sia-00g;Wijnegem afwaarts  (Albertkanaal);1;0"',"")
            flash("File will not be loaded", "warning")
    else:
        #file doesn't exist
        flash(app.config['DLB_STATIONLIST_FILENAME'] + " is not found !", "error" )
        bRet = False

    return bRet

# def loadStationListFromFile():
#     from app import app, db
#     import os
#     from .models import Stations
#     filename = app.config['DLB_STATIONLIST_FILENAME']
#     filename = os.path.join(app.config['DLB_UPLOAD_FOLDER'], filename)
#     if os.path.exists(filename):
#     # if (checkStationListFile(filename) == True):
#         for record in db.session.query(Stations).all():
#             db.session.delete(record)
#
#         db.session.commit()
#
#         with open(filename,"r") as inputFile:
#             for line in inputFile.readlines():
#                 station=classes.stationItem()
#                 station.stationid = line.split(";")[0]
#                 station.stationname = line.split(";")[1]
#                 station.gaugeExNumber = line.split(";")[2]
#                 station.sensorExNumber = line.split(";")[2][:-1] + "s"
#                 station.stationdescription = line.split(";")[3]
#                 station.stationHQ = int(line.split(";")[4])
#                 station.stationYSI = int(line.split(";")[5])
#                 record = Stations(stationid=station.stationid,
#                                   sensorExNumber = station.sensorExNumber,
#                                   gaugeExNumber = station.gaugeExNumber,
#                                   stationname=station.stationname,
#                                   stationdescription=station.stationdescription,
#                                   stationHQ=station.stationHQ,
#                                   stationYSI=station.stationYSI
#                                   )
#                 db.session.add(record)
#
#             # Save to DB
#             db.session.commit()
#             inputFile.close()
#             import datetime
#             ts = datetime.datetime.now()
#             st = datetime.datetime.now().strftime("%Y%m%d%H%M")
#             newfilename = os.path.join(app.config['DLB_BACKUP_FOLDER'], st + '_' + app.config['DLB_STATIONLIST_FILENAME'])
#             print newfilename
#             if os.path.exists(newfilename):
#                 os.remove(newfilename)
#
#             os.rename(filename,newfilename)
#     else:
#         # stasssat is not a valid file
#         bRet = False


def flash_errors(form):
    from flask import flash
    for field, errors in form.errors.items():
        for error in errors:
            # flash(u"Error in the %s field - %s" % (
            #     getattr(form, field).label.text, error
            # ))
            flash(u"%s" % ( error ),"warning")