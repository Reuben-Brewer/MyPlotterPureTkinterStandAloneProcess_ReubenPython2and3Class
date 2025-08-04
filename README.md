########################

MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class

Pure-Tkinter real-time data-plotting class, launched as a separate process (with separate Python interpreter) so as not
to slow-down other code due to Python's GIL (Global Interpreter Lock).

Reuben Brewer, Ph.D.

reuben.brewer@gmail.com,

www.reubotics.com

Apache 2 License

Software Revision X, 08/03/2025

Verified working on:

Python 3.11/3.12 for

Windows 10/11 64-bit

Ubuntu 20.04, and

and Raspberry Pi 4/5 Bookworm.

THE SEPARATE-PROCESS-SPAWNING COMPONENT OF THIS CLASS IS NOT 
AVAILABLE IN PYTHON 2 DUE TO LIMITATION OF "multiprocessing.set_start_method('spawn')" 
ONLY BEING AVAILABLE IN PYTHON 3. PLOTTING WITHIN A SINGLE PROCESS STILL WORKS.

########################  

######################## Python module installation instructions, all OS's

MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class, ListOfModuleDependencies: ['GetCPUandMemoryUsageOfProcessByPID_ReubenPython3Class', 'numpy', 'pexpect', 'psutil', 'pyautogui']

MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class, ListOfModuleDependencies_TestProgram: ['keyboard', 'MyPrint_ReubenPython2and3Class']

MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class, ListOfModuleDependencies_NestedLayers: ['future.builtins', 'psutil']

MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class, ListOfModuleDependencies_All:['future.builtins', 'GetCPUandMemoryUsageOfProcessByPID_ReubenPython3Class', 'keyboard', 'MyPrint_ReubenPython2and3Class', 'numpy', 'pexpect', 'psutil', 'pyautogui']

########################
