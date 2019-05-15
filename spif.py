'''
Created on May 7, 2019

@author: pascal
'''

import xml.etree.ElementTree as ET
import settings 
from utils import debug, error
import os.path

class spif():
    '''
     Object that represents a Security Policy Information File
    '''
    
 


    def __init__(self, ctxt, fileName):
        '''
        Constructor
        '''
        debug(ctxt,"Parsing {file}".format(file=fileName))
        if not os.path.isfile(fileName):
        		error (ctxt,"{file} is not a file".format(file=fileName)) 

        try:
            self.root = ET.parse(fileName).getroot()
            self.fName = fileName
            self.ctxt = ctxt
        except ET.ParseError as e: error("Could not parse xml file {file} ({exception})".format(file=fileName, exception=str(e)))
    
    def __str__(self): return self.fName
    def getRoot(self): return self.root
    
    def getGeneralInfo(self):
        """ Fill in the general info dictionary (name and/or object id) """

        ns = {'spif': 'http://www.xmlspif.org/spif'}
        self.generalInfo = {}
        debug(self.ctxt,"Loading securityPolicyId object")
        
        if self.root.find("spif:securityPolicyId",ns) is None:
            error('No security policy id in template')
        if self.root.find("spif:securityPolicyId",ns).get('name') is None and self.root.find("spif:securityPolicyId",ns).get('id') is None:
            error('No security policy id or name in template')

           # Name and/or present : OK    -> fill in the dict    
            if self.root.find("spif:securityPolicyId",ns).get('id') is not None:
               self.generalInfo['policyId'] = self.root.find("spif:securityPolicyId",ns).get('id')
            if self.root.find("spif:securityPolicyId",ns).get('name') is not None:
                self.generalInfo['policyName'] = self.root.find("spif:securityPolicyId",ns).get('name')

