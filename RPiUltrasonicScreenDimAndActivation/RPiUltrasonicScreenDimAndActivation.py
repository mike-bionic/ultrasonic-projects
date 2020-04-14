import RPi.GPIO as GPIO
import os
GPIO.setmode(GPIO.BCM)
signal = 12

max_timeout = 20
timeout = 0
monitor_state = 1

GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)

def monitor_power(status, monitor_state):
	if status == 1:
		if monitor_state == 0:
			os.system('tvservice --off')
		return 1
	elif status == 0:
		if monitor_state == 1:
			os.system('tvservice --preferred')
		return  0


while True:
	state = GPIO.input(signal)
	if state == False:
		timeout = 0
		monitor_state = monitor_power(1, monitor_state)
		print('off')
	else:
		# timeout = 0
		monitor_state = monitor_power(0, monitor_state)
		print('on')

	timeout += 1
	if timeout >= max_timeout:
		timeout = 0
		monitor_state = monitor_power(0, monitor_state)



