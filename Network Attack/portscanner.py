"""
Function:       				Multi-Thread Port Scanner
Created Date:           02.09.2019
Updated Date:						06.07.2021
Created By:     				Anonymous Systems (0_o)
Dependencies:						None
Reference:							http://index-of.es/Varios-2/Hacking%20with%20Python%20The%20Ultimate%20Beginner's%20Guide.pdf
"""

import threading
import socket
from queue import Queue
import time


class PortScanner:
	def __init__(self, host_input, port_min_input, port_max_input, threads_input):
		host_input = host_input
		port_min_input = port_min_input
		port_max_input = port_max_input
		threads_input = threads_input
		lock = threading.Lock()
		self.handle_inputs(host_input, port_min_input, port_max_input, threads_input)

		# Create Queue
		self.q = Queue()

		# Invoke threads to begin checking ports
		for n in range(self.threads):
				t = threading.Thread(target=self.threader)
				t.daemon = True
				t.start()

		# Input requested ports into queue
		for port in range(self.port_min, self.port_max):
				self.q.put(port)

		# Blocks until all tasks are finished
		self.q.join()

	def handle_inputs(self, host_input, port_min_input, port_max_input, threads_input):
		'''Scan port(s) of host machine'''
    # Target source determined
		if host_input == "":
				self.host = '127.0.0.1'
				print(f"Checking the following source: {self.host}")
		else:
				self.host = host_input
				print(f"Checking the following source: {self.host}")
    # Starting port determined
		if port_min_input == "":
				self.port_min = 1
				print(f"Starting at port: {self.port_min}")
		else:
				self.port_min = int(port_min_input)
				print(f"Starting at port: {self.port_min}")
    # Ending port determined
		if port_max_input == "":
				self.port_max = 65535 + 1
				self.port_max_actual = self.port_max - 1
				print(f"Ending at port: {self.port_max_actual}")
		else:
				self.port_max = int(port_max_input) + 1
				self.port_max_actual = self.port_max - 1
				print(f"Ending at port: {self.port_max_actual}")
    # Threads value determined
		if threads_input == "":
				self.threads = 300
				print(f"Spawning {self.threads} threads...")
		else:
				self.threads = int(threads_input)
				print(f"Spawning {self.threads} threads...")

		print(f'Please Wait, scanning ports {self.port_min}-{self.port_max_actual} on remote host {self.host}')

	# Function to Check Port
	def check_port(self, host, port):
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					r = s.connect_ex((host, port))
					if r == 0:
									print(f"[!] Port {port} is OPEN [!]")
					else: pass

	# Function to invoke check_port() on each port in queue
	def threader(self):
			while True:
					port = self.q.get()
					self.check_port(self.host, port)
					self.q.task_done()


if __name__ == '__main__':
    host_input = input("Enter a remote host to scan or leave blank for default(127.0.0.1): ")
    port_min_input = input("Please enter starting port number or leave blank for default(1): ")
    port_max_input = input("Please enter ending port number or leave blank for default(65535): ")
    threads_input = input("Please enter number of threads to run simultaneously or leave blank for default(300): ")

    # Start Stopwatch for threads execution time
    time_start = time.perf_counter()

    PortScanner(host_input, port_min_input, port_max_input, threads_input)

    # Stop Stopwatch for threads execution time
    time_end = time.perf_counter()
    cal = time_end - time_start
    if cal > 60:
        cal = cal / 60
        print(f"\nScanner completed in {cal}mins")
    else:
        print(f"\nScanner completed in {cal}secs")
