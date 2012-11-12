import os
import json

switches = {}
controllerIP = '10.100.14.71'
cport = '8080'
data  = os.popen('curl -s http://'+controllerIP+ ':'+cport+'/wm/core/controller/switches/json').read()

switches = json.loads(data)


for i in range(len(switches)):
	#print switches[i]
	print 'switch==>',i
	print 'tables==>',switches[i]['tables']
	print 'dpid==>',switches[i]['dpid']

	print 



