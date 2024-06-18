# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision L, 06/17/2024

Verified working on: Python 3.8 for Windows 8.1, 10 64-bit, Ubuntu 20.04, and Raspberry Pi Buster (no Mac testing yet).
THE SEPARATE-PROCESS-SPAWNING COMPONENT OF THIS CLASS IS NOT AVAILABLE IN PYTHON 2 DUE TO LIMITATION OF
"multiprocessing.set_start_method('spawn')" ONLY BEING AVAILABLE IN PYTHON 3. PLOTTING WITHIN A SINGLE PROCESS STILL WORKS.
'''

__author__ = 'reuben.brewer'

#########################################################
from MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *
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
def TestButtonResponse():
    global MyPrint_ReubenPython2and3ClassObject
    global USE_MYPRINT_FLAG

    if USE_MYPRINT_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.my_print("Test Button was Pressed!")
    else:
        print("Test Button was Pressed!")
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MYPRINT_OPEN_FLAG

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject
    global USE_PLOTTER_FLAG
    global PLOTTER_OPEN_FLAG
    global SHOW_IN_GUI_PLOTTER_FLAG

    global PARENT_GUI_COUNTER

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            PARENT_GUI_COUNTER = PARENT_GUI_COUNTER + 1
            #MyPrint_ReubenPython2and3ClassObject.my_print("PID = " + str(os.getpid()) + ", PARENT_GUI_COUNTER: " + str(PARENT_GUI_COUNTER))

            #########################################################
            if MYPRINT_OPEN_FLAG == 1:
                MyPrint_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            #########################################################
            #if USE_PLOTTER_FLAG == 1 and PLOTTER_OPEN_FLAG == 1 and SHOW_IN_GUI_PLOTTER_FLAG == 1:
                #pass #DO NOT CALL MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.GUI_update_clock() as the plotter is firing its own, internal root.after callbacks faster than in this parent root GUI loop.
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
            #########################################################

        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback():
    global EXIT_PROGRAM_FLAG

    print("Exiting all threads in test_program_for_MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class.")

    EXIT_PROGRAM_FLAG = 1

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global GUI_RootAfterCallbackInterval_Milliseconds

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    #################################################
    #################################################

    #################################################
    TestButton = Button(root, text='Test Button', state="normal", width=20, command=lambda i=1: TestButtonResponse())
    TestButton.grid(row=0, column=0, padx=5, pady=1)
    #################################################

    #################################################
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################

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

    global USE_MYPRINT_FLAG
    USE_MYPRINT_FLAG = 1

    global USE_GUI_FLAG
    USE_GUI_FLAG = 1
    
    global USE_SINUSOIDAL_TEST_FLAG
    USE_SINUSOIDAL_TEST_FLAG = 1
    ################################################
    ################################################

    ################################################
    ################################################
    global SHOW_IN_GUI_PLOTTER_FLAG
    SHOW_IN_GUI_PLOTTER_FLAG = 1

    global SHOW_IN_GUI_MYPRINT_FLAG
    SHOW_IN_GUI_MYPRINT_FLAG = 1
    ################################################
    ################################################

    ################################################
    ################################################
    global GUI_ROW_MYPRINT
    global GUI_COLUMN_MYPRINT
    global GUI_PADX_MYPRINT
    global GUI_PADY_MYPRINT
    global GUI_ROWSPAN_MYPRINT
    global GUI_COLUMNSPAN_MYPRINT
    GUI_ROW_MYPRINT = 2

    GUI_COLUMN_MYPRINT = 0
    GUI_PADX_MYPRINT = 1
    GUI_PADY_MYPRINT = 10
    GUI_ROWSPAN_MYPRINT = 1
    GUI_COLUMNSPAN_MYPRINT = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global root

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject

    global PLOTTER_OPEN_FLAG
    PLOTTER_OPEN_FLAG = -1

    global MyPrint_ReubenPython2and3ClassObject

    global MYPRINT_OPEN_FLAG
    MYPRINT_OPEN_FLAG = -1
    
    global PARENT_GUI_COUNTER
    PARENT_GUI_COUNTER = 0
    
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
    
    #################################################  KEY GUI LINE
    #################################################
    if USE_GUI_FLAG == 1:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread)
        GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        GUI_Thread_ThreadingObject.start()
        time.sleep(0.5)  #Allow enough time for 'root' to be created that we can then pass it into other classes.
    else:
        root = None
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
            PLOTTER_OPEN_FLAG = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject, exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1:

        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MYPRINT_FLAG),
                                                                        ("root", root),
                                                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                        ("GUI_ROW", GUI_ROW_MYPRINT),
                                                                        ("GUI_COLUMN", GUI_COLUMN_MYPRINT),
                                                                        ("GUI_PADX", GUI_PADX_MYPRINT),
                                                                        ("GUI_PADY", GUI_PADY_MYPRINT),
                                                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MYPRINT),
                                                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MYPRINT)])

        MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 10),
                                                                ("WidthOfPrintingLabel", 200),
                                                                ("PrintToConsoleFlag", 1),
                                                                ("LogFileNameFullPath", os.getcwd() + "//TestLog.txt"),
                                                                ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            time.sleep(0.25)
            MYPRINT_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_PLOTTER_FLAG == 1 and PLOTTER_OPEN_FLAG != 1:
        print("Failed to open MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1 and MYPRINT_OPEN_FLAG != 1:
        print("Failed to open MyPrint_ReubenPython2and3ClassObject.")
        ExitProgram_Callback()
    #################################################
    #################################################

    MyPrint_ReubenPython2and3ClassObject.my_print("$$$$$$$$$$$$$$ STARTING MAIN LOOP $$$$$$$$$$$$$$")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

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
        if PLOTTER_OPEN_FLAG == 1:

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
                TimeGain = math.pi / (2.0 * SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle)
                DesiredAngleDeg_1 = 0.5*(SINUSOIDAL_MOTION_INPUT_MaxValue + SINUSOIDAL_MOTION_INPUT_MinValue) + math.exp(0.1*CurrentTime_MainLoopThread)*0.5 * abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue) * math.sin(TimeGain * CurrentTime_MainLoopThread)  # AUTOMATIC SINUSOIDAL MOVEMENT
                DesiredAngleDeg_2 = 0.5*(SINUSOIDAL_MOTION_INPUT_MaxValue + SINUSOIDAL_MOTION_INPUT_MinValue) + math.exp(0.05*CurrentTime_MainLoopThread)*0.5 * abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue) * math.cos(TimeGain * CurrentTime_MainLoopThread)  # AUTOMATIC SINUSOIDAL MOVEMENT
                DesiredAngleDeg_3 = 0.25*(SINUSOIDAL_MOTION_INPUT_MaxValue + SINUSOIDAL_MOTION_INPUT_MinValue) + math.exp(0.03*CurrentTime_MainLoopThread)*0.5 * abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue) * math.tan(TimeGain * CurrentTime_MainLoopThread)  # AUTOMATIC SINUSOIDAL MOVEMENT

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
    if MYPRINT_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if PLOTTER_OPEN_FLAG == 1:
        MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    #################################################

##########################################################################################################
##########################################################################################################
