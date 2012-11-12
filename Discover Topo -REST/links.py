import os
import json

links = {}
controllerIP = '10.100.14.71'
cport = '8080'
data  = os.popen('curl -s http://'+controllerIP+ ':'+cport+'/wm/topology/links/json').read()

links = json.loads(data)


for i in range(len(links)):
	#print links[i]
	print 'link: ',i
	print 'src-switch==>',links[i]['src-switch']
	print 'src-port==>',links[i]['src-port']
	print 'dst-switch==>',links[i]['dst-switch']
	print 'dst-port==>',links[i]['dst-port']
	print 



