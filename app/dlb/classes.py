from datetime import datetime
from . import log

class stationItem:
    log.debug('start class stationItem')
    # stationid = -1
    stationname = u""
    sensorExNumber = u""
    gaugeExNumber = u""
    stationdescription = ""
    stationHQ = 0
    stationYSI = 0

class historyItemHQ:
    log.debug('start class historyItemHQ')
    # stationid = -1
    stationname = u""
    recTs = datetime(1900,1,1)
    observator = u""
    operator = u""
    sensorTs = datetime(1900,1,1)
    sensorValue = -9999
    sensorTime = ""
    gaugeTs = datetime(1900,1,1)
    gaugeValue = -9999
    gaugeTime = ""
    sensorCleaned = ""
    gaugeCleaned = ""
    sectionCleaned = ""
    comment = u""
    deltaT = -9999
    hardwareChanged = False
    hardwareNumberOld = u""
    hardwareNumberNew = u""
    hardwareReset = False
    hardwareCalibrated = False
    hardwareConfigured = False

class historyItemYSI:
    log.debug('start class historyItemYSI')
    # stationid = -1
    stationname = u""
    recTs = datetime(1900,1,1)
    observator = u""
    operator = u""
    gaugeTs = datetime(1900,1,1)
    gaugeValue = -9999
    gaugeTime = ""
    gaugeCleaned = False
    comment = u""
    deltaT = -9999
    hardwareChanged = False
    hardwareNumberOld = u""
    hardwareTsOld = ""
    hardwareTimeOld = ""
    hardwareNumberNew = u""
    hardwareTsNew = ""
    hardwareTimeNew = ""
    hardwareCleaned = False
    hardwareCalibrated = False
    samplesCollected = False
    sectionCleaned = False
