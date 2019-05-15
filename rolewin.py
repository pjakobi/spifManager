'''
Created on May 7, 2019

@author: pascal
'''
import sys

import os
from settings import context 
from utils import error, debug
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMenuBar

class roleWin(QMainWindow):

	def __init__(self, ctxt):
		super(roleWin,self).__init__()
		self.resize(ctxt.windowWidth, ctxt.windowHeight) 
		self.move(ctxt.windowX, ctxt.windowY) 
		self.setWindowTitle("{prog} {version} - {file}".format(prog=ctxt.title,version=ctxt.version,file=os.path.basename(ctxt.spif))) 
		menu = self.menuBar().addMenu('File')


		




