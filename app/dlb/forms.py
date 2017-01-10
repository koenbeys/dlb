from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators, DateField, DateTimeField, TextField, IntegerField, FloatField
from . import log


class StationListForm(Form):

    log.debug('class StationListForm(Form)')

    stationname = StringField('stationname', validators=[
        validators.DataRequired('You must select a location !')])
    submit = SubmitField('Submit')
    op = StringField('op')

class histoHQForm(Form):
    log.debug('class histoHQForm(Form)')

    stationname = StringField('stationname', validators=[validators.DataRequired('stationname is required')])
    dtfrom = DateTimeField((u'dtfrom'), validators=[validators.data_required()], format='%d/%m/%Y')
    dtto = DateTimeField((u'dtto'), validators=[validators.data_required()], format='%d/%m/%Y')


class StationHQForm(Form):
    log.debug('class StationHQForm(Form)')

    stationname = StringField('stationname', validators=[validators.DataRequired('stationname is required')])
    #stationExNumber = StringField('stationExNumber', validators=[validators.DataRequired('stationid is required')])
    recTs = DateTimeField((u'recTs'), validators=[validators.data_required()], format='%d/%m/%Y %H:%M')

    sensorTs = DateTimeField((u'sensorTs'), validators=[validators.data_required()], format='%d/%m/%Y %H:%M')
    gaugeTs = DateTimeField((u'gaugeTs'), validators=[validators.data_required()], format='%d/%m/%Y %H:%M')
    #operator = StringField((u'operator'), validators=[validators.DataRequired('operator is required')])
    deltaT = IntegerField((u'deltaT'), validators=[validators.DataRequired('deltaT value must be numerical')])
    sensorValue = FloatField((u'sensorValue'), validators=[validators.DataRequired('sensor value must be numerical')])
    gaugeValue = FloatField((u'gaugeValue'), validators=[validators.DataRequired('gauge value must be numerical')])
    comment = StringField((u'comment'))
    hardwareChanged =  BooleanField(u'hardwareChanged')
    hardwareReset =  BooleanField(u'hardwareReset')
    hardwareConfigured =  BooleanField(u'hardwareConfigured')
    sensorCleaned = BooleanField(u'sensorCleaned')
    gaugeCleaned  = BooleanField(u'gaugeCleaned')
    sectionCleaned = BooleanField(u'sectionCleaned')
    hardwareCalibrated = BooleanField(u'hardwareCalibrated')

    observator = StringField((u'observator'), validators=[validators.DataRequired('observator is absolutely required')])

    sensorTime = StringField(u'sensorTime')
    gaugeTime = StringField(u'gaugeTime')

    hardwareNumberOld = StringField(u'hardwareNumberOld', validators=[validators.DataRequired('old number required if changed')])
    hardwareNumberNew = StringField(u'hardwareNumberNew', validators=[validators.DataRequired('new number required if changed')])

    #test
    #    submit = SubmitField('Submit')

class StationYSIForm(Form):
    log.debug('class StationYSIForm(Form)')

    stationname = StringField(u'stationname', validators=[validators.DataRequired('stationname is required')])
    recTs = DateTimeField((u'recTs'), validators=[validators.data_required('recTs not valid')], format='%d/%m/%Y %H:%M')
 #   operator = StringField((u'operator'), validators=[validators.DataRequired('operator is required')])
    observator = StringField((u'observator'), validators=[validators.DataRequired('observator is required')])
    deltaT = IntegerField((u'deltaT'), validators=[validators.DataRequired('deltaT value must be numerical')])
    gaugeTs = DateTimeField((u'gaugeTs'), validators=[validators.data_required('gaugeTs not valid')], format='%d/%m/%Y %H:%M')
    gaugeTime = StringField((u'gaugeTime'))
    gaugeCleaned  = BooleanField(u'gaugeCleaned')
    gaugeValue = FloatField((u'gaugeValue'), validators=[validators.DataRequired('gaugeValue value must be numerical')])
    hardwareChanged = BooleanField(u'hardwareChanged')
    hardwareNumberOld = StringField((u'hardwareNumberOld'), validators=[validators.DataRequired('old number required if changed')])
    hardwareTsOld = DateTimeField((u'hardwareTsOld'), validators=[validators.data_required('hardwareTsOld not valid')], format='%d/%m/%Y %H:%M')
    hardwareTimeOld = StringField((u'hardwareTimeOld'))
    hardwareNumberNew = StringField((u'hardwareNumberNew'), validators=[validators.DataRequired('new number required if changed')])
    hardwareTsNew = DateTimeField((u'hardwareTsNew'), validators=[validators.data_required('hardwareTsNew not valid')], format='%d/%m/%Y %H:%M')
    hardwareTimeNew = StringField((u'hardwareTimeNew'))
    hardwareCleaned = BooleanField(u'hardwareCleaned')
    hardwareCalibrated = BooleanField(u'hardwareCalibrated')
    samplesCollected = BooleanField(u'samplesCollected')
    sectionCleaned = BooleanField(u'sectionCleaned')
    comment = StringField((u'comment'))

class histoYSIForm(Form):
    log.debug('class histoYSIForm(Form)')
    stationname = StringField('stationname', validators=[validators.DataRequired('stationname is required')])
    dtfrom = DateTimeField((u'dtfrom'), validators=[validators.data_required()], format='%d/%m/%Y')
    dtto = DateTimeField((u'dtto'), validators=[validators.data_required()], format='%d/%m/%Y')


# class uploadForm(Form):
#     file = StringField(u'file', validators=[validators.DataRequired('stationid is required')])

class TestForm(Form):
    #print "ok"
    dataloggerTime = DateTimeField((u'dataloggerDate'), validators=[validators.data_required()],
             format='%d/%m/%Y %H:%M')
    #dataloggerDate = DateField('dataloggerTime',format='%Y-%m-%d')
    #date = StringField('dataloggerTime',validators=[validators.Regexp('^(20|21|22|23|[01]\d|\d)((:[0-5]\d){1,2})$')])

    #dataloggerTime = StringField('dataloggerTime')
    #dtime = dataloggerDate.data & " " & dataloggerTime.data
    #ddTime = DateTimeField(dtime, format='%Y-%m-%d %H:%M')
    submit = SubmitField('Submit')
