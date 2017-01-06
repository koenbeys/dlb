r"""
	Adson Logging libray
"""

__version__ = '0.0.1'
__all__ = [
    'SetDebug', 'GetDebug','ResetDebug', 'PrintDebug', 'SetDebugFile',
    'SetLogFile','PrintLog',
    'PrintError','PrintWarning'
]

__author__ = 'Koen Beys'

"""			Debugging

SetDebug        =>  start debugging
ResetDebug      =>  Stop Debugging
GetDebug        =>  status van debugging => 1 => debugging is actief
SetDebugFile    =>  Voeg debugging info toe aan meegeveven file
                    input   "Filename" => filename
                            1 => naar Scherm
PrintDebug		=> Commando dat debug INFO print of bijvoegd aan file

"""

def SetDebug(dbg=1):
    from lib import AdsVar
    AdsVar.debug =dbg

def GetDebug():
    from adson import AdsVar

    try:
        a=AdsVar.debug
    except:
        AdsVar.debug=0
    return AdsVar.debug

def ResetDebug(dbg=0):
    from adson import AdsVar
    AdsVar.debug =dbg

def SetDebugFile(DebugFile):
    from os.path import isfile
    from os import access,W_OK

    from adson import PrintDebug,PrintDebug,PrintLog,AdsVar

    PrintDebug('start module ')

    AdsVar.debugFile=DebugFile

    if AdsVar.debugFile!=None:
        if not(isfile(AdsVar.debugFile)) :
            PrintDebug('Debugfile: %s bestaat niet.' % (AdsVar.debugFile ) )
            try :
                MYFILE = open(AdsVar.debugFile,"w")
                MYFILE.close()
            except :
                PrintError('Error creating Debugfile %s' % (AdsVar.debugFile))

            PrintDebug('Debugfile: %s aangemaakt.' % (AdsVar.debugFile ))

        try :
            if access(AdsVar.debugFile,W_OK):
                PrintDebug('Debugfile %s writable'% (AdsVar.debugFile))
            else:
                PrintDebug('Debugfile %s NOT writable'% (AdsVar.debugFile))
                AdsVar.debugFile=1
        except IOError:
            PrintWarning('Kan bestand niet openen: %s' % (AdsVar.debugFile) )
            AdsVar.debugFile=1

def PrintDebug(Str_value):
    from time import strftime, localtime
    from adson import AdsVar
    from inspect import stack

    try:
        a=AdsVar.debug
    except:
        AdsVar.debug=0

    try:
        a=AdsVar.debugFile
    except:
        AdsVar.debugFile = 1

    if AdsVar.debug == 1 :
        if AdsVar.debugFile == 1:
            print strftime("%Y/%m/%d-%H:%M:%S", localtime()) + ": DEB: " + stack()[1][3]+","+ stack()[2][3]+ " - "+str(Str_value)
        elif AdsVar.debugFile != None :
            DEB = open(AdsVar.debugFile, "a")
            DEB.write( strftime("%Y/%m/%d-%H:%M:%S", localtime()) + ': DEB: '  + stack()[1][3]+","+ stack()[2][3]+ " - "+ str(Str_value)+'\n')
            DEB.close()
#######################################################################################



"""			Logging

SetLogFile	=> Voeg Logging info toe aan meegeveven file

PrintLog		=> Commando dat de log INFO print of bijvoegd aan file

"""

def SetLogFile(LogFile):
    from os.path import isfile
    from os import access,W_OK

    from adson import PrintDebug,PrintDebug,PrintLog,AdsVar

    PrintDebug('start module' )

    AdsVar.LogFile=LogFile

    if AdsVar.LogFile not in (0,1,None):
        if not(isfile(AdsVar.LogFile)) :
            PrintWarning('Logfile: ' + AdsVar.LogFile + ' bestaat niet.')
            try :
                MYFILE = open(AdsVar.LogFile,"w")
                MYFILE.close()
            except :
                PrintWarning('Error creating Logfile'+AdsVar.LogFile)

            PrintDebug('Logfile: ' + AdsVar.LogFile + ' aangemaakt.')

        try :
            if access(AdsVar.LogFile,W_OK):
                PrintDebug('Logfile ' + AdsVar.LogFile + ' writable')
            else:
                PrintWarning('Logfile ' + AdsVar.LogFile + ' NOT writable')
                AdsVar.LogFile=1
        except IOError:
            PrintWarning('Kan bestand niet openen: '+ AdsVar.LogFile )
            AdsVar.LogFile=1


def PrintLog(Str_value):
    from time import strftime, localtime
    from adson import AdsVar

    try:
        a=AdsVar.LogFile
    except:
        AdsVar.LogFile = 1

    if AdsVar.LogFile == 1:
        print strftime("%Y/%m/%d-%H:%M:%S", localtime()) + ": LOG: " + str(Str_value)
    elif AdsVar.LogFile != None :
	   LOG = open(AdsVar.LogFile, "a")
	   LOG.write( strftime("%Y/%m/%d-%H:%M:%S", localtime()) + ': ' + str(Str_value)+'\n')
	   LOG.close()

#######################################################################################
"""			Trackfiles

SetTrackFile	            => Voeg error info toe aan meegeveven file
WriteTrackFile              => Maak een dumpfile van de TrackFile op disk
ReadTrackFile               => Lees de dumpfile van de TrackFIle van disk en maak ter beschiiking in memory
Clean_TrackFile_FileList    => Vergelijk de TrackFile met de Filelist en schrap in de Filelist de records die voorkomen in de TrackFile
                               (FileList => files die nog moet verwerkt worden) en schrapt in de TrackFile de files die niet meer voor komen
                               in Track File

"""
def SetTrackFile(TrackFile):
    from os.path import isfile
    from os import access,W_OK
    from adson import AdsVar

    from adson import PrintDebug,PrintDebug,PrintLog

    PrintDebug('start module' )

    AdsVar.TrackFile=TrackFile

    AdsVar.TrackFileList=[]
    if AdsVar.TrackFile!=None:
        if not(isfile(AdsVar.TrackFile)) :
            PrintWarning('TrackFile: %s bestaat niet.' % (AdsVar.TrackFile))
            try :
                MYFILE = open(AdsVar.TrackFile,"w")
                MYFILE.close()
            except :
                PrintWarning('Error creating TrackFile %s' % (AdsVar.TrackFile) )

            PrintDebug('TrackFile: %s aangemaakt.'% (AdsVar.TrackFile))

        try :
            if access(AdsVar.TrackFile,W_OK):
                PrintDebug('TrackFile %s writable'% (AdsVar.TrackFile))
            else:
                PrintWarning('TrackFile %s NOT writable'% (AdsVar.TrackFile))
                AdsVar.TrackFile=None
        except IOError:
            PrintWarning('Kan bestand niet openen: %s' % (AdsVar.TrackFile))
            AdsVar.TrackFile=None


def WriteTrackFile():
    from os.path import isfile
    from os import access,W_OK,rename,remove
    from adson import SetTrackFile,AdsVar
    from pickle import dump

    PrintDebug('start module' )

    try:
        a=AdsVar.TrackFile
    except:
        AdsVar.TrackFile = None

    PrintDebug('WriteTrackFile start: %s' % (AdsVar.TrackFile))

    if  AdsVar.TrackFile != None:
        if isfile(AdsVar.TrackFile+".tmp"):
            remove(AdsVar.TrackFile+".tmp")
        if isfile(AdsVar.TrackFile):
            PrintDebug('WriteTrackFile : %s found + rename'% (AdsVar.TrackFile))
            rename(AdsVar.TrackFile,AdsVar.TrackFile+".tmp")

        try :
            TRACKFILE = open(AdsVar.TrackFile,"wb")
            dump(AdsVar.TrackFileList,TRACKFILE)
            TRACKFILE.close()
        except :
            PrintWarning('Error open /schrijven TrackFile %s '% (AdsVar.TrackFile))
    PrintDebug('WriteTrackFile einde : %s ' % (AdsVar.TrackFile))

def ReadTrackFile():
    from os.path import isfile,getsize
    from os import access,W_OK,rename,remove
    from lib import SetTrackFile,AdsVar
    from pickle import load

    PrintDebug('start module ' )

    try:
        a=AdsVar.TrackFile
    except:
        AdsVar.TrackFile = None

    PrintDebug('ReadTrackFile start : %s' % (AdsVar.TrackFile))

    if  AdsVar.TrackFile != None :
        if isfile(AdsVar.TrackFile) and getsize(AdsVar.TrackFile)>0 :
            try :
                TRACKFILE = open(AdsVar.TrackFile,"rb")
                AdsVar.TrackFileList=load(TRACKFILE)
                TRACKFILE.close()
            except :
                PrintWarning('Error open / lezen TrackFile %s'% (AdsVar.TrackFile))
    PrintDebug('ReadTrackFile einde : %s'% (AdsVar.TrackFile))

def Clean_TrackFile_FileList ():
    from adson import AdsVar,PrintDebug

    PrintDebug("TrackFileList bevat %d, FileList %d Files" % (len(AdsVar.TrackFileList),len(AdsVar.FileList)))
    AdsVar.FileList=sorted(AdsVar.FileList,key=lambda file: file[2])
    AdsVar.TrackFileList=sorted(AdsVar.TrackFileList,key=lambda file: file[2])
    i=0
    j=0

    while i <= len(AdsVar.TrackFileList)-1 and j < len(AdsVar.FileList):
        while AdsVar.FileList[j][2] < AdsVar.TrackFileList[i][2] and j < len(AdsVar.FileList) - 1 and i < len(AdsVar.TrackFileList) - 1:
            if j < len(AdsVar.FileList)-1:
                j=j+1

        if AdsVar.TrackFileList[i]==AdsVar.FileList[j]  :
##            adson.PrintLog("File "+AdsVar.FileList[j][2]+" gevonden  in de TrackFile")
            del AdsVar.FileList[j]

            if i < len(AdsVar.TrackFileList):
                i=i+1
        else:
            del AdsVar.TrackFileList[i]

    PrintDebug("Er blijven TrackFileList bevat %d, FileList %d Files over" % (len(AdsVar.TrackFileList),len(AdsVar.FileList)))




#######################################################################################

"""			Error files

SetErrorFile	=> set de ErrorFile voor Printerror() functie zodat de errors in afzonderlijkfile komen,
                   anders worden ze in Logfile weg geschreven
PrintError		=> Commando dat error INFO print of bijvoegd aan file
PrintWarning    => Commando dat error INFO print of bijvoegd aan de logfile

"""

def SetErrorFile(ErrorFile):
    from os.path import isfile
    from os import access,W_OK

    from adson import PrintDebug,PrintDebug,PrintLog,AdsVar

    AdsVar.ErrorFile=ErrorFile

    if AdsVar.ErrorFile!=None:
        if not(isfile(AdsVar.ErrorFile)) :
            PrintDebug('Errorfile: ' + AdsVar.ErrorFile + ' bestaat niet.')
            try :
                MYFILE = open(AdsVar.ErrorFile,"w")
                MYFILE.close()
            except :
                PrintError('Error creating Errorfile'+AdsVar.ErrorFile)

            PrintDebug('Errorfile: ' + AdsVar.ErrorFile + ' aangemaakt.')

        try :
            if access(AdsVar.ErrorFile,W_OK):
                PrintDebug('Errorfile ' + AdsVar.ErrorFile + ' writable')
            else:
                PrintDebug('Errorfile ' + AdsVar.ErrorFile + ' NOT writable')
                AdsVar.ErrorFile=1
        except IOError:
            PrintWarning('Kan bestand niet openen: '+ AdsVar.ErrorFile )
            AdsVar.ErrorFile=1


def PrintError(Str_value):
    from time import strftime, localtime
    from adson import PrintLog,AdsVar

    try:
        a=AdsVar.ErrorFile
    except:
        AdsVar.ErrorFile = 1

    if AdsVar.ErrorFile == 1:
        PrintLog(" ### ERROR ### " + str(Str_value))
    elif AdsVar.LogFile != None :
        ERROR = open(AdsVar.ErrorFile, "a")
        ERROR.write( strftime("%Y/%m/%d-%H:%M:%S", localtime()) + ": ### ERROR ###: " + str(Str_value)+'\n')
        ERROR.close()



def PrintWarning(Str_value):
    from time import strftime, localtime
    from adson import PrintLog,AdsVar

    try:
        a=AdsVar.DisableWarning
    except:
        AdsVar.DisableWarning=0

    if not AdsVar.DisableWarning :
        PrintLog(" ### WARNING ### " + str(Str_value))
    return

