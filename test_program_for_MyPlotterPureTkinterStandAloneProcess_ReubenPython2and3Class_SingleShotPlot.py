# -*- coding: utf-8 -*-

'''
Reuben Brewer, reuben.brewer@gmail.com, www.reubotics.com
Apache 2 License
Software Revision B, 08/15/2019

Verified working on: Python 2.7 and 3 for Windows 8.1 64-bit and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

from MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *

import os, sys, platform
import time, datetime
import threading
import collections
import math, numpy
import traceback
import re

###############
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
###############

###############
if sys.version_info[0] < 3:
    from builtins import raw_input as input
else:
    from future.builtins import input as input #"sudo pip3 install future" (Python 3) AND "sudo pip install future" (Python 2)
###############

##########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
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
    global USE_PLOTTER_FLAG
    USE_PLOTTER_FLAG = 1
    ################################################
    ################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject

    global PLOTTER_OPEN_FLAG
    PLOTTER_OPEN_FLAG = -1

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle
    SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle = 2.0

    global SINUSOIDAL_MOTION_INPUT_MinValue
    SINUSOIDAL_MOTION_INPUT_MinValue = -50

    global SINUSOIDAL_MOTION_INPUT_MaxValue
    SINUSOIDAL_MOTION_INPUT_MaxValue = 50
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
                                                                                                ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                                                ("GraphCanvasWidth", 1280),
                                                                                                ("GraphCanvasHeight", 700),
                                                                                                ("GraphCanvasWindowStartingX", 0),
                                                                                                ("GraphCanvasWindowStartingY", 0),
                                                                                                ("GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents", 20)])

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                                        ("ParentPID", os.getpid()),
                                                                                        ("WatchdogTimerDurationSeconds_ExpirationWillEndStandAlonePlottingProcess", 1.0),
                                                                                        ("MarkerSize", 3),
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

    if USE_PLOTTER_FLAG == 1:
        try:
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class(MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict)
            time.sleep(0.25)
            PLOTTER_OPEN_FLAG = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject, exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if PLOTTER_OPEN_FLAG != 1:
        print("Failed to open MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.")
        input("Press any key (and enter) to exit.")
        sys.exit()
    #################################################
    #################################################

    ################################################# SINGLE-SHOT PLOT EXAMPLE, WatchdogTimerDurationSeconds_ExpirationWillEndStandAlonePlottingProcess must be 0
    #################################################
    TimeList = list()
    DesiredAngleDeg_1_List = list()

    for TimeIndex in range(0, 100):
        TimeGain = math.pi / (2.0 * SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle)
        DesiredAngleDeg_1 = 0.5*(SINUSOIDAL_MOTION_INPUT_MaxValue + SINUSOIDAL_MOTION_INPUT_MinValue) + math.exp(0.1*TimeIndex)*0.5 * abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue) * math.sin(TimeGain * TimeIndex)  # AUTOMATIC SINUSOIDAL MOVEMENT
        TimeList.append(TimeIndex)
        DesiredAngleDeg_1_List.append(DesiredAngleDeg_1)

    print("TimeList: " + str(TimeList))
    print("DesiredAngleDeg_1_List: " + str(DesiredAngleDeg_1_List))

    if USE_PLOTTER_FLAG == 1:

        while 1:
            #################################################
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.GetMostRecentDataDict()
            if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict:
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict["StandAlonePlottingProcess_ReadyForWritingFlag"]
            else:
                pass
            #################################################

            if MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag == 1:
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot("PlotCurve0", TimeList, DesiredAngleDeg_1_List)
                break

    input("Please press any key to continue...")
    #################################################
    ################################################# SINGLE-SHOT PLOT EXAMPLE, WatchdogTimerDurationSeconds_ExpirationWillEndStandAlonePlottingProcess must be 0
