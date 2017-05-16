import sys
import serial
import glob
import time
#import struct

def serial_ports():
	"""Lists serial ports

	:raises EnvironmentError:
	    On unsupported or unknown platforms
	:returns:
	    A list of available serial ports
	"""
	if sys.platform.startswith('win'):
		ports = ['COM' + str(i + 1) for i in range(256)]

	elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
		# this is to exclude your current terminal "/dev/tty"
		ports = glob.glob('/dev/tty[A-Za-z]*')

	elif sys.platform.startswith('darwin'):
		ports = glob.glob('/dev/tty.*')

	else:
		raise EnvironmentError('Unsupported platform')

	result = []
	for port in ports:
		try:
			s = serial.Serial(port)
			s.close()
			result.append(port)
		except (OSError, serial.SerialException):
			pass
	
	return result
	

def arduino_echo(out_msg, in_msg_len, brate):

	res = ["",""]	
	ports = serial_ports()
	for port in ports:
		try:
			sp = serial.Serial(port, brate, timeout=1)
			time.sleep(2.0)			
			sp.write(out_msg)
			res = [sp.read(in_msg_len), port]

			sp.close()
			break

		except (OSError, serial.SerialException):
			pass
			
	return res


