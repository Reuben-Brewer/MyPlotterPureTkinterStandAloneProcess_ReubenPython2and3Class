# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision Z, 10/02/2025

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

########################################################################################################## MUST ISSUE CTRLc_RegisterHandlerFunction() AT START OF PROGRAM
##########################################################################################################
def CTRLc_RegisterHandlerFunction():

    CurrentHandlerRegisteredForSIGINT = signal.getsignal(signal.SIGINT)
    #print("CurrentHandlerRegisteredForSIGINT: " + str(CurrentHandlerRegisteredForSIGINT))

    defaultish = (signal.SIG_DFL, signal.SIG_IGN, None, getattr(signal, "default_int_handler", None)) #Treat Python's built-in default handler as "unregistered"

    if CurrentHandlerRegisteredForSIGINT in defaultish: # Only install if it's default/ignored (i.e., nobody set it yet)
        signal.signal(signal.SIGINT, CTRLc_HandlerFunction)
        print("test_program_for_MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class_SingleShotPlot.py, CTRLc_RegisterHandlerFunction event fired!")

    else:
        print("test_program_for_MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class_SingleShotPlot.py, could not register CTRLc_RegisterHandlerFunction (already registered previously)")
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
##########################################################################################################
if __name__ == '__main__':

    ##########################################################################################################
    ##########################################################################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    CTRLc_RegisterHandlerFunction()
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
    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global SinusoidalMotionInput_ROMtestTimeToPeakAngle
    SinusoidalMotionInput_ROMtestTimeToPeakAngle = 2.0

    global SinusoidalMotionInput_MinValue
    SinusoidalMotionInput_MinValue = -50

    global SinusoidalMotionInput_MaxValue
    SinusoidalMotionInput_MaxValue = 50
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    global MyPlotterPureTkinterStandAloneProcess_Object

    global MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG
    MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = -1

    global MyPlotterPureTkinterStandAloneProcess_MostRecentDict
    MyPlotterPureTkinterStandAloneProcess_MostRecentDict = dict()

    global MyPlotterPureTkinterStandAloneProcess_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag
    MyPlotterPureTkinterStandAloneProcess_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = -1

    global LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess
    LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess = -11111.0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    global MyPlotterPureTkinterStandAloneProcess_Object_GUIparametersDict
    MyPlotterPureTkinterStandAloneProcess_Object_GUIparametersDict = dict([("EnableInternal_MyPrint_Flag", 1),
                                                                                                ("NumberOfPrintLines", 10),
                                                                                                ("GraphCanvasWidth", 1280),
                                                                                                ("GraphCanvasHeight", 700),
                                                                                                ("GraphCanvasWindowStartingX", 0),
                                                                                                ("GraphCanvasWindowStartingY", 0),
                                                                                                ("GraphCanvasWindowTitle", "My plotting example!"),
                                                                                                ("GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents", 20)])

    global MyPlotterPureTkinterStandAloneProcess_SetupDict
    MyPlotterPureTkinterStandAloneProcess_SetupDict = dict([("GUIparametersDict", MyPlotterPureTkinterStandAloneProcess_Object_GUIparametersDict),
                                                                                        ("ParentPID", os.getpid()),
                                                                                        ("WatchdogTimerDurationSeconds_ExpirationWillEndStandAlonePlottingProcess", 10.0),
                                                                                        ("CurvesToPlotNamesAndColorsDictOfLists", dict([("NameList", ["PlotCurve0", "PlotCurve1", "PlotCurve2"]),
                                                                                                                                        ("MarkerSizeList", [3, 2, 1]),
                                                                                                                                        ("LineWidthList", [2, 1, 0]),
                                                                                                                                        ("ColorList", ["Red", "Green", "Blue"])])),
                                                                                        ("SmallTextSize", 7),
                                                                                        ("LargeTextSize", 12),
                                                                                        ("NumberOfDataPointToPlot", 100),
                                                                                        ("XaxisNumberOfTickMarks", 10),
                                                                                        ("YaxisNumberOfTickMarks", 10),
                                                                                        ("XaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("YaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("XaxisAutoscaleFlag", 0),
                                                                                        ("YaxisAutoscaleFlag", 0),
                                                                                        ("X_min", 0.0),
                                                                                        ("X_max", 10.0),
                                                                                        ("Y_min", 1.1*SinusoidalMotionInput_MinValue),
                                                                                        ("Y_max", 1.1*SinusoidalMotionInput_MaxValue),
                                                                                        ("XaxisDrawnAtBottomOfGraph", 0),
                                                                                        ("XaxisLabelString", "Time (sec)"),
                                                                                        ("YaxisLabelString", "Y-units (units)"),
                                                                                        ("ShowLegendFlag", 1),
                                                                                        ("KeepPlotterWindowAlwaysOnTopFlag", 0),
                                                                                        ("RemoveTitleBorderCloseButtonAndDisallowWindowMoveFlag", 0),
                                                                                        ("AllowResizingOfWindowFlag", 1)])

    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            MyPlotterPureTkinterStandAloneProcess_Object = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class(MyPlotterPureTkinterStandAloneProcess_SetupDict)
            MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = MyPlotterPureTkinterStandAloneProcess_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPlotterPureTkinterStandAloneProcess_Object, exceptions: %s" % exceptions)
            traceback.print_exc()
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

    ########################################################################################################## SINGLE-SHOT PLOT EXAMPLE, WatchdogTimerDurationSeconds_ExpirationWillEndStandAlonePlottingProcess must be 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    TimeList = list()
    DesiredAngleDeg_1_List = list()

    Time = 0.0
    for TimeIndex in range(0, 100):
        Time = 0.1*TimeIndex
        TimeGain = math.pi / (2.0 * SinusoidalMotionInput_ROMtestTimeToPeakAngle)
        DesiredAngleDeg_1 = 0.5*(SinusoidalMotionInput_MaxValue + SinusoidalMotionInput_MinValue) + 0.5*abs(SinusoidalMotionInput_MaxValue - SinusoidalMotionInput_MinValue) * math.sin(TimeGain * Time)
        TimeList.append(Time)
        DesiredAngleDeg_1_List.append(DesiredAngleDeg_1)
    ##########################################################################################################
    ##########################################################################################################

    print("Starting test_program_for_MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class_SingleShotPlot.py")
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:

        StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

        SingleShotFiredFLag = 0

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        while(EXIT_PROGRAM_FLAG == 0):

            ##########################################################################################################
            ##########################################################################################################
            CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread

            if CurrentTime_MainLoopThread > 20.0:
                ExitProgram_Callback()
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################SET's
            ##########################################################################################################
            if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1 and SingleShotFiredFLag == 0:

                ##########################################################################################################
                try:

                    MyPlotterPureTkinterStandAloneProcess_MostRecentDict = MyPlotterPureTkinterStandAloneProcess_Object.GetMostRecentDataDict()

                    if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_MostRecentDict:
                        MyPlotterPureTkinterStandAloneProcess_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = MyPlotterPureTkinterStandAloneProcess_MostRecentDict["StandAlonePlottingProcess_ReadyForWritingFlag"]

                        if MyPlotterPureTkinterStandAloneProcess_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag == 1:
                            if CurrentTime_MainLoopThread - LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess >= 0.040:

                                MyPlotterPureTkinterStandAloneProcess_Object.ExternalAddPointOrListOfPointsToPlot(["PlotCurve0"],
                                                                                                                    [TimeList],
                                                                                                                    [DesiredAngleDeg_1_List],
                                                                                                                    OverrideCurveAndPointListsMustMatchInLengthFlag=1)
                                LastTime_MainLoopThread_MyPlotterPureTkinterStandAloneProcess = CurrentTime_MainLoopThread

                                SingleShotFiredFLag = 1
                ##########################################################################################################

                ##########################################################################################################
                except:
                    exceptions = sys.exc_info()[0]
                    print("MyPlotterPureTkinterStandAloneProcess, exceptions: %s" % exceptions)
                    #traceback.print_exc()
                ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################

            time.sleep(0.030)

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ########################################################################################################## SINGLE-SHOT PLOT EXAMPLE, WatchdogTimerDurationSeconds_ExpirationWillEndStandAlonePlottingProcess must be 0

    ########################################################################################################## THIS IS THE EXIT ROUTINE!
    ##########################################################################################################
    print("Exiting test_program_for_MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class_SingleShotPlot.py")

    ##########################################################################################################
    if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:
        MyPlotterPureTkinterStandAloneProcess_Object.ExitProgram_Callback()
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
