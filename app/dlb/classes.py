class stationItem:
    stationid = -1
    stationname = ""
    sensorExNumber = ""
    gaugeExNumber = ""
    stationdescription = ""
    stationHQ = 1
    stationYSI = 1

class historyItemHQ:
    stationid = -1
    date = ""
    deltaT = 0
    operator = ""
    dataloggerTime = ""
    dataloggerValue = -9999
    gaugeTime = ""
    gaugeValue = -9999
    dataloggerCleaned = False
    gaugeCleaned = False
    sectionCleaned = False
    comment = ""
