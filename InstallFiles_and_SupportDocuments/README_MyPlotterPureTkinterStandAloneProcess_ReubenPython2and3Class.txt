########################  

MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class

Pure-Tkinter real-time data-plotting class, launched as a separate process (with separate Python interpreter) so as not
to slow-down other code due to Python's GIL (Global Interpreter Lock).

Reuben Brewer
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License

Software Revision G, 07/18/2022

Verified working on: 
Python 3.8 for Windows 8.1, 10 64-bit and Raspberry Pi Buster (no Mac testing yet).
THE SEPARATE-PROCESS-SPAWNING COMPONENT OF THIS CLASS IS NOT 
AVAILABLE IN PYTHON 2 DUE TO LIMITATION OF "multiprocessing.set_start_method('spawn')" 
ONLY BEING AVAILABLE IN PYTHON 3. PLOTTING WITHIN A SINGLE PROCESS STILL WORKS.

########################  

########################### Python module installation instructions, all OS's

MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class, ListOfModuleDependencies: ['future.builtins', 'numpy', 'pexpect', 'psutil']
MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class, ListOfModuleDependencies_TestProgram: ['future.builtins', 'MyPrint_ReubenPython2and3Class']
MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class, ListOfModuleDependencies_NestedLayers: ['future.builtins']
MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class, ListOfModuleDependencies_All: ['future.builtins', 'MyPrint_ReubenPython2and3Class', 'numpy', 'pexpect', 'psutil']

###########################