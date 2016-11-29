from . import dlb
from flask import redirect, render_template, render_template_string, Blueprint,request,url_for
from . import classes

def getStationList():
    from .models import Stations
    tblStations = Stations.query.filter(Stations.stationid >= 0)

#    lstStations = []
#    for station in tblStations:
#        lstStations.append(getStationInfo(station.stationid))
    return tblStations

def getStationInfo(stationid):
    from .models import Stations
    recstation = Stations.query.filter(Stations.stationid == stationid).first()
    # ostation = classes.stationItem()
    # ostation.stationid = recstation.stationid
    # ostation.stationname = recstation.stationname
    # ostation.stationdescription = recstation.stationdescription
    # ostation.stationExNumber = recstation.stationExNumber
    return recstation

def getHistoryHQ(stationid, limit):
    from .models import historyItemsHQs
    tblHistory = historyItemsHQs.query.filter(historyItemsHQs.stationid == stationid).order_by('-id').limit(limit)
    return tblHistory

def getHistoryHQbyDates(stationid,dtfrom,dtto):
    from datetime import datetime, timedelta
    from .models import historyItemsHQs
    dtdtfrom = datetime.strptime(dtfrom, '%d/%m/%Y')
    dtdtto = datetime.strptime(dtto, '%d/%m/%Y')
    dtdtto =dtdtto + timedelta(days=1)
    tblHistory = historyItemsHQs.query.filter(historyItemsHQs.stationid == stationid, historyItemsHQs.recTs >= dtdtfrom, historyItemsHQs.recTs <= dtdtto).order_by('-id')
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


def getHistoryYSI(stationid, limit):
    from .models import historyItemsYSIs
    tblHistory = historyItemsYSIs.query.filter(historyItemsYSIs.stationid == stationid).order_by('-id').limit(limit)
    return tblHistory

def getHistoryYSIbyDates(stationid,dtfrom,dtto):
    from datetime import datetime, timedelta
    from .models import historyItemsYSIs
    dtdtfrom = datetime.strptime(dtfrom, '%d/%m/%Y')
    dtdtto = datetime.strptime(dtto, '%d/%m/%Y')
    dtdtto =dtdtto + timedelta(days=1)
    tblHistory = historyItemsYSIs.query.filter(historyItemsYSIs.stationid == stationid, historyItemsYSIs.recTs >= dtdtfrom, historyItemsYSIs.recTs <= dtdtto).order_by('-id')
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


def checkStationListFile(filename):
    import os
    bRet = False
    if os.path.exists(filename):
        bRet = True
        #extra tests to be implemented
    else:
        #file doesn't exist
        bRet = False

    return bRet

def loadStationListFromFile():

    from app import app, db
    import os
    from .models import Stations
    filename = app.config['DLB_STATIONLIST_FILENAME']
    filename = os.path.join(app.config['DLB_UPLOAD_FOLDER'], filename)
    if (checkStationListFile(filename) == True):
        for record in db.session.query(Stations).all():
            db.session.delete(record)

        db.session.commit()

        inputFile = open(filename,"r")

        for line in inputFile.readlines():
            print line
            station=classes.stationItem()
            station.stationid = line.split(";")[0]
            station.stationname = line.split(";")[1]
            station.gaugeExNumber = line.split(";")[2]
            station.sensorExNumber = line.split(";")[2][:-1] + "s"
            station.stationdescription = line.split(";")[3]
            station.stationHQ = int(line.split(";")[4])
            station.stationYSI = int(line.split(";")[5])

            record = Stations(stationid=station.stationid,
                              sensorExNumber = station.sensorExNumber,
                              gaugeExNumber = station.gaugeExNumber,
                              stationname=station.stationname,
                              stationdescription=station.stationdescription,
                              stationHQ=station.stationHQ,
                              stationYSI=station.stationYSI
                              )

            db.session.add(record)

        # Save to DB
        db.session.commit()
        inputFile.close()
        import datetime
        ts = datetime.datetime.now()
        st = datetime.datetime.now().strftime("%Y%m%d%H%M")
        newfilename = os.path.join(app.config['DLB_BACKUP_FOLDER'], st + '_' + app.config['DLB_STATIONLIST_FILENAME'])
        print newfilename
        if os.path.exists(newfilename):
            os.remove(newfilename)

        os.rename(filename,newfilename)
    else:
        # stasssat is not a valid file
        bRet = False

