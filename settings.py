'''
Created on May 7, 2019

@author: pascal
'''
import getopt, sys
import functools
import datetime
import os
from os import path


defaultSpif =  "/etc/spifmgr/default.spif"

typeErrorLabel = "Boolean needed"

class context():
    
	def __init__(self,progName):
		self.defaultHeight = 150
		self.defaultWidth = 800
		self.defaultX = 300
		self.defaultY = 300
		self.spifName = defaultSpif
		self.debugModeValue = False
		self.progBaseName = progName
		self.progLabel = "SPIF designer"
		self.progVersion = "0.0"
        
	@property
	def spif(self):
		return self.spifName
	@spif.setter
	def spif(self, value):
		if not isinstance(value, str): raise TypeError(typeErrorLabel)
		self.spifName = value

	@property
	def debugMode(self):
		return self.debugModeValue
	@debugMode.setter
	def debugMode(self, value):
		if not isinstance(value, bool): raise TypeError(typeErrorLabel)
		self.debugModeValue = value
    

	@property
	def progName(self):
		return self.progDirName
	@progName.setter
	def progName(self, value):
		if not isinstance(value, str): raise TypeError(typeErrorLabel)
		self.progDirName = value
	
	@property
	def windowHeight(self): return self.defaultHeight
	@property
	def windowWidth(self): return self.defaultWidth
	@property
	def windowX(self): return self.defaultX
	@property
	def windowY(self): return self.defaultY 

	@property
	def title(self): return self.progLabel
	@property
	def version(self): return self.progVersion

