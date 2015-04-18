import os
import xml.etree.ElementTree as ET

command_list = []



def get_commands( path_file ):

	xtree = ET.parse(path_file)
	#element = xtree.find('.//div[@id="versions"]')
	root = xtree.getroot()
	
	#table = element[1][0][2]
	#test = u'\u2714'; #this is the check symbol
	#versions = []
	#for x in range(1, 13):
	#	text = table[0][x].text
	#	if text == test:
	#		versions.append(version_check[x])
	#return versions
	
	for element in root:
	    command_list.append(element[0].text)
		
def get_data( path_file ):

	xtree = ET.parse(path_file)
	#element = xtree.find('.//div[@id="versions"]')
	element = xtree.getroot()
	table = element[0]
	print table.attr
	test = u'\u2714'; #this is the check symbol
	versions = []
	#for x in range(1, 13):
	#	text = table[0][x].text
	#	if text == test:
	#		versions.append(version_check[x])	
		
		

get_commands("list.xml")

#print current_command_list
api = "el3"
for command in command_list:
	pathfile = api+"\\"+command+".xhtml"
	if(os.path.isfile(pathfile)):
		print "file exists"
		get_data(pathfile)
