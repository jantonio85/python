#!/usr/bin/env python
# -*- encoding: utf8 -*-

__version__ = '1.0'
__author__ = 'JoseAnt Morales'
__email__ = 'jamorales@tedial.com'

import sys;
import argparse
import lxml.etree as ET


"""Python script for separating the xml datamodel from repositories
This script take a common section and create several xml files depending the sifferents sections:

parameter1: xml datamodel (mandatory)
parameter2:
	- xsl file
	- Section: folders, types and thes (thesaurus)
parameter3: section
Only we can use one section value
Examples
files_export.py exportRepositoryT02.xml folders
XSLT by default exportTypes.xsl

folders created...
NRK_T02_folders.xml created...
files_export.py exportRepositoryT02.xml
All tags

folders created...
NRK_T02_folders.xml created...

types created...
NRK_T02_types.xml created...

thes created...
NRK_T02_thes.xml created...
"""

project = 'NRK'
tenant='T02'


def createXML(xml,xsl,typeXML):
	#print typeXML
	if typeXML == 'folders' or typeXML == 'thes' or typeXML == 'types':
		newdom = transform(dom,node=ET.XSLT.strparam(typeXML))
		#print(ET.tostring(newdom, pretty_print=True))
    		#print 'Folder XML Result created....'infile = unicode((ET.tostring(newdom, pretty_print=True)))
		infile = unicode((ET.tostring(newdom, pretty_print=True)))
		print typeXML+' created...'
		#name = project_tenant_type.xml

		name=project+'_'+tenant+'_'+typeXML+'.xml'
    		#outfile= open ('xml_result_folder.xml','a')
		outfile= open (name,'a')
    		outfile.write(infile)
		print name+' created... \n'
	else:
		print 'Incorrect type: Valid types folders, types, thes \n'

try:

	xml=sys.argv[1]

	xsl='exportTypes.xsl'
	#print 'XSLT: '+ xsl + '\n'
	#print 'XSLT by default '+xsl+'\n'

	if (sys.argv[2].find('.xsl')>-1):
		#print str(sys.argv[1].find('.xsl'))
		xsl=sys.argv[2]
		print 'XSLT: '+ xsl + '\n'
		types=sys.argv[3]


	else:
		types=sys.argv[2]


		print 'XSLT by default '+xsl+'\n'


	dom = ET.parse(xml)
	xslt = ET.parse(xsl)
	transform = ET.XSLT(xslt)
	createXML(dom,xsl,types)


except IndexError:
	if not xml: print 'XML not found'
	else:
		print 'All tags \n'
		dom = ET.parse(xml)
        	xslt = ET.parse(xsl)
	        transform = ET.XSLT(xslt)
			#We create a xml result for each node
	        #FOLDER XML
        	createXML(dom,xsl,"folders")


	        #We create a xml result for each node
	        #TYPES XML
        	createXML(dom,xsl,"types")


	        #We create a xml result for each node
	        #THES XML
        	createXML(dom,xsl, "thes")
