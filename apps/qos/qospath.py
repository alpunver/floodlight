#! /usr/bin/python
"""
QoSPath.py ---------------------------------------------------------------------------------------------------
Developed By: Ryan Wallner (ryan.wallner1@marist.edu)
Add QoS to a specific path in the network. Utilized circuit pusher developed by KC Wang
[Note]
	*circuitpusher.py is needed in the same directory for this application to run
	 succesfully!

 USAGE: 
		qospath.py <add|delete>	 <source-ip> <dest-ip> <policy> <controller-ip>
 		*note: This adds the Quality of Service to each switch along the path between hosts
-----------------------------------------------------------------------------------------------------------------------
"""

import os
import simplejson #used to process policies and encode/decode requests
import subprocess #spawning subprocesses

##Get switches in a cirtcute using cirtcuit pusher (may need to modify to get all switches in path)
##Then use the add policy to a switch in QoSService to add a service along a path.

def main():
	#checks
	if (len(sys.argv) == 2):
	 if sys.argv[1] == "--help":
	  usage_help()
	  exit()
	if (len(sys.argv)) != 6:
	 usage()
	 exit()

#TODO

def usage():
	print '''type "qos_pusher.py --help" for more details
	             qospath.py <add|delete>	 <source-ip> <dest-ip> <policy> <controller-ip>'''
def usage_help():
	print '''
	        ###################################
		QoSPath.py
		Author: Ryan Wallner (Ryan.Wallner1@marist.edu)
		QoSPath is a simple service that utilizes KC Wang's 
		CircuitPusher  to push Quality of Service along a
		specific path in the network.
		
		[Note]
			*Use the "name" of the policy you want to add in the path
			visit "http://controller-ip:8080/wm/qos/policy/json" to get a list of policies
			
		To Add a service:
		qospath.py add  10.0.0.1  10.0.0.2  "Add ToS 45" 127.0.0.1
		qospath.py delete  10.0.0.1  10.0.0.2  "Add ToS 45" 127.0.0.1  
		
		qospath.py add  10.0.0.1  10.0.0.2  "Enqueue 1:0" 127.0.0.1 
		qospath.py delete  10.0.0.1  10.0.0.2  "Enqueue 1:0" 127.0.0.1
			
		###################################
		'''
#Call main
if  __name__ == "__main__" :
	main()