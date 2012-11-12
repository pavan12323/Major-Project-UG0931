import os
import json

hosts = {}
controllerIP = '10.100.14.71'
cport = '8080'
command = 'curl -s http://'+controllerIP+ ':'+cport+'/wm/device/'

data  = os.popen(command).read()


hosts = json.loads(data)


for i in range(len(hosts)):
	if len(hosts[i]['attachmentPoint']) > 0:
		print 'Host Mac==>', hosts[i]['mac'][0]
		print 'connected to Switch==>', hosts[i]['attachmentPoint'][0]['switchDPID']
		print 'to Switch port==>', hosts[i]['attachmentPoint'][0]['port']
		print 

