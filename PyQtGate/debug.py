# Use debug.dtrace() in the part of code to start watching
# type n for next step
# type s to step in subroutine (the n key jumps through the subrotines)
# type r to continue just to the end of the subrotine without stepping
# type c to continue to the end of the hole code without stepping
# type p var to watch actual var value
# type q to abruptly terminate de code
# type l to see where in the code you are

def dtrace():
	'''Set a tracepoint in the Python debugger that works with Qt'''
	from PyQt4.QtCore import pyqtRemoveInputHook
	from pdb import set_trace
	pyqtRemoveInputHook()
	set_trace()
