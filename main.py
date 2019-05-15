'''
Created on May 7, 2019

@author: pascal
'''
import getopt, sys

import os
from spif import spif
from settings import context 
from utils import usage, debug
from rolewin import roleWin

from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget

if __name__ == '__main__':
    currentSettings = context(os.path.basename(sys.argv[0]))
    currentSettings.progName = os.path.basename(sys.argv[0])

	
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hds:f:",["help","debug","spif=","file="])
    except getopt.GetoptError:
        usage(currentSettings)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage(currentSettings)
        elif opt in ("-d", "--debug", "-v", "--verbose"):
            currentSettings.debugMode = True
            debug(currentSettings,"Debug mode set")
        elif opt in ("-f", "--file", "-s", "--spif="):
            debug(currentSettings,"Loading {}".format(arg))
            currentSettings.spif = str(arg)


currentSpif = spif(currentSettings,currentSettings.spif)
currentSpif.getGeneralInfo()
app = QApplication(sys.argv)

# w = QWidget() 
# w.resize(currentSettings.windowWidth, currentSettings.windowHeight) 
# w.move(currentSettings.windowX, currentSettings.windowY) 
#w.setWindowTitle(os.path.basename(currentSettings.spif)) 
w = roleWin(currentSettings)
w.show() 

sys.exit(app.exec_())

