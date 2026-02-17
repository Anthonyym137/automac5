import os
import sys
import time
import socket
import random
import psutil
import platform
import subprocess


def clear_terminal():
	"""Clears the terminal screen."""
	subprocess.run(['clear'])


def is_root():
	"""Performs a root permission check."""
	if os.geteuid() != 0:
		os.execvp('sudo', ['sudo', 'python3'] + sys.argv)


def get_interfaces():
	"""Returns the active network interfaces and the active MAC addresses on the interfaces."""
	interfaces = psutil.net_if_addrs()
	if 'lo' in interfaces.keys():
		del interfaces['lo']

	for itf in interfaces.keys():
		for addr in interfaces[itf]:
			if addr.family == psutil.AF_LINK:
				interfaces[itf] = addr.address

	return interfaces


def random_mac():
	"""Generates local MAC addresses according to IEEE standards."""
	mac = ''
	hexchars = '0123456789abcdef'
	for i in range(1, 18):
		if i ==2:
			mac += random.choice('26ae')
			continue
		if i%3 ==0:
			mac += ':'
			continue
		mac += random.choice(hexchars)
	return mac


def check_connection():
	"""Checks the status of the Internet connection."""
	try:
		socket.setdefaulttimeout(3)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(('8.8.8.8', 53))
		return True
	except socket.error:
		return False


def main():
	"""Main Program."""
	clear_terminal()
	is_root()
	try:
		while True:
			interfaces = get_interfaces()
			macaddress = random_mac()
			for itf in interfaces.keys():
				subprocess.run(['nmcli', 'device', 'set', itf, 'managed', 'no'])
				subprocess.run(['dhclient', '-r', itf])
				time.sleep(1)

				subprocess.run(['ip', 'link', 'set', itf, 'down'])
				time.sleep(2)

				subprocess.run(['ifconfig', itf, 'hw', 'ether', macaddress])
				subprocess.run(['ip', 'link', 'set', itf, 'up'])
				time.sleep(2)

				subprocess.run(['nmcli', 'device', 'set', itf, 'managed', 'yes'])
				print('\n'+interfaces[itf]+'  -->  '+macaddress+f'\tinterface: ({itf})')

			while not check_connection():
				print('\r\033[93mConnection Waiting...\033[0m', end="", flush=True)

			print('\n\033[96m[+] Connection Established.\033[0m\n')

			timer = 0
			while timer <= 300:
				print(f'\r\033[92m{300-timer} s. cooldown\033[0m', end="", flush=True)
				timer += 1
				time.sleep(1)

	except KeyboardInterrupt:
		print('\033[91mShutdowning...\033[0m')
		for itf in interfaces.keys():
			subprocess.run(['ip', 'link', 'set', itf, 'up'])
			time.sleep(2)
			subprocess.run(['nmcli', 'device', 'set', itf, 'managed', 'yes'])

		print('\033[91mThe Program has been shutdown\033[0m')
		sys.exit(0)


if __name__ == '__main__':
	main()
