from netaddr import *
import pprint
from math import log2,ceil

class interface(object):
	def __init__(self,name,switchport,ipv4address=None):
		self.name = name
		self.ipv4address = ipv4address
		self.switchport = switchport


class device(object):
	def __init__(self,name,int_list,location):
		self.name =  name
		self.int_list = int_list
		self.location = location



class Link(object):
	def __init__(self,name,int1,int2):
		self.name = name
		self.int1 = int1
		self.int2 = int2

	def getAdd(self):
		if self.int1.ipv4address == None :
		    print ("This is a switchport - Access ")
		else :
		    print ("1st @: "+str(self.int1.ipv4address))

		if self.int2.ipv4address == None :
		    print ("This is a switchport - Access ")
		else :
		    print ("2nd @: "+str(self.int2.ipv4address))




class Topology(object):
	def __init__(self, name , devices , links,terminals,network_add=None):
		self.name = name
		self.devices = devices
		self.links = links
		self.terminals = terminals
		self.network_add = network_add

	def adressing(self):
		subnetsnum =  log2(len(self.links)) / log2(2)
		subnetsnum = ceil(subnetsnum)
		netip = IPNetwork(self.network_add)
		newprefix = netip.prefixlen + subnetsnum
		print ("The new subnet mask : "+str(newprefix))
		subnets = list(netip.subnet(newprefix))
		print (subnets[1].netmask)
		cmp = 0
		for link in self.links:
			subnet = subnets[cmp]
			addresses  = subnet.iter_hosts()
			firstadd = next(addresses)
			secondadd = next(addresses)
			print (firstadd)
			print (secondadd)


			if link.int1.switchport == False :
				link.int1.ipv4address = firstadd
			else :
				link.int1.ipv4address = None


			if link.int2.switchport == False :
				link.int2.ipv4address = secondadd
			else :
				link.int2.ipv4address = None

			cmp+=1

		for link in self.links:
			link.getAdd()












if __name__ == "__main__":

	interface1 = interface("ethernet0/0",False)
	interface2 = interface("ethernet0/1",False)
	interface3 = interface("ethernet0/1",False)
	interface4 = interface("ethernet0/1",False)
	interface5 = interface("ethernet0/1",False)
	interface6 = interface("ethernet0/1",False)
	intlist1 = []
	intlist1.append(interface1)
	intlist1.append(interface2)
	intlist1.append(interface3)
	intlist1.append(interface4)
	intlist1.append(interface5)
	intlist1.append(interface6)
	switch1  = device("DSW1",intlist1,"AGG")


	interface7 = interface("ethernet0/0",False)
	interface8 = interface("ethernet0/1",False)
	interface9 = interface("ethernet0/1",False)
	interface10 = interface("ethernet0/1",False)
	interface11 = interface("ethernet0/1",False)
	interface12 = interface("ethernet0/1",False)
	intlist2 = []
	intlist2.append(interface7)
	intlist2.append(interface8)
	intlist2.append(interface9)
	intlist2.append(interface10)
	intlist2.append(interface11)
	intlist2.append(interface12)
	switch2  = device("DSW2",intlist2,"AGG")



	interface13 = interface("ethernet0/1",False)
	interface14 = interface("ethernet0/1",False)
	intlist3 = []
	intlist3.append(interface13)
	intlist3.append(interface14)
	Router = device("router1",intlist3,"Core")

	interface16 = interface("eth0/0",True)
	interface17 = interface("eth0/1",True)
	interface18 = interface("eth0/0",True)
	interface19 = interface("eth0/1",True)
	interface20 = interface("eth0/0",True)
	interface21 = interface("eth0/1",True)
	interface22 = interface("eth0/0",True)
	interface23 = interface("eth0/1",True)

	asw1intlist = []
	asw1intlist.append(interface16)
	asw1intlist.append(interface17)
	asw2intlist = []
	asw2intlist.append(interface18)
	asw2intlist.append(interface19)
	asw3intlist = []
	asw3intlist.append(interface20)
	asw3intlist.append(interface21)
	asw4intlist = []
	asw4intlist.append(interface22)
	asw4intlist.append(interface23)
	asw1  = device("DSW2",asw1intlist,"ACC")
	asw2  = device("DSW2",asw2intlist,"ACC")
	asw3  = device("DSW2",asw3intlist,"ACC")
	asw4  = device("DSW2",asw4intlist,"ACC")
	link1 = Link("1",interface1,interface13)
	link2 = Link("2",interface7,interface14)
	link3 = Link("3",interface2,interface8)
	link4 = Link("4",interface3,interface16)
	link5 = Link("5",interface4,interface18)
	link6 = Link("6",interface5,interface20)
	link7 = Link("7",interface6,interface22)
	link8 = Link("8",interface9,interface17)
	link9 = Link("9",interface10,interface19)
	link10 = Link("10",interface11,interface21)
	link11 = Link("11",interface12,interface23)
	links = []
	links.append(link1)
	links.append(link2)
	links.append(link3)
	links.append(link4)
	links.append(link5)
	links.append(link6)
	links.append(link7)
	links.append(link8)
	links.append(link9)
	links.append(link10)
	links.append(link11)

	devices  = []
	devices.append(switch1)
	devices.append(switch2)
	devices.append(Router)
	devices.append(asw1)
	devices.append(asw2)
	devices.append(asw3)
	devices.append(asw4)

	OurTopology = Topology("topology1",devices,links,200,"192.168.0.0/16")
	OurTopology.adressing()



	#abbouiadjra
