from app import db

class Stations(db.Model):
    __tablename__ = 'stations'

    stationname = db.Column(db.Unicode(10), primary_key=True, server_default=u'')
    sensorExNumber = db.Column(db.Unicode(20), nullable=False, server_default=u'')
    gaugeExNumber = db.Column(db.Unicode(20), nullable=False, server_default=u'')

    stationdescription = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    stationHQ = db.Column(db.Boolean(), nullable=False, server_default='1')
    stationYSI = db.Column(db.Boolean(), nullable=False, server_default='1')


class historyItemsHQs(db.Model):
    __tablename__ = 'historyItemsHQ'
    id = db.Column(db.Integer, primary_key=True)
    stationname = db.Column(db.Unicode(10), nullable=False, server_default=u'')

    recTs =  db.Column(db.DateTime(), nullable=False, server_default='01/01/1900')

    operator = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    observator = db.Column(db.Unicode(50), nullable=False, server_default=u'-')

    sensorExNumber = db.Column(db.Unicode(20), nullable=False, server_default=u'')
    sensorTs = db.Column(db.DateTime(), nullable=False, server_default='01/01/1900')
    sensorValue = db.Column(db.Numeric, nullable=False , server_default='-9999')
    gaugeExNumber = db.Column(db.Unicode(20), nullable=False, server_default=u'')
    gaugeTs = db.Column(db.DateTime(), nullable=False, server_default='01/01/1900')
    gaugeValue = db.Column(db.Numeric(), nullable=False, server_default='-9999')
    sensorCleaned = db.Column(db.Boolean(), nullable=False, server_default='0')
    gaugeCleaned = db.Column(db.Boolean(), nullable=False, server_default='0')
    sectionCleaned = db.Column(db.Boolean(), nullable=False, server_default='0')
    hardwareChanged = db.Column(db.Boolean(), nullable=False, server_default='0')
    hardwareNumberOld = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    hardwareNumberNew = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    hardwareReset = db.Column(db.Boolean(), nullable=False, server_default='0')
    hardwareConfigured = db.Column(db.Boolean(), nullable=False, server_default='0')
    hardwareCalibrated = db.Column(db.Boolean(), nullable=False, server_default='0')
    deltaT = db.Column(db.Integer, nullable=False, server_default='0')
    comment = db.Column(db.Unicode(255), nullable=False, server_default=u'')

class historyItemsYSIs(db.Model):
    __tablename__ = 'historyItemsYSI'
    id = db.Column(db.Integer, primary_key=True)
    stationname = db.Column(db.Unicode(10), nullable=False, server_default=u'')

    recTs =  db.Column(db.DateTime(), nullable=False, server_default='01/01/1900')
    deltaT = db.Column(db.Integer, nullable=False, server_default='0')

    operator = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    observator = db.Column(db.Unicode(50), nullable=False, server_default=u'-')

    gaugeExNumber = db.Column(db.Unicode(20), nullable=False, server_default=u'')
    gaugeTs = db.Column(db.DateTime(), nullable=False, server_default='01/01/1900')
    gaugeValue = db.Column(db.Numeric(), nullable=False, server_default='-9999')
    gaugeCleaned = db.Column(db.Boolean(), nullable=False, server_default='0')
    hardwareChanged = db.Column(db.Boolean(), nullable=False, server_default='0')
    hardwareNumberOld = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    hardwareTsOld = db.Column(db.DateTime(), nullable=False, server_default='01/01/1900')
    hardwareNumberNew = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    hardwareTsNew = db.Column(db.DateTime(), nullable=False, server_default='01/01/1900')

    hardwareCleaned = db.Column(db.Boolean(), nullable=False, server_default='0')
    hardwareCalibrated = db.Column(db.Boolean(), nullable=False, server_default='0')

    samplesCollected = db.Column(db.Boolean(), nullable=False, server_default='0')

    sectionCleaned = db.Column(db.Boolean(), nullable=False, server_default='0')
    comment = db.Column(db.Unicode(255), nullable=False, server_default=u'')

