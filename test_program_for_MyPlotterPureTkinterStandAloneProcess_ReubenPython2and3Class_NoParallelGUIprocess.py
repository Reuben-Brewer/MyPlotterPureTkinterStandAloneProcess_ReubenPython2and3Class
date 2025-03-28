# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision R, 03/27/2025

Verified working on: Python 3.12 for Windows 11 64-bit, Ubuntu 20.04, and Raspberry Pi Buster.
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
if __name__ == '__main__':

    #################################################
    #################################################
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
    #################################################
    #################################################

    ################################################
    ################################################
    global USE_MyPlotterPureTkinterStandAloneProcess_FLAG
    USE_MyPlotterPureTkinterStandAloneProcess_FLAG = 1
    
    global USE_KEYBOARD_FLAG
    USE_KEYBOARD_FLAG = 1
    
    global USE_SINUSOIDAL_TEST_FLAG
    USE_SINUSOIDAL_TEST_FLAG = 1
    ################################################
    ################################################

    ################################################
    ################################################
    global SHOW_IN_GUI_MyPlotterPureTkinterStandAloneProcess_FLAG
    SHOW_IN_GUI_MyPlotterPureTkinterStandAloneProcess_FLAG = 1
    ################################################
    ################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30

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
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject

    global MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG
    MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPlotterPureTkinter_MostRecentDict
    MyPlotterPureTkinter_MostRecentDict = dict()

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = -1



    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict = dict([("EnableInternal_MyPrint_Flag", 1),
                                                                                                ("NumberOfPrintLines", 10),
                                                                                                ("GraphCanvasWidth", 1280),
                                                                                                ("GraphCanvasHeight", 700),
                                                                                                ("GraphCanvasWindowStartingX", 0),
                                                                                                ("GraphCanvasWindowStartingY", 0),
                                                                                                ("GraphCanvasWindowTitle", "My plotting example!"),
                                                                                                ("GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents", 20)])
    
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                                        ("ParentPID", os.getpid()),
                                                                                        ("WatchdogTimerDurationSeconds_ExpirationWillEndStandAlonePlottingProcess", 5.0),
                                                                                        ("MarkerSize", 3),
                                                                                        ("LineWidth", 3),
                                                                                        ("CurvesToPlotNamesAndColorsDictOfLists", dict([("NameList", ["PlotCurve0", "PlotCurve1", "PlotCurve2"]),("ColorList", ["Red", "Green", "Blue"])])),
                                                                                        ("NumberOfDataPointToPlot", 25),
                                                                                        ("XaxisNumberOfTickMarks", 10),
                                                                                        ("YaxisNumberOfTickMarks", 10),
                                                                                        ("XaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("YaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("XaxisAutoscaleFlag", 1),
                                                                                        ("YaxisAutoscaleFlag", 1),
                                                                                        ("X_min", 0.0),
                                                                                        ("X_max", 5.0),
                                                                                        ("Y_min", -5.0),
                                                                                        ("Y_max", 5.0),
                                                                                        ("XaxisDrawnAtBottomOfGraph", 0),
                                                                                        ("XaxisLabelString", "Time (sec)"),
                                                                                        ("YaxisLabelString", "Y-units (units)"),
                                                                                        ("ShowLegendFlag", 1)])
    
    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class(MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict)
            MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG
            
        except:
            exceptions = sys.exc_info()[0]
            print("MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject, exceptions: %s" % exceptions)
            #traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG != 1:
                print("Failed to open MyPlotterPureTkinterClass_Object.")
                ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_KEYBOARD_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        keyboard.on_press_key("esc", ExitProgram_Callback)
    #################################################
    #################################################

    #################################################
    #################################################
    if EXIT_PROGRAM_FLAG == 0:
        StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()
    #################################################
    #################################################

    while(EXIT_PROGRAM_FLAG == 0):

        #################################################
        #################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread

        if CurrentTime_MainLoopThread > 10.0:
            ExitProgram_Callback()
        #################################################
        #################################################

        #################################################
        #################################################
        if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:

            #################################################
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.GetMostRecentDataDict()
            #print(str(MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict))

            if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict:
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict["StandAlonePlottingProcess_ReadyForWritingFlag"]
            else:
                pass
            #################################################

            #################################################
            if USE_SINUSOIDAL_TEST_FLAG == 1:
                TimeGain = math.pi / (2.0 * SinusoidalMotionInput_ROMtestTimeToPeakAngle)
                DesiredAngleDeg_1 = 0.5*(SinusoidalMotionInput_MaxValue + SinusoidalMotionInput_MinValue) + math.exp(0.1*CurrentTime_MainLoopThread)*0.5 * abs(SinusoidalMotionInput_MaxValue - SinusoidalMotionInput_MinValue) * math.sin(TimeGain * CurrentTime_MainLoopThread)  # AUTOMATIC SINUSOIDAL MOVEMENT
                DesiredAngleDeg_2 = 0.5*(SinusoidalMotionInput_MaxValue + SinusoidalMotionInput_MinValue) + math.exp(0.05*CurrentTime_MainLoopThread)*0.5 * abs(SinusoidalMotionInput_MaxValue - SinusoidalMotionInput_MinValue) * math.cos(TimeGain * CurrentTime_MainLoopThread)  # AUTOMATIC SINUSOIDAL MOVEMENT
                DesiredAngleDeg_3 = 0.25*(SinusoidalMotionInput_MaxValue + SinusoidalMotionInput_MinValue) + math.exp(0.03*CurrentTime_MainLoopThread)*0.5 * abs(SinusoidalMotionInput_MaxValue - SinusoidalMotionInput_MinValue) * math.tan(TimeGain * CurrentTime_MainLoopThread)  # AUTOMATIC SINUSOIDAL MOVEMENT

                if MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag == 1:
                    #pass
                    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot("PlotCurve0", CurrentTime_MainLoopThread, DesiredAngleDeg_1)
                    #MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot("PlotCurve1", CurrentTime_MainLoopThread, DesiredAngleDeg_2)
                    #MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot("PlotCurve2", CurrentTime_MainLoopThread, DesiredAngleDeg_3)

                time.sleep(0.050)
            #################################################

        ##################################################
        ##################################################

    ################################################# THIS IS THE EXIT ROUTINE!
    #################################################
    print("MAIN LEADER PROGRAM Exiting main program 'test_program_for_MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class_NoParallelGUIprocess.")

    #################################################
    if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:
        MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    #################################################

##########################################################################################################
##########################################################################################################
