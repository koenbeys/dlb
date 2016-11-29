from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, DateField, DateTimeField, TextField


# Define the User profile form
class StationListForm(Form):
    stationid = StringField('stationid', validators=[
        validators.DataRequired('stationid is required')])
    submit = SubmitField('Submit')
    op = StringField('op')

class histoHQForm(Form):
    stationid = StringField('stationid', validators=[validators.DataRequired('stationid is required')])
    dtfrom = DateTimeField((u'dtfrom'), validators=[validators.data_required()], format='%d/%m/%Y')
    dtto = DateTimeField((u'dtto'), validators=[validators.data_required()], format='%d/%m/%Y')

class StationHQForm(Form):
    stationid = StringField('stationid', validators=[validators.DataRequired('stationid is required')])
    #stationExNumber = StringField('stationExNumber', validators=[validators.DataRequired('stationid is required')])
    recTs = DateTimeField((u'recTs'), validators=[validators.data_required()], format='%d/%m/%Y %H:%M')
    observator = StringField((u'observator'))
    sensorTs = DateTimeField((u'sensorTs'), validators=[validators.data_required()], format='%d/%m/%Y %H:%M')
    gaugeTs = DateTimeField((u'gaugeTs'), validators=[validators.data_required()], format='%d/%m/%Y %H:%M')
    #operator = StringField((u'operator'), validators=[validators.DataRequired('operator is required')])
    deltaT = StringField((u'deltaT'), validators=[validators.DataRequired('deltaT is required')])
    sensorValue = StringField((u'sensorValue'), validators=[validators.DataRequired('sensorValue is required')])
    gaugeValue = StringField((u'gaugeValue'), validators=[validators.DataRequired('gaugeValue is required')])
    comment = StringField((u'comment'))
    hardwareChanged =  BooleanField(u'hardwareChanged')
    hardwareNumberOld =  StringField(u'hardwareNumberOld')
    hardwareNumberNew =  StringField(u'hardwareNumberNew')
    hardwareReset =  BooleanField(u'hardwareReset')
    hardwareConfigured =  BooleanField(u'hardwareConfigured')
    sensorCleaned = BooleanField(u'sensorCleaned')
    gaugeCleaned  = BooleanField(u'gaugeCleaned')
    sectionCleaned = BooleanField(u'sectionCleaned')
    hardwareCalibrated = BooleanField(u'hardwareCalibrated')
#test
    #    submit = SubmitField('Submit')

class StationYSIForm(Form):
    stationid = StringField(u'stationid', validators=[validators.DataRequired('stationid is required')])
    recTs = DateTimeField((u'recTs'), validators=[validators.data_required()], format='%d/%m/%Y %H:%M')
 #   operator = StringField((u'operator'), validators=[validators.DataRequired('operator is required')])
    observator = StringField((u'observator'))
    gaugeTs = DateTimeField((u'gaugeTs'), validators=[validators.data_required()], format='%d/%m/%Y %H:%M')
    gaugeValue = StringField((u'gaugeValue'), validators=[validators.DataRequired('gaugeValue is required')])
    hardwareChanged = BooleanField(u'hardwareChanged')
    hardwareNumberOld = StringField((u'hardwareNumberOld'))
    hardwareTsOld = DateTimeField((u'hardwareTsOld'), validators=[validators.data_required()], format='%d/%m/%Y %H:%M')
    hardwareNumberNew = StringField((u'hardwareNumberNew'))
    hardwareTsNew = DateTimeField((u'hardwareTsNew'), validators=[validators.data_required()], format='%d/%m/%Y %H:%M')
    hardwareCleaned = BooleanField(u'hardwareCleaned')
    hardwareCalibrated = BooleanField(u'hardwareCalibrated')
    samplesCollected = BooleanField(u'samplesCollected')
    sectionCleaned = BooleanField(u'sectionCleaned')
    comment = StringField((u'comment'))

class histoYSIForm(Form):
    stationid = StringField('stationid', validators=[validators.DataRequired('stationid is required')])
    dtfrom = DateTimeField((u'dtfrom'), validators=[validators.data_required()], format='%d/%m/%Y')
    dtto = DateTimeField((u'dtto'), validators=[validators.data_required()], format='%d/%m/%Y')


class TestForm(Form):
    print "ok"
    dataloggerTime = DateTimeField((u'dataloggerDate'), validators=[validators.data_required()],
             format='%d/%m/%Y %H:%M')
    #dataloggerDate = DateField('dataloggerTime',format='%Y-%m-%d')
    #date = StringField('dataloggerTime',validators=[validators.Regexp('^(20|21|22|23|[01]\d|\d)((:[0-5]\d){1,2})$')])

    #dataloggerTime = StringField('dataloggerTime')
    #dtime = dataloggerDate.data & " " & dataloggerTime.data
    #ddTime = DateTimeField(dtime, format='%Y-%m-%d %H:%M')
    submit = SubmitField('Submit')

