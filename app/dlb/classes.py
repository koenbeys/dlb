class stationItem:
    # stationid = -1
    stationname = ""
    sensorExNumber = ""
    gaugeExNumber = ""
    stationdescription = ""
    stationHQ = 0
    stationYSI = 0

from datetime import datetime
class historyItemHQ:
    # stationid = -1
    stationname = ""
    recTs = datetime(1900,1,1)
    observator = ""
    operator = ""
    sensorTs = datetime(1900,1,1)
    sensorValue = -9999
    sensorTime = ""
    gaugeTs = datetime(1900,1,1)
    gaugeValue = -9999
    gaugeTime = ""
    sensorCleaned = ""
    gaugeCleaned = ""
    sectionCleaned = ""
    comment = ""
    deltaT = -9999
    hardwareChanged = False
    hardwareNumberOld = ""
    hardwareNumberNew = ""
    hardwareReset = False
    hardwareCalibrated = False
    hardwareConfigured = False


class historyItemYSI:
    # stationid = -1
    stationname = ""
    recTs = datetime(1900,1,1)
    observator = ""
    operator = ""
    gaugeTs = datetime(1900,1,1)
    gaugeValue = -9999
    gaugeTime = ""
    gaugeCleaned = False
    comment = ""
    deltaT = -9999
    hardwareChanged = False
    hardwareNumberOld = ""
    hardwareTsOld = ""
    hardwareTimeOld = ""
    hardwareNumberNew = ""
    hardwareTsNew = ""
    hardwareTimeNew = ""
    hardwareCleaned = False
    hardwareCalibrated = False
    samplesCollected = False
    sectionCleaned = False
