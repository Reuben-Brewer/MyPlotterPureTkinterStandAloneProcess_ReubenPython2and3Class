# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision W, 07/16/2025

Verified working on: Python 3.11/12 for Windows 10/11 64-bit, Ubuntu 20.04, and Raspberry Pi Bookworm.
THE SEPARATE-PROCESS-SPAWNING COMPONENT OF THIS CLASS IS NOT AVAILABLE IN PYTHON 2 DUE TO LIMITATION OF
"multiprocessing.set_start_method('spawn')" ONLY BEING AVAILABLE IN PYTHON 3. PLOTTING WITHIN A SINGLE PROCESS STILL WORKS.
'''

__author__ = 'reuben.brewer'

#########################################################
from MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class import *
#########################################################

#########################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
import math
import traceback
import re
import keyboard
import random
from random import randint
import signal #for CTRLc_HandlerFunction
#########################################################

#########################################################
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
#########################################################

#########################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#########################################################

##########################################################################################################
##########################################################################################################
def CTRLc_RegisterHandlerFunction():

    signal.signal(signal.SIGINT, CTRLc_HandlerFunction)

##########################################################################################################
##########################################################################################################

########################################################################################################## MUST ISSUE CTRLc_RegisterHandlerFunction() AT START OF PROGRAM
##########################################################################################################
def CTRLc_HandlerFunction(signum, frame):

    print("CTRLc_HandlerFunction event firing!")

    ExitProgram_Callback()

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
def GetLatestWaveformValue(CurrentTime, MinValue, MaxValue, Period, WaveformTypeString="Sine"):
    
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        try:

            ##########################################################################################################
            ##########################################################################################################
            OutputValue = 0.0
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            WaveformTypeString_ListOfAcceptableValues = ["Sine", "Cosine", "Triangular", "Square"]
        
            if WaveformTypeString not in WaveformTypeString_ListOfAcceptableValues:
                print("GetLatestWaveformValue: Error, WaveformTypeString must be in " + str(WaveformTypeString_ListOfAcceptableValues))
                return -11111.0
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            if WaveformTypeString == "Sine":
    
                TimeGain = math.pi/Period
                OutputValue = (MaxValue + MinValue)/2.0 + 0.5*abs(MaxValue - MinValue)*math.sin(TimeGain*CurrentTime)
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            elif WaveformTypeString == "Cosine":
    
                TimeGain = math.pi/Period
                OutputValue = (MaxValue + MinValue)/2.0 + 0.5*abs(MaxValue - MinValue)*math.cos(TimeGain*CurrentTime)
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            elif WaveformTypeString == "Triangular":
                TriangularInput_TimeGain = 1.0
                TriangularInput_MinValue = -5
                TriangularInput_MaxValue = 5.0
                TriangularInput_PeriodInSeconds = 2.0
        
                #TriangularInput_Height0toPeak = abs(TriangularInput_MaxValue - TriangularInput_MinValue)
                #TriangularInput_CalculatedValue_1 = abs((TriangularInput_TimeGain*CurrentTime_CalculatedFromMainThread % PeriodicInput_PeriodInSeconds) - TriangularInput_Height0toPeak) + TriangularInput_MinValue
        
                A = abs(MaxValue - MinValue)
                P = Period
    
                #https://stackoverflow.com/questions/1073606/is-there-a-one-line-function-that-generates-a-triangle-wave
                OutputValue = (A / (P / 2)) * ((P / 2) - abs(CurrentTime % (2 * (P / 2)) - P / 2)) + MinValue
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            elif WaveformTypeString == "Square":
    
                TimeGain = math.pi/Period
                MeanValue = (MaxValue + MinValue)/2.0
                SinusoidalValue =  MeanValue + 0.5*abs(MaxValue - MinValue)*math.sin(TimeGain*CurrentTime)
                
                if SinusoidalValue >= MeanValue:
                    OutputValue = MaxValue
                else:
                    OutputValue = MinValue
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            else:
                OutputValue = 0.0
            ##########################################################################################################
            ##########################################################################################################
            
            return OutputValue

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        except:
            exceptions = sys.exc_info()[0]
            print("GetLatestWaveformValue: Exceptions: %s" % exceptions)
            return -11111.0
            traceback.print_exc()
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback(OptionalArugment = 0):
    global EXIT_PROGRAM_FLAG

    print("Exiting all threads in test_program_for_MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class.")

    EXIT_PROGRAM_FLAG = 1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    ##########################################################################################################
    ##########################################################################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    CTRLc_RegisterHandlerFunction()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    random.seed() #For random-number-generation
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    global USE_MyPlotterPureTkinterStandAloneProcess_FLAG
    USE_MyPlotterPureTkinterStandAloneProcess_FLAG = 1
    
    global USE_KEYBOARD_FLAG
    USE_KEYBOARD_FLAG = 1
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    global SHOW_IN_GUI_MyPlotterPureTkinterStandAloneProcess_FLAG
    SHOW_IN_GUI_MyPlotterPureTkinterStandAloneProcess_FLAG = 1
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30

    global CurrentTime_CalculatedFromMainThread
    CurrentTime_CalculatedFromMainThread = -11111.0

    global StartingTime_CalculatedFromMainThread
    StartingTime_CalculatedFromMainThread = -11111.0

    global LoopCounter_CalculatedFromMainThread
    LoopCounter_CalculatedFromMainThread = 0

    global MoveGraphPositionCounter
    MoveGraphPositionCounter = 0

    global PeriodicInput_AcceptableValues
    PeriodicInput_AcceptableValues = ["GUI", "VINThub", "Sine", "Cosine", "Triangular", "Square"]

    global PeriodicInput_Type_1
    PeriodicInput_Type_1 = "Sine"

    global PeriodicInput_MinValue_1
    PeriodicInput_MinValue_1 = -1.0

    global PeriodicInput_MaxValue_1
    PeriodicInput_MaxValue_1 = 1.0

    global PeriodicInput_Period_1
    PeriodicInput_Period_1 = 0.5

    global PeriodicInput_CalculatedValue_1
    PeriodicInput_CalculatedValue_1 = 0.0

    global PeriodicInput_Type_2
    PeriodicInput_Type_2 = "Sine"

    global PeriodicInput_MinValue_2
    PeriodicInput_MinValue_2 = -1.0

    global PeriodicInput_MaxValue_2
    PeriodicInput_MaxValue_2 = 1.0

    global PeriodicInput_Period_2
    PeriodicInput_Period_2 = 1.0

    global PeriodicInput_CalculatedValue_2
    PeriodicInput_CalculatedValue_2 = 0.0
    
    global NoiseCounter
    NoiseCounter = 0

    global NoiseCounter_FireEveryNth
    NoiseCounter_FireEveryNth = 5

    global NoiseAmplitude_Percent0to1OfPeriodicInputAmplitude
    NoiseAmplitude_Percent0to1OfPeriodicInputAmplitude = 0.25
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject

    global MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG
    MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = -1

    global MyPlotterPureTkinterStandAloneProcess_MostRecentDict
    MyPlotterPureTkinterStandAloneProcess_MostRecentDict = dict()

    global MyPlotterPureTkinterStandAloneProcess_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag
    MyPlotterPureTkinterStandAloneProcess_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = -1

    global LastTime_CalculatedFromMainThread_MyPlotterPureTkinterStandAloneProcess
    LastTime_CalculatedFromMainThread_MyPlotterPureTkinterStandAloneProcess = -11111.0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    global MyPlotterPureTkinterStandAloneProcess_GUIparametersDict
    MyPlotterPureTkinterStandAloneProcess_GUIparametersDict = dict([("EnableInternal_MyPrint_Flag", 1),
                                                                    ("NumberOfPrintLines", 10),
                                                                    ("GraphCanvasWidth", 1280),
                                                                    ("GraphCanvasHeight", 720),
                                                                    ("GraphCanvasWindowStartingX", 1),
                                                                    ("GraphCanvasWindowStartingY", 2),
                                                                    ("GraphCanvasWindowTitle", "My plotting example!"),
                                                                    ("GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents", 20)])

    global MyPlotterPureTkinterStandAloneProcess_SetupDict
    MyPlotterPureTkinterStandAloneProcess_SetupDict = dict([("GUIparametersDict", MyPlotterPureTkinterStandAloneProcess_GUIparametersDict),
                                                            ("ParentPID", os.getpid()),
                                                            ("WatchdogTimerDurationSeconds_ExpirationWillEndStandAlonePlottingProcess", 5.0),
                                                            ("CurvesToPlotNamesAndColorsDictOfLists", dict([("NameList", ["PlotCurve1", "PlotCurve2", "PlotCurve3"]),
                                                                                                        ("MarkerSizeList", [3, 5, 1]),
                                                                                                        ("LineWidthList", [1, 1, 0]),
                                                                                                        ("IncludeInXaxisAutoscaleCalculationList", [1, 1, 1]),
                                                                                                        ("IncludeInYaxisAutoscaleCalculationList", [1, 1, 1]),
                                                                                                        ("ColorList", ["Red", "Green", "Blue"])])),
                                                            ("SmallTextSize", 7),
                                                            ("LargeTextSize", 12),
                                                            ("NumberOfDataPointToPlot", 25),
                                                            ("XaxisNumberOfTickMarks", 10),
                                                            ("YaxisNumberOfTickMarks", 10),
                                                            ("XaxisNumberOfDecimalPlacesForLabels", 3),
                                                            ("YaxisNumberOfDecimalPlacesForLabels", 3),
                                                            ("XaxisAutoscaleFlag", 1),
                                                            ("YaxisAutoscaleFlag", 0),
                                                            ("X_min", 0.0),
                                                            ("X_max", 5.0),
                                                            ("Y_min", -5.0),
                                                            ("Y_max", 5.0),
                                                            ("XaxisDrawnAtBottomOfGraph", 0),
                                                            ("XaxisLabelString", "Time (sec)"),
                                                            ("YaxisLabelString", "Y-units (units)"),
                                                            ("ShowLegendFlag", 1),
                                                            ("SavePlot_DirectoryPath", os.path.join(os.getcwd(), "SavedImagesFolder"))])
    
    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class(MyPlotterPureTkinterStandAloneProcess_SetupDict)
            MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG
            
        except:
            exceptions = sys.exc_info()[0]
            print("MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject, exceptions: %s" % exceptions)
            #traceback.print_exc()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG != 1:
                print("Failed to open MyPlotterPureTkinterClass_Object.")
                ExitProgram_Callback()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    if USE_KEYBOARD_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        keyboard.on_press_key("esc", ExitProgram_Callback)
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    if EXIT_PROGRAM_FLAG == 0:
        print("$$$$$$$$$$$$$$ Starting test_program_for_MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class_NoParallelGUIprocess.py $$$$$$$$$$$$$$")
        StartingTime_CalculatedFromMainThread = getPreciseSecondsTimeStampString()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    while(EXIT_PROGRAM_FLAG == 0):

        ##########################################################################################################
        ##########################################################################################################
        CurrentTime_CalculatedFromMainThread = getPreciseSecondsTimeStampString() - StartingTime_CalculatedFromMainThread
        LoopCounter_CalculatedFromMainThread = LoopCounter_CalculatedFromMainThread + 1

        if CurrentTime_CalculatedFromMainThread > 60.0:
            ExitProgram_Callback()
        ##########################################################################################################
        ##########################################################################################################

        ######################################################################################################
        ######################################################################################################
        AmplitudeScalar = GetLatestWaveformValue(CurrentTime_CalculatedFromMainThread, 
                                                                1.0, 
                                                                10.0, 
                                                                PeriodicInput_Period_1, 
                                                                PeriodicInput_Type_1)
                                                                
        PeriodicInput_CalculatedValue_1 = GetLatestWaveformValue(CurrentTime_CalculatedFromMainThread, 
                                                                AmplitudeScalar*PeriodicInput_MinValue_1, 
                                                                AmplitudeScalar*PeriodicInput_MaxValue_1, 
                                                                PeriodicInput_Period_1, 
                                                                PeriodicInput_Type_1)
        ######################################################################################################
        ######################################################################################################

        ######################################################################################################
        ######################################################################################################

        ######################################################################################################
        PeriodicInput_CalculatedValue_2 = PeriodicInput_CalculatedValue_1*2.0 + 3.0
        ######################################################################################################

        ######################################################################################################
        NoiseCounter = NoiseCounter + 1
        if NoiseCounter == NoiseCounter_FireEveryNth:
            NoiseAmplitude = NoiseAmplitude_Percent0to1OfPeriodicInputAmplitude * abs(PeriodicInput_MaxValue_1 - PeriodicInput_MinValue_1)
            NoiseValue = random.uniform(-1.0 * NoiseAmplitude, NoiseAmplitude)
            PeriodicInput_CalculatedValue_2 = PeriodicInput_CalculatedValue_2 + NoiseValue
            NoiseCounter = 0
        ######################################################################################################
        
        ######################################################################################################
        ######################################################################################################

        ########################################################################################################### SET's
        ##########################################################################################################
        if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:

            ##########################################################################################################
            try:
                MoveGraphPositionCounter = MoveGraphPositionCounter + 1
                if MoveGraphPositionCounter == 150:
                    MovementScaleFactor = 0.5
                    MyPlotterPureTkinterStandAloneProcess_GUIparametersDict["GraphCanvasWidth"] = round(1380)
                    MyPlotterPureTkinterStandAloneProcess_GUIparametersDict["GraphCanvasHeight"] = round(820)
                    #MyPlotterPureTkinterStandAloneProcess_GUIparametersDict["GraphCanvasWindowStartingX"] = round(MovementScaleFactor*LoopCounter_CalculatedFromMainThread)
                    #MyPlotterPureTkinterStandAloneProcess_GUIparametersDict["GraphCanvasWindowStartingY"] = round(MovementScaleFactor*LoopCounter_CalculatedFromMainThread)
                    MyPlotterPureTkinterStandAloneProcess_SetupDict["GUIparametersDict"] = MyPlotterPureTkinterStandAloneProcess_GUIparametersDict

                    #MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalUpdateSetupDict(MyPlotterPureTkinterStandAloneProcess_SetupDict)

                    MoveGraphPositionCounter = 0
            ##########################################################################################################

            ##########################################################################################################
            except:
                exceptions = sys.exc_info()[0]
                print("MyPlotterPureTkinterStandAloneProcess, ProcessVariablesThatCanBeLiveUpdated: exceptions: %s" % exceptions)
                traceback.print_exc()
            ##########################################################################################################

            ##########################################################################################################
            try:

                MyPlotterPureTkinterStandAloneProcess_MostRecentDict = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.GetMostRecentDataDict()

                if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_MostRecentDict:
                    MyPlotterPureTkinterStandAloneProcess_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = MyPlotterPureTkinterStandAloneProcess_MostRecentDict["StandAlonePlottingProcess_ReadyForWritingFlag"]

                    if MyPlotterPureTkinterStandAloneProcess_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag == 1:
                        if CurrentTime_CalculatedFromMainThread - LastTime_CalculatedFromMainThread_MyPlotterPureTkinterStandAloneProcess >= 0.040:

                            #'''
                            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["PlotCurve1",
                                                                                                                                     "PlotCurve2"],
                                                                                                                                    [CurrentTime_CalculatedFromMainThread]*2,
                                                                                                                                    [PeriodicInput_CalculatedValue_1,
                                                                                                                                    PeriodicInput_CalculatedValue_2])
                            #'''

                            '''
                            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["PlotCurve3"],
                                                                                                                                    [CurrentTime_CalculatedFromMainThread]*1,
                                                                                                                                    [PeriodicInput_CalculatedValue_2])
                            '''

                            LastTime_CalculatedFromMainThread_MyPlotterPureTkinterStandAloneProcess = CurrentTime_CalculatedFromMainThread
            ##########################################################################################################

            ##########################################################################################################
            except:
                exceptions = sys.exc_info()[0]
                print("MyPlotterPureTkinterStandAloneProcess, exceptions: %s" % exceptions)
                #traceback.print_exc()
            ##########################################################################################################

        #########################################################################################################
        #########################################################################################################

        time.sleep(0.030)

    #########################################################################################################
    #########################################################################################################
    #########################################################################################################

    ######################################################################################################### THIS IS THE EXIT ROUTINE!
    #########################################################################################################
    print("Exiting test_program_for_MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class_NoParallelGUIprocess.py")

    #########################################################################################################
    if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:
        MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #########################################################################################################

    #########################################################################################################
    #########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
