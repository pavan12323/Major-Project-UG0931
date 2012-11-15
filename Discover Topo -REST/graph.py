""" This is a simple application based on REST API 
@author Basavesh
"""


import os 				# OS Calls
import sys 				# System Calls
import json				# To convert to and fro from json to python objects
try:
	import networkx as nx           # package to do graph manipulations
except Exception:
	print "Please install networkX and try again"
	sys.exit()

try:
	import matplotlib.pyplot as plt  # package to draw graphs
except Exception:
	print "Please install matplotlib and try again"
	sys.exit()

controllerIP = 'localhost'		 # 
cport = '8080'

class MyTopology(object):
	"""Class for visualizing mininet topology"""
	def __init__(self):
		'''Constructor for this class  '''
		self.endDevices = {}
		self.switches = []
		self.switches_adj = {}
		self.links = {}


	def add_endDevice(self, ip, mac, to_switch, to_port):
		"""Method to add End Devides. ex: hosts """
		self.endDevices[ip] = {}
		self.endDevices[ip]['mac'] = mac
		self.endDevices[ip]['to_switch'] = to_switch
		self.endDevices[ip]['to_port'] = to_port	
		
	def add_switch(self, dpid):
		""" Method to add switches based on their dpid"""
		self.switches.append(dpid)


	def add_link(self, src, dst, src_port, dst_port, weight = 1):
		""" Method to add link and it's attributes """
		if src not in self.switches_adj:
			self.switches_adj[src] = []
		self.switches_adj[src].append(dst)	


		#add link and it's attributes
		if src not in self.links:
			self.links[src] = {}
		self.links[src][dst] = {}
		self.links[src][dst]['src_port'] = src_port
		self.links[src][dst]['dst_port'] = dst_port
		self.links[src][dst]['weight'] = weight 

		

topology = MyTopology() # Created an empty instance of Mytopology 


##### Fetch data From Controller using REST API ############################

######################## get list of all switches ##########################
try:
	command = 'curl -s http://'+controllerIP+ \
	          ':'+cport+'/wm/core/controller/switches/json'

except Exception:
	print "make sure that the controller is running"
	sys.exit()

data  = os.popen(command).read()
switches = json.loads(data)

for i in range(len(switches)):
	switch_dpid = switches[i]['dpid']
	topology.add_switch(switch_dpid)
#################################end #######################################

####################### get list of end devices ############################
command = 'curl -s http://'+controllerIP+ ':'+cport+'/wm/device/'
data  = os.popen(command).read()
hosts = json.loads(data)
for i in range(len(hosts)):
	if len(hosts[i]['attachmentPoint']) > 0:
		try:
			ipv4 = hosts[i]['ipv4'][0]
			mac = hosts[i]['mac'][0]
			to_switch = hosts[i]['attachmentPoint'][0]['switchDPID']
			to_port = hosts[i]['attachmentPoint'][0]['port']
			topology.add_endDevice(ipv4, mac, to_switch, to_port)
		except Exception:
			print 'Please do pingall so that controller will know'+ \
			      ' all host\'s ipv4 address'
			sys.exit()
################################end ########################################


################## get list of links #######################################
command = 'curl -s http://'+controllerIP+ ':'+cport+'/wm/topology/links/json'
data  = os.popen(command).read()
links = json.loads(data)

for i in range(len(links)):
	src_switch = links[i]['src-switch']
	src_port = links[i]['dst-switch']
	dst_switch = links[i]['src-port']
	dst_port = links[i]['dst-port']
	topology.add_link(src_switch, src_port, dst_switch, dst_port)
############################# end ##########################################


###### Create Graph from the above topoly using networkX ###################
G = nx.Graph(name='Mininet topo of only switches') #Empty undirected graph
# add switches
for i in range(len(switches)):
	G.add_node(switches[i]['dpid'])

#print the registered switches
if len(G.nodes()) == 0:
	print 'No switches present'
	sys.exit()

print "Printing switches "
for switch in G.nodes():
	print 'Switch ==> ',switch
print 

# add links / edges 
# networkx will take care of the two half duplex links
for src in topology.links:
	for dst in topology.links[src]:
		G.add_edge(src,dst)

# print all edges and links
print "Printing Edges"
for src, dst in G.edges():
	print "Edge/link  {} <==> {} ".format(src,dst)
print

# use Dijstr's algorithm to find shortest path
path_matrix = nx.shortest_path(G) #computes for whole graph

#printing the End Devices
print "printing the End Devices"
for host in topology.endDevices:
	print "End Device ipv4 ==> {}".format(host)
print

# get the Source from user
Source = raw_input('Please input the ipv4 address of host from which you\
want to ping. ex: A.B.C.D ')
print 


# Test if source is present in topology
if Source not in topology.endDevices:
	print "There is no host with this IP address"
	sys.exit()

# get the Destination from user
Destination = raw_input('Please input the ipv4 address of host to \
which you want to ping. ex: A.B.C.D ')
print 

# Test if the destination is present in topology
if Source not in topology.endDevices:
	print "There is no host with this IP address"
	sys.exit()

# Get the Switch for which host is attached to 
Source_switch = topology.endDevices[Source]['to_switch']

Destination_switch = topology.endDevices[Destination]['to_switch']


# Print the path which will be used to ping
print 'Path taken is'
print 'host-{} ==> '.format(Source),
for switch in path_matrix[Source_switch][Destination_switch]:
	print 'Switch-{} ==> '.format(switch),
print 'host-{}'.format(Destination)
print
#print multiple shortest paths 
print 'Multiple Shortest path available are'
for path in nx.all_shortest_paths(G,source=Source_switch, target=Destination_switch):
	print 'host-{} ==> '.format(Source),
	for nodes in path:
		print 'Switch-{} ==> '.format(switch),
	print 'host-{}'.format(Destination)
	print



print
print
# Trying to push one flow entry to switch ==>
print 'trying to add one dummy flow entry to Source_switch' 

shortest_path = path_matrix[Source_switch][Destination_switch]

for i in range(len(shortest_path)):
	j = i+1
	if j == len(shortest_path):
		break
	print 'src-{} port-{} ==> dst-{} port-{}'.format(shortest_path[i],topology.links[shortest_path[i]][shortest_path[j]]['src_port'], shortest_path[j], topology.links[shortest_path[i]][shortest_path[j]]['dst_port'])




'''
#command = "curl -d -s '{}' http://".format(str(flow_entry))+controllerIP+ ":"+cport+"/wm/staticflowentrypusher/json"
command = "curl -s -d '{\"switch\": \"%s\", \"name\":\"%s\", \"ether-type\":\"%s\", \"cookie\":\"0\", \"priority\":\"32768\", \"ingress-port\":\"%s\",\"active\":\"true\", \"actions\":\"output=%s\",\"src-ip\":\"%s\",\"dst-ip\":\"%s\"}' http://%s/wm/staticflowentrypusher/json" % (Source_switch, "flow-mod-1", "0x806", 1, 2,Source,Destination, "localhost:8080")
print command
result  = os.popen(command).read()
'''



#nx.draw(G)
#plt.show()

#curl -d '{"switch": "00:00:00:00:00:00:00:01", "name":"flow-mod-1", "cookie":"0", "priority":"32768", "ingress-port":"1","active":"true", "actions":"output=2"}' http://<controller_ip>:8080/wm/staticflowentrypusher/json