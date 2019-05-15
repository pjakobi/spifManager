'''
Created on May 8, 2019

@author: pascal
'''
import os
import sys
from settings import context 


        
def usage(ctxt):
    print (os.path.basename(ctxt.progName) + ":")
    print ("\t-h or --help : this message")
    print ("\t-d or --debug: debug mode")
    print ("\t-v or --verbose: verbose mode (same as debug)")
    print ("\t-f or --file <filename>")
    print ("\t-s or --spif <filename>")    
    sys.exit(0)
    
def debug(ctxt,debugLabel):
    if ctxt.debugMode : 
        print ("{prefix} info: {label}".format(prefix=ctxt.progName, label=debugLabel))
        
def error(ctxt,errorLabel):
    sys.stderr.write("{prefix} error: {label}\n".format(prefix=ctxt.progName, label=errorLabel))
    sys.exit(2)